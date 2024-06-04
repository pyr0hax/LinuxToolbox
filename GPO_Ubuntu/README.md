# Playbook instructions.

## This playbook will root ssh into your Ubuntu Desktop machines, Go to /etc/passwd, look at user 1001 and then become that user to execute all the tasks. So preferred using Desktop Environments that has only one additional user. 

## This is to give a GPO-Like experience to your Ubuntu Desktop Environment. a Lot more features will be added.

1. Edit your inventory file to reflect your subnet of your Ubuntu Desktops.
2. Set the Desktop Background location on your Ansible server that you want to use on all Ubuntu Desktops.
3. After Onedrive is installed, you need to run onedrive --synchronize on each machine to login and specify the Return URI (For Companies using Office package)
4. Change the Theme to whatever you want to that is available standard on the Ubuntu Desktop.
5. Added OnlyOffice as default Office Suite as the look and feel is very similar to the Microsoft Office suite.

## What is still to come?

- Automated Printer installs,
- More "Needed" Software installs for a Office environment,
- Monitoring of Ubuntu Desktop systems.
- and much more. Will add as ideas come up.