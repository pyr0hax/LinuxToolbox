# LinuxToolbox

# Pyroscan: A Simple Port Scanner Written in Python

Pyroscan is a user-friendly port scanning tool coded in Python. Its usage is simple: just enter the target host and port using the command `-H` for the host and `-p` for the port.

### Usage:

    pyroscan.py -H <target_host> -p <target_port>
    
### Troubleshooting:
If you are running Linux and the script won't execute, please use the following command:

    sudo chmod +x ./pyroscan.py

Note that you will need to enter your Sudo password if you are not root.

Stay secure and enjoy using Pyroscan for all your port scanning needs!

# NginxProxySetup: NginxProxySetup is a tool that can assist you in building basic configurations for reverse proxy and securing your site with Certbot.

Please note that you need to have port 80 and 443 open to your NGINX server for this tool to work.

To run the script, follow these steps:

+ Download the script to your NGINX server.
+ Make the script executable by running the following command:

        sudo chmod +x ./nginxproxysetup.sh

This command ensures that the script can be executed.
Once the script is set to be executed, run the follwing command:

    ./nginxproxysetup.sh

This should now prompt you for information like your proxy address as well as the address the proxy server should serve the content to as example:

    (e.g., example.com): " proxy_address
    (e.g., http://localhost:8000): " target_address

You can also modify the target_address to work with application as well as example:

    http://localhost:8000/application

Please make sure to modify the email address in the script to whom it should notify when certificate is expiring.

# Pyroname: a Rename tool to overwrite, but commenting out the old info when catting info from one file to the other.

SED rename when catting to an existing file it comments out the old code so that there can be no confusion

# NetplanApply: a simple shell script to automate the IP config changes to a NETPLAN config file.

## Usage

1. Make the script executable by running:

    ```bash
    sudo chmod +x setipubuntu.sh
    ```

2. Execute the script:

    ```bash
    sudo sh ./setipubuntu.sh
    ```

3. You will be prompted to choose between DHCP and static IP configuration. 

    - If you choose static, follow the prompts to set your IP address, gateway, and DNS servers.

4. After configuring the network settings, the script will display available netplan configurations. 

5. Choose the correct configuration file. 

6. Netplan will be configured with your new network settings.

# GPO_Ubuntu: Create a Windows GPO Like experience using Ansible for Linux (Ubuntu only now).

## Usage

1. Run the Ansible playbook from your Ansible server using:

    ansible-playbook -i inventory gpo_playbook.yaml