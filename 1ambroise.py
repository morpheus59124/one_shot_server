import paramiko
from scp import SCPClient

#Import de la clé privée (Si déjà configurée)
#pkey = paramiko.RSAKey.from_private_key_file("/home/eric/.ssh/id_rsa")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Passphrase -> La phrase de passe de la clé privée, si on se connecte avec un mdp => utiliser password=
ssh.connect(hostname="82.165.52.3", port=22, username="root", password="PASSWORD")

#ssh.exec_command()
scp = SCPClient(ssh.get_transport())
scp.put("D:/Bureau/infra/install.py", "/home/test/install.py") 
scp.put("D:/Bureau/infra/2.py", "/home/test/2.py") 
scp.put("D:/Bureau/infra/application.conf", "/home/test/application.conf") 
scp.put("D:/Bureau/infra/application.service", "/home/test/application.service")
scp.put("D:/Bureau/infra/3.py", "/home/test/3.py")
scp.put("D:/Bureau/infra/4.py", "/home/test/4.py")
scp.put("D:/Bureau/infra/5.py", "/home/test/5.py")
scp.put("D:/Bureau/infra/7.py", "/home/test/7.py")
scp.put("D:/Bureau/infra/99.py", "/home/test/99.py")
scp.put("D:/Bureau/infra/100.sh", "/home/test/100.sh")
scp.put("D:/Bureau/infra/101.py", "/home/test/101.py")
scp.put("D:/Bureau/infra/start.sh", "/home/test/start.sh")
scp.put("D:/Bureau/infra/travelproject.service", "/home/test/travelproject.service")
scp.put("D:/Bureau/infra/101.sh", "/home/test/101.sh")

ssh.close()