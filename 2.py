#installation de nginx
import os

os.system("apt install nginx -y")
os.system("systemctl start nginx")
os.system("systemctl enable nginx")
os.system("cp /home/test/application.conf /etc/nginx/sites-available/")
os.system("cp /home/test/application.service /etc/systemd/system/")
os.system("ln -s /etc/nginx/sites-available/application.conf /etc/nginx/sites-enabled/")
os.system("systemctl restart nginx")
os.system("systemctl restart application.service")
os.system("systemctl daemon-reload")
os.system("exit")
