# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.ssh.username = 'vagrant'

  config.vm.synced_folder "../", "/code", mount_options: ["dmode=777,fmode=777"]

  config.vm.define :production do |production|
    production.vm.network :public_network, :bridge => 'eth0', :auto_config => false
    production.vm.provider :virtualbox do |vb|

        host = RbConfig::CONFIG['host_os']

        # Give VM 1/4 system memory & access to all cpu cores on the host
        if host =~ /darwin/
            cpus = `sysctl -n hw.ncpu`.to_i
            # sysctl returns Bytes and we need to convert to MB
            mem = `sysctl -n hw.memsize`.to_i / 1024 / 1024 / 4
        elsif host =~ /linux/
            cpus = `nproc`.to_i
            # meminfo shows KB and we need to convert to MB
            mem = `grep 'MemTotal' /proc/meminfo | sed -e 's/MemTotal://' -e 's/ kB//'`.to_i / 1024 / 4
        else # sorry Windows folks, I can't help you
            cpus = 2
            mem = 1024
        end

        vb.customize ["modifyvm", :id, "--memory", mem]
        vb.customize ["modifyvm", :id, "--cpus", cpus]
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
    end
    config.vm.provision "ansible" do |ansible|
        ansible.host_key_checking = false
        ansible.sudo = true
        ansible_inventory_path = "inventory.ini"
        ansible.playbook = "playbook.yml"
    end
    config.vm.network :private_network, ip: "192.168.56.151"   
  end

end
