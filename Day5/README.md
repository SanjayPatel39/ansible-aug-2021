### Download Jenkins Build Server
```
sudo su -
wget https://get.jenkins.io/war-stable/2.289.3/jenkins.war
```

### Install JDK 1.8
```
sudo su -
yum install -y java-11-openjdk-devel
```

### Verify if JRE is in path
```
java -version
```

### Launching jenkins (You won't be able to use this terminal)
```
sudo su -
java -jar ./jenkins.war
```
