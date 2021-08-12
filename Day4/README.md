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

### Building ansible node docker images
```
sudo su -
pip3 install docker-py
cd ansible-aug-2021/Day2
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
