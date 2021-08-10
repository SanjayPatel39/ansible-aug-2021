### Installing Ansible Python Docker SDK
```
sudo pip3 install docker-py
```

### Executing playbook that demonstrates list variable
```
cd ~/ansible-aug-2021
git pull
cd Day2/Loops
ansible-playbook list-playbook.yml
```

### Executing playbook that demonstrates with_sequence
```
cd ~/ansible-aug-2021
cd Day2/Loops
ansible-playbook sequence-playbook.yml
```

### Deleting existing containers
```
docker rm -f $(docker ps -aq)
```

### Provisioning Docker containers via Ansible playbook
```
cd ~/ansible-aug-2021
cd Day2/Loops
ansible-playbook provision-containers-playbook.yml
```
