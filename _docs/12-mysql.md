# mysql CLI



```  C:\Apps\mysql57\my.ini
[mysqld]
# set basedir to your installation path
basedir=C:/Apps/mysql57
# set datadir to the location of your data directory
datadir=C:/Apps/mysql57/data
```


``` mysql-init.txt
ALTER USER 'root'@'localhost' IDENTIFIED BY 'Pass1234';
```

SERVER
.\bin\mysqld.exe --initialize
.\bin\mysqld.exe --init-file=C:/Apps/mysql57/mysql-init.txt --console
.\bin\mysqld.exe --console

CLIENT
.\bin\mysql.exe -u root -p


CREATE DATABASE zhixian$default;
CREATE DATABASE zhixian$forum;
