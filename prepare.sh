
apt-get update
apt-get install -y software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install -y python3.6
apt-get install -y python3-pip
apt-get install -y virtualenv
virtualenv --python=/usr/bin/python3.6 py36
source py36/bin/activate
pip install torch stanfordnlp
apt-get install -y default-jdk

