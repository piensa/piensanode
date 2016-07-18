Piensanode
===========

0. Git clone this repo to your local dev box:

    git clone https://github.com/piensa/piensanode.git
    
1. Have a HHyperMap checkout in the parent folder where this is checked out.

    git clone https://github.com/cga-harvard/HHypermap.git -b registry
    
2. Install Vagrant and Ansible (2.0+)

    vagrant up

3. If you are working on HHyperMap, install it from source inside the virtual machine:

   vagrant ssh
   source venvs/piensanode/bin/activate
   pip install -e /code/HHyperMap

4. Access the server on:

    http://192.168.56.151/
    
    
