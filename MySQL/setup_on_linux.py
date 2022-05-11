# Get a linux server - Ubuntu
# sudo apt-get install mysql-server

# Default is Localhost
# Change into Remote:
# sudo mysql_secure_installation utility
# y y y y y
# sudo ufw enable
# sudo ufw allow mysql

# SERVER BINDING
# cd to /etc/mysql/mysql.conf.
# nano mysqld.cnf
# under bind-address = 127.0.0.1
# change it into bind-address = 0.0.0.0
# save and exit
# sudo systemctl start mysql
# sudo systemctl enable mysql
# sudo systemctl restart mysql

# mysql.conf -u root -p
# pw
# CREATE DATABASE test;

'''
-> Query OK
GRAND ALL ON test.* TO leo@"my-ip-addrEss" IDENTIFIED BY "PWD";
'''

import mysql.connector
from datetime import date
import datetime

db = mysql.connector.connect(
      host = "server ip addr",
      user = "leo",
      passwd = "PWD"
)

mycursor = db.cursor()
mycursor.execute("SHOW DATABASES")
print(mycursor.fetchone())
