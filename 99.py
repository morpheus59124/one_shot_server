import fileinput
import os

for line in fileinput.input("/etc/ssh/sshd_config", inplace=True):
        print(line.replace("#Port 22", "Port 2222"), end="")

for line in fileinput.input("/etc/ssh/sshd_config", inplace=True):
        print(line.replace("PermitRootLogin yes", "PermitRootLogin no"), end="")

for line in fileinput.input("/etc/ssh/sshd_config", inplace=True):
        print(line.replace("#PubkeyAuthentication yes", "PubkeyAuthentication no"), end="")

#for line in fileinput.input("/etc/ssh/sshd_config", inplace=True):
        #print(line.replace("UsePAM yes", "UsePAM no"), end="")

for line in fileinput.input("/etc/ssh/sshd_config", inplace=True):
        print(line.replace("#PermitEmptyPasswords no", "PermitEmptyPasswords no"), end="")


