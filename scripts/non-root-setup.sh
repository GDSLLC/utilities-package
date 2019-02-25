cd /home/vagrant
virtualenv --python python3.6 venv
. venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r /vagrant/requirements.txt

