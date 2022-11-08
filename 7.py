#installation de python flask
import os
os.system("apt install python3-pip -y")
os.system("apt install git -y")
os.system("mkdir /var/www/application")
os.system("cd /var/www/")
os.system("git clone https://github.com/gfaille/RedFace_bike_race.git")
os.system("cp -R /home/test/RedFace_bike_race/* /var/www/application")
os.system("sudo chown -R www-data:www-data /var/www/application")
os.system("sudo apt install python3-flask python3-gunicorn gunicorn3 -y")
os.system("pip install pymongo flask Flask-Markdown Flask-WTF Flask-Ext")
os.system("exit")