### Installing custom facts in all ansible nodes
```
cd ~/ansible-aug-2021
git pull
cd Day3/CustomFacts
ansible-playbook install-facts-playbook.yml
```

#### Retrieving installed facts via ansible adhoc command
```
cd Day3/CustomFacts
ansible all -m setup | grep "IP Address"
```
The expected output is
<pre>
[jegan@tektutor CustomFacts]$ ansible all -m setup | grep "IP Address"
                "IP Address": "172.17.0.2"
                "IP Address": "172.17.0.3"
                "IP Address": "172.17.0.5"
                "IP Address": "172.17.0.4"
</pre>
