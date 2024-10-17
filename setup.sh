#!/bin/bash
apt update
apt upgrade

apt install mariadb-server

green() {
  echo -e '\e[32m'$1'\e[m';
}

readonly EXPECTED_ARGS=3
readonly E_BADARGS=65
readonly MYSQL=`which mysql`

# Construct the MySQL query
readonly Q1="CREATE DATABASE IF NOT EXISTS $1;"
readonly Q2="CREATE USER IF NOT EXISTS '$2'@'localhost' IDENTIFIED BY '$3';"
readonly Q3="CREATE USER IF NOT EXISTS '$2'@'%' IDENTIFIED BY '$3';"
readonly Q4="GRANT ALL ON $1.* TO '$2'@'localhost' IDENTIFIED BY '$3';"
readonly Q5="GRANT ALL ON $1.* TO '$2'@'%' IDENTIFIED BY '$3';"
readonly Q6="FLUSH PRIVILEGES;"
readonly Q7="CREATE TABLE IF NOT EXISTS $1.sessions (id INT AUTO_INCREMENT, initDate DATE, duration INT, score INT, gameId INT, gameName VARCHAR(255), gameEmulator VARCHAR(255), gamePath VARCHAR(255), userId INT, state VARCHAR(255), PRIMARY KEY(id));"
readonly SQL="${Q1}${Q2}${Q3}${Q4}${Q5}${Q6}${Q7}"

# Do some parameter checking and bail if bad
if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: $0 dbname dbuser dbpass"
  exit $E_BADARGS
fi

# Run the actual command
$MYSQL -u root -p -e "$SQL"

# Let the user know the database was created
green "Database $1 and user $2 created with a password you chose"
green "Restarting Mysql Service"

service mysql restart