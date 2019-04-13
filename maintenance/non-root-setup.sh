cd /home/vagrant
virtualenv --python python3.6 venv
. venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools

if [ -d "/vagrant" ]; then
  pip install -r /vagrant/requirements.txt
fi

if [ ! -d "/vagrant" ]; then
  pip install -r ~/repo/requirements.txt
fi
