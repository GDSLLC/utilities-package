Vagrant.configure("2") do |config|
  config.ssh.forward_agent = true
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.provision "shell", inline: 'bash /vagrant/scripts/root-setup.sh', keep_color: true
  config.vm.provider "virtualbox" do |v|
    v.customize ['modifyvm', :id, '--nictype1', 'virtio']
    v.memory = 4096
  end
end
