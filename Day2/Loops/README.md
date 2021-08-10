### Deleting existing containers
```
docker rm -f $(docker ps -aq)
```

### Installing Ansible Python Docker SDK
```
sudo pip3 install docker-py
```

### Executing playbook that demonstrates list variable
```
cd ~/ansible-aug-2021
git pull
cd Day2/Loops
anisible-playbook list-playbook.yml
```

### Executing playbook that demonstrates with_sequence
```

```

