### Install Docker CE in RHEL 8
```
sudo su -
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce
systemctl enable docker && systemctl start docker
systemctl status docker
usermod -aG docker ec2-user
```

### Test docker
```
docker --version
docker images
```

### Let's install git, vim and tree utility
```
sudo su -
yum install -y git tree vim
```

### Install Ansible
```
sudo su -
yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install -y ansible
```

### Test Ansible installation
```
ansible --version
```

### Clone the TekTutor github repo for all the source code
```
git clone http://github.com/tektutor/ansible-aug-2021.git
```

### Create key pair for root user
```
sudo su -
ssh-keygen
```
Accept all defaults by hitting enter thrice without modifying any options while generating ssh-keygen

### Building ansible node docker images
```
sudo su -
pip3 install docker-py
cd ansible-aug-2021/Day2
cp /root/.ssh/id_rsa.pub authorized_keys
ansible-playbook build-ansiblenode-docker-images-playbook.yml
```

### Verify if the ubuntu and centos nodes images are built properly
```
docker images
```
The expected output is shown below
<pre>
root@ip-172-31-2-163 Day2]# docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
tektutor/ansible-centos   latest    66705dfb276b   5 seconds ago    257MB
tektutor/ansible-ubuntu   latest    bf41d1242e83   30 seconds ago   220MB
ubuntu                    16.04     38b3fa4640d4   2 weeks ago      135MB
centos                    8         300e315adb2f   8 months ago     209MB
[root@ip-172-31-2-163 Day2]# 
</pre>

### Let's provision couple of containers on ubuntu and centos
```
cd ansible-aug-2021/Day2/Loops
ansible-playbook provision-containers-playbook.yml
```

### See if the containers are running
```
docker ps
```
The expected output is
<pre>
[root@ip-172-31-2-163 Loops]# docker ps
CONTAINER ID   IMAGE                            COMMAND               CREATED         STATUS         PORTS                                        NAMES
9dd566d68478   tektutor/ansible-centos:latest   "/usr/sbin/sshd -D"   4 seconds ago   Up 3 seconds   0.0.0.0:3002->22/tcp, 0.0.0.0:9002->80/tcp   centos002
51b8450f8b60   tektutor/ansible-centos:latest   "/usr/sbin/sshd -D"   5 seconds ago   Up 3 seconds   0.0.0.0:3001->22/tcp, 0.0.0.0:9001->80/tcp   centos001
83ae1cb95fdc   tektutor/ansible-ubuntu:latest   "/usr/sbin/sshd -D"   5 seconds ago   Up 4 seconds   0.0.0.0:2002->22/tcp, 0.0.0.0:8002->80/tcp   ubuntu002
14883f9c8a81   tektutor/ansible-ubuntu:latest   "/usr/sbin/sshd -D"   6 seconds ago   Up 5 seconds   0.0.0.0:2001->22/tcp, 0.0.0.0:8001->80/tcp   ubuntu001
</pre>

### See if ansible ping works
```
sudo su -
cd ~ansible-aug-2021
cd Day2/InstallNginx/v4
ansible all -m ping
```

### Let's try install nginx 
```
sudo su -
cd ~ansible-aug-2021
cd Day2/InstallNginx/v4
ansible-playbook install-nginx-playbook.yml
```

### See if you are able access the web pages from the ansible nodes
```
curl http://localhost:8001
curl http://localhost:8002
curl http://localhost:9001
curl http://localhost:9002
```

### Save collected facts to JSON file
```
sudo su -
cd ~ansible-aug-2021
git pull
cd Day4/FactsCachingToJSON
ansible all -m setup 
```
Now you may investigate the facts folder for the JSON files in the name of the host listed in the inventory file.

### Trying out the facts filter plugin
```
sudo su -
cd ~ansible-aug-2021
git pull
cd Day4/Filters
rm -rf facts
ansible-playbook playbook.yml 
```
You may observe the facts folder with only selective facts are captured as opposed to all facts.

### Linear vs Free Strategy
You can change the strategy to linear in ansible.cfg before running
```
cd ~/ansible-aug-2021
git pull
cd Day4/LinearVsFreeStrategy
ansible-playbook install-nginx-playbook.yml
```
You can record the time the playbook took to complete. Now, you may modify the ansible.cfg strategy to free and rerun the playbook. You may now compare the time difference, generally free stratefy seems to be faster than linear.
