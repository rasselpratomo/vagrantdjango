box = "ubuntu/trusty64"
install_path = "install.sh"
ip = "127.0.0.1"

Vagrant.configure(2) do |config|
  config.vm.box = box
  config.vm.network :forwarded_port, guest: 8000, host: 9000, host_ip: ip

  config.vm.provision :shell, :path => install_path.sh
end
