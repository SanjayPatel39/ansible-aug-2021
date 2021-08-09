### Installing Git
```
su -
yum install git
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
  ansible python module location = /usr/lib/python3.6/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 3.6.8 (default, Aug 24 2020, 17:57:11) [GCC 8.3.1 20191121 (Red Hat 8.3.1-5)]
[jegan@localhost Ansible]$ 
</pre>

### Installing Docker Community Edition
```
su -
yum install -y yum-utils

yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

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

You may check if you are able to execute docker commands as regular user
```
docker --version
docker images
```

#### Troubleshooting permission denied issue
```
su -
usermod -aG docker rps
sudo su rps
docker images
```
