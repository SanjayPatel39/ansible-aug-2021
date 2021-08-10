### Executing the playbook
```
cd ~/ansible-aug-2021
git pull
cd Day2/InstallNginx
ansible-playbook install-nginx-playbook.yml
```

### Testing
```
curl http://localhost:8001
curl http://localhost:8002
```
