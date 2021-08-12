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

### Clone the TekTutor github repo for all the source code
```
git clone http://github.com/tektutor/ansible-aug-2021.git
```
