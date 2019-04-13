DEBIAN_FRONTEND=noninteractive apt-get -y -o DPkg::options::="--force-confdef" -o DPkg::options::="--force-confold" update
DEBIAN_FRONTEND=noninteractive apt-get -y -o DPkg::options::="--force-confdef" -o DPkg::options::="--force-confold" upgrade

apt install -y --quiet ca-certificates

apt install -y build-essential
apt install -y linux-headers-$(uname -r)

apt install -y libssl-dev libffi-dev

apt install -y python-virtualenv
apt install -y python-setuptools
apt install -y python-pip

apt install -y python3
apt install -y python3-pip
apt install -y python3-dev

apt install -y git

apt install -y wget
apt install -y curl
apt install -y rsync
apt install -y p7zip
apt install -y zip
apt install -y unzip
apt install -y xclip

apt install -y emacs