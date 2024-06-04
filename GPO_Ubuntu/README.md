# Playbook instructions.

## This playbook will root ssh into your Ubuntu Desktop machines, and Fetch all the Users on the system and execute the playbook for each user

## This is to give a GPO-Like experience to your Ubuntu Desktop Environment. a Lot more features will be added.

1. Edit your inventory file to reflect your subnet of your Ubuntu Desktops.
2. Add the root password to the Inventory file as well.
3. Set the Desktop Background location on your Ansible server that you want to use on all Ubuntu Desktops.
4. After Onedrive is installed, you need to run onedrive --synchronize on each machine to login and specify the Return URI (For Companies using Office package)
5. Change the Theme to whatever you want to that is available standard on the Ubuntu Desktop.
6. Added OnlyOffice as default Office Suite as the look and feel is very similar to the Microsoft Office suite.
7. Added a block to popular social media by pointing the DNS entries to 127.0.0.1.

8. You can run the playbook with the following command from your Ansible Server:

    ```bash
    ansible-playbook -i inventory gpo_playbook.yaml
    ```

## What is still to come?

- Automated Printer installs,
- More "Needed" Software installs for a Office environment,
- Monitoring of Ubuntu Desktop systems.
- and much more. Will add as ideas come up.