#Author: Jaco van Zyl
#Email: jvanzyl5@outlook.com
#!/bin/bash

level1=$(printf "    ") # 4 spaces
level2=$(printf "        ") # 8 spaces
level3=$(printf "            ") # 12 spaces

read -p "Do you want to use DHCP or Static IP? (dhcp/static): " ip_type

config=""

if [[ "$ip_type" == "dhcp" ]]; then
    config="${level3}dhcp4: true"
elif [[ "$ip_type" == "static" ]]; then
    read -p "Enter IP address and subnet mask (e.g., 10.208.72.9/24): " ip_subnet
    read -p "Enter gateway address (e.g., 10.208.72.1): " gateway
    read -p "Enter DNS servers (comma-separated): " dns_servers

    config=$(cat <<EOF
${level3}dhcp4: false
${level3}addresses:
${level3}  - $ip_subnet
${level3}routes:
${level3}  - to: 0.0.0.0/0
${level3}    via: $gateway
${level3}nameservers:
${level3}  addresses: [$dns_servers]
EOF
    )
else
    echo "Invalid option. Please choose either dhcp or static."
    exit 1
fi

echo "Available netplan configurations:"
ls /etc/netplan/*.yaml 2>/dev/null || echo "No netplan configurations found."

read -p "Enter the name of the configuration file you want to edit (e.g., 01-netcfg.yaml): " config_file
config_path="/etc/netplan/$config_file"

if [ -f "$config_path" ]; then
    echo "Editing $config_path"
else
    echo "Error: Configuration file not found."
    exit 1
fi

cat <<EOF | sudo tee "$config_path"
network:
  version: 2
  ethernets:
    eth0:
$config
EOF

sudo netplan apply
