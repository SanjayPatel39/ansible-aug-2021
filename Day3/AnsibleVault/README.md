### Creating an ansible vault protected file
```
ansible-vault create credentials.yml
```
When prompts for password, type your preferred ansible vault password.

You may add the below details in the credentials.yml
```
ansible_user: root 
ansible_host: 172.16.95.149
ansible_private_key_file: ~/.ssh/id_rsa
```

### Viewing an ansible vault protected file
```
ansible-vault view credentials.yml
```
You need to type your vault password, when prompted.

### Editing an ansible vault protected file
```
ansible-vault edit credentials.yml
```
You need to type your vault password, when prompted.

### You may also encrypt an existing file using ansible vault
```
ansible-vault encrypt credentials.yml
```

### You may decrypt an vault protected file 
```
ansible-vault decrypt credentials.yml
```
view

### Executing the playbook that accesses vault-protected file
```
cd ~/ansible-aug-2021
git pull
cd Day3/AnsibleVault
ansible-playbook access-vault-protected-data-playbook.yml
```
