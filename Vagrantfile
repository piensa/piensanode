# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.ssh.username = 'vagrant'

  config.vm.synced_folder ".", "/srv/git/piensanode", mount_options: ["dmode=777,fmode=777"]

  config.vm.define :production do |production|
    production.vm.network :public_network, :bridge => 'eth0', :auto_config => false
    production.vm.provider :virtualbox do |vb|
        vb.customize [ "modifyvm", :id, "--name", "piensanode-prod","--memory", 4096 ]
    end
    config.vm.provision "ansible" do |ansible|
        ansible.host_key_checking = false
        ansible.sudo = true
        ansible_inventory_path = "inventory.ini"
        ansible.playbook = "playbook.yml"
    end
    config.vm.network :private_network, ip: "192.168.56.151"   
    config.vm.provision :shell, :inline => "sudo service uwsgi restart", run: "always"
  end

end
