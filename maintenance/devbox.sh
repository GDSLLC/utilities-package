vagrant up
vagrant ssh --command 'cd /vagrant; sudo bash maintenance/install_deps.sh'
vagrant ssh --command 'cd /vagrant; sudo bash maintenance/create_venv.sh'
vagrant ssh --command 'cd /vagrant; sudo bash maintenance/install_app.sh'
vagrant ssh --command 'cd /vagrant; sudo bash maintenance/test.sh'
