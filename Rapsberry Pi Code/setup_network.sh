
# Mettre à jour et installer les paquets nécessaires
sudo apt-get update
sudo apt-get install -y hostapd dnsmasq iptables-persistent netfilter-persistent gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-rtsp

# Configurer hostapd
sudo bash -c 'cat <<EOF > /etc/hostapd/hostapd.conf
interface=wlan0
driver=nl80211
ssid=RaspberryPiAP
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=raspberry
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
EOF'

sudo sed -i 's|#DAEMON_CONF=""|DAEMON_CONF="/etc/hostapd/hostapd.conf"|' /etc/default/hostapd

# Configurer dnsmasq
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo bash -c 'cat <<EOF > /etc/dnsmasq.conf
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
EOF'

# Configurer le réseau
sudo bash -c 'cat <<EOF >> /etc/dhcpcd.conf
interface wlan0
static ip_address=192.168.4.1/24
denyinterfaces eth0
denyinterfaces wlan0
EOF'

# Activer le routage IP et configurer iptables
sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo netfilter-persistent save

# Redémarrer les services pour appliquer les configurations
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo systemctl restart dnsmasq

echo "Wi-Fi access point configured and started."
