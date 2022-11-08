# installation de Fail2ban
import os
os.system("apt install fail2ban -y")
os.system("systemctl start fail2ban")
os.system("systemctl enable fail2ban")
os.system("echo '[sshd]\nenabled = true\nport = 2222\nlogpath = /var/log/auth.log\nmaxretry = 3' >> /etc/fail2ban/jail.d/defaults-debian.conf")
os.system("exit")



