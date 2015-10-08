sudo apt-get update -y
sudo apt-get install python-pip -y
sudo pip install django
cd /vagrant/testproject
python manage.py runserver 0.0.0.0:8000 >/dev/null 2>&1 &
