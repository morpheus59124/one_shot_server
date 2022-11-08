#installation de Apache2
import os

os.system("apt install apache2 -y")
os.system("systemctl start apache2")
os.system("systemctl enable apache2")
os.system("a2enmod ssl")
os.system("systemctl reload apache2")
os.system("apt install python3-certbot-apache -y")
os.system("certbot --apache")
os.system("systemctl reload apache2")


