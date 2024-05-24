#!/bin/bash
#Author Jaco van Zyl

ssh username@server.example.com 'mysqldump -u your_username -p"your_password" database | pv -W > /path/to/database_backup.sql'
scp username@server.example.com:/path/to/database_backup.sql /path/to/local/directory | pv -W > /dev/null
ssh username@server.example.com 'rm /path/to/database_backup.sql'

# Use the following command to start editing the crontab and use the line below to setup the path to the script
# crontab -e
# 0 1 * * * /path/to/backup_script.sh
