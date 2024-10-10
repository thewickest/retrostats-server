# Creating a test database in the Raspberry PI
sudo apt update
sudo apt upgrade

sudo apt install mariadb-server

# answer yes to every query
sudo mysql_secure_installation 

sudo mysql -u root -p

CREATE DATABASE retrostats;

CREATE USER 'retrostats'@'localhost' IDENTIFIED BY 'retrostats';
CREATE USER 'retrostats'@'%' IDENTIFIED BY 'retrostats';

GRANT ALL PRIVILEGES ON retrostats.* TO 'retrostats'@'localhost';
GRANT ALL PRIVILEGES ON retrostats.* TO 'retrostats'@'%';

FLUSH PRIVILEGES;

# Enable Mysql ports to be connected outside localhost

sudo nano /etc/mysql/mariadb.conf.d/50-server-cnf

# Change the bind-address line to 0.0.0.0. This will allow to receive external connections
# Restart the service
sudo service mysql restart

# This is and insecure practice meant just for development processes. Instead of 0.0.0.0 you should be allowing the host's IP address