#!/bin/bash

# Stopper les services pour configurer
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq

# Configurer /etc/dhcpcd.conf pour une IP statique
sudo bash -c 'cat >> /etc/dhcpcd.conf <<EOF
interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant
EOF'

# Redémarrer le service dhcpcd
sudo service dhcpcd restart

# Configurer /etc/hostapd/hostapd.conf
sudo bash -c 'cat > /etc/hostapd/hostapd.conf <<EOF
interface=wlan0
driver=nl80211
ssid=RaspberryPi_AP
hw_mode=g
channel=6
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=your_password_here
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
EOF'

# Pointer hostapd vers son fichier de configuration
sudo sed -i 's|#DAEMON_CONF=""|DAEMON_CONF="/etc/hostapd/hostapd.conf"|' /etc/default/hostapd

# Configurer /etc/dnsmasq.conf
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo bash -c 'cat > /etc/dnsmasq.conf <<EOF
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
EOF'

# Redémarrer et activer les services
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo systemctl restart dnsmasq

# Activer le forwarding IPv4
sudo bash -c 'cat >> /etc/sysctl.conf <<EOF net.ipv4.ip_forward=1 EOF'
sudo sysctl -p

# Configurer le NAT entre wlan0 et eth0
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo bash -c 'iptables-save > /etc/iptables/rules.v4'

# Instructions de fin
echo "Configuration terminée. Le Raspberry Pi est maintenant un point d'accès Wi-Fi."
