vagrant up
vagrant ssh --command 'cd /vagrant; sudo bash maintenance/install_deps.sh'
vagrant ssh --command 'cd /vagrant; sudo bash maintenance/install_python.sh'
vagrant ssh --command 'cd /vagrant; sudo bash maintenance/install_app.sh'
vagrant ssh --command 'cd /vagrant; sudo bash maintenance/test.sh'
