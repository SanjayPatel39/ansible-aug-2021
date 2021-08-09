### Installing Git
```
su -
yum install git
```

### Cloning this repository (Try this command as devops user only the first time)
```
git clone https://github.com/tektutor/ansible-aug-2021.git
cd ansible-aug-2021
```

### Moving forward, every time I push new code, you need to pull(not clone)
```
cd /home/devops/ansible-aug-2021
git pull
```

### Installing Ansible
```
su -
yum install -y epel-release
yum install -y ansible
```

You may now check the version of Ansible installed
```
ansible --version
```
The expected output is
<pre>
[jegan@localhost Ansible]$ ansible --version
ansible 2.9.23
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/jegan/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.6/site-packages/ansibleYou may s
  executable location = /usr/bin/ansible
  python version = 3.6.8 (default, Aug 24 2020, 17:57:11) [GCC 8.3.1 20191121 (Red Hat 8.3.1-5)]
[jegan@localhost Ansible]$ 
</pre>

### Installing Docker Community Edition
```
su -
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce
```

#### Troubleshooting Docker installation issue
```
su -
yum install -y docker-ce --allowerasing
```

#### Starting the docker service
```
su -
systemctl enable docker
systemctl start docker
systemctl status docker
```
To come out of the status command, type 'q'

You may check if you are able to execute docker commands as regular user
```
docker --version
docker images
```

#### Troubleshooting permission denied issue
```
su -
usermod -aG docker devops
sudo su devops
docker images
```

### Generate you key pair for devops user
```
ssh-keygen
```
The expected output is shown below

<pre>
Generating public/private rsa key pair.
Enter file in which to save the key (/home/devops/.ssh/id_rsa): 
Created directory '/home/devops/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/devops/.ssh/id_rsa.
Your public key has been saved in /home/devops/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:zJM9Xq61M4HQ31aBkDPqFff37hr6iCfeF8dLJCd0E7I devops@localhost.localdomain
The key's randomart image is:
+---[RSA 3072]----+
|           .o....|
|           = +o+ |
|         .. *Eo o|
|       o.+.. o +o|
|        S.+o..=oo|
|         +.+o +.+|
|          . ooo+.|
|          .=++.o.|
|         .+o==oo.|
+----[SHA256]-----+
[devops@localhost ~]$ 
</pre>

### Building a custom ubuntu ansible node
```
cd /home/devops/ansible-aug-2021
git pull
cd Day1/ubuntu-ansible
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-ubuntu .
```
You may optionally change 'tektutor' startup name with your organization name.

#### See if you are able to list the custom images
```
docker images
```
The expected output is
<pre>
[jegan@localhost ubuntu-ansible]$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
tektutor/ansible-ubuntu   latest    fbd15f46e99a   14 seconds ago   220MB
ubuntu                    16.04     38b3fa4640d4   13 days ago      135MB
[jegan@localhost ubuntu-ansible]$ 
</pre>

### Create ubuntu1 and ubuntu2 containers out of the newly build custom image
```
docker run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 -p 8001:80 tektutor/ansible-ubuntu
docker run -d --name ubuntu2 --hostname ubuntu2 -p 2002:22 -p 8002:80 tektutor/ansible-ubuntu
```

#### List the containers
```
docker ps
```
The expected output is
<pre>[jegan@localhost Day1]$ docker ps
CONTAINER ID   IMAGE                     COMMAND               CREATED          STATUS          PORTS                                                                          NAMES
9d46ec6d3a5d   tektutor/ansible-ubuntu   "/usr/sbin/sshd -D"   7 seconds ago    Up 5 seconds    0.0.0.0:2002->22/tcp, :::2002->22/tcp, 0.0.0.0:8002->80/tcp, :::8002->80/tcp   ubuntu2
aa5a4350bc75   tektutor/ansible-ubuntu   "/usr/sbin/sshd -D"   20 seconds ago   Up 18 seconds   0.0.0.0:2001->22/tcp, :::2001->22/tcp, 0.0.0.0:8001->80/tcp, :::8001->80/tcp   ubuntu1
</pre>

#### Test ssh connectivity (as devops user)
```
ssh -p 2001 root@localhost
exit
ssh -p 2002 root@localhost
exit
```
When it prompts with the question, you need to type yes
```
Are you sure, do you want to continue connecting yes/no?
```
The expected output is shown below
<pre>
[jegan@localhost Day1]$ ssh -p 2001 root@localhost
The authenticity of host '[localhost]:2001 ([::1]:2001)' can't be established.
ECDSA key fingerprint is SHA256:irBMfGdAaC2ufLDoygathering=explicit0KZsb5D33z7eqtF/+lv30OxHIY.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2001' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.18.0-240.el8.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.
</pre>

### Troubleshooting git pull
Delete the file that errors out, for example
```
rm -f /home/devops/ansible-aug-2021/Day1/ubuntu-ansible/authorized_keys
git pull
```

### Executing Ansible ad-hoc command
```
cd Day1
ansible -i inventory -m ping
```

The expected output is shown below

<pre>
[jegan@localhost Ansible]$ cd Day1
[jegan@localhost Day1]$ ls
inventory  ubuntu-ansible
[jegan@localhost Day1]$ pwd
/home/jegan/Ansible/Day1
[jegan@localhost Day1]$ ls -l
total 4
-rw-rw-r--. 1 jegan jegan 218 Aug  9 00:30 inventory
drwxrwxr-x. 2 jegan jegan  47 Aug  8 23:53 ubuntu-ansible
[jegan@localhost Day1]$ ansible -i inventory all -m ping
ubuntu2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
ubuntu1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
[jegan@localhost Day1]$ 
</pre>

### What happens when you execute an Ansible adhoc command
1. Ansible Creates a temp directory in the ACM and on the Ansible Node(s).
2. Ansible then copies the ansible module from ACM into the ACM temp folder and paste all the python inclues inline in the same python script.
3. Using sftp/scp, Ansible then copies from the python script from ACM temp to Ansible Node temp folder.
4. Ansible gives execute permission to the Python script.
5. Executes the Python script on the Ansible Nodes and captures the output from the remote machines.
6. Cleans up by deleting the temp folder on the ansible remote machines.
7. Gives a summary of output in the ACM.

### Executing the Ansible Playbook
```
cd ~/ansible-aug-2021
git pull
cd Day1
ansible-playbook -i inventory ping.yml
```

### Executing the Ansible Playbook when ansible.cfg is present in current directory
```
cd ~/ansible-aug-2021
git pull
cd Day1
ansible-playbook ping.yml
```
