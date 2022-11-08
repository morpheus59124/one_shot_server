import os
os.system("apt install gpg -y")
os.system('echo "deb http://repo.mongodb.org/apt/debian bullseye/mongodb-org/5.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list')
os.system("curl -sSL https://www.mongodb.org/static/pgp/server-5.0.asc  -o mongoserver.asc")
os.system("gpg --no-default-keyring --keyring ./mongo_key_temp.gpg --import ./mongoserver.asc")
os.system("gpg --no-default-keyring --keyring ./mongo_key_temp.gpg --export > ./mongoserver_key.gpg")
os.system("sudo mv mongoserver_key.gpg /etc/apt/trusted.gpg.d/")
os.system("sudo apt update -y")
os.system("sudo apt install mongodb-org -y")
os.system("sudo systemctl enable --now mongod")


