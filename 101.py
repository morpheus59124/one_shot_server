import os

os.system("cp /home/test/travelproject.service /etc/systemd/system/")
os.system("cp /home/test/start.sh /var/www/application/")

os.system("chmod +x /var/www/application/start.sh")

os.system("systemctl enable travelproject.service")
os.system("systemctl start travelproject.service")