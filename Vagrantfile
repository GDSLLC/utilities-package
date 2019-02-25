Vagrant.configure("2") do |config|
  config.ssh.forward_agent = true
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.provider "virtualbox" do |v|
    v.customize ['modifyvm', :id, '--nictype1', 'virtio']
    v.memory = 4096
  end
end
