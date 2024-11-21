from scapy.all import *
import time

# List of blacklisted domains
BLACKLIST = [
    "doubleclick.net",
    "adservice.google.com",
    "ads.yahoo.com"
]

# Function to check if a packet matches a blacklisted domain
def is_blacklisted(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):  # Check for TCP and payload
        payload = packet[Raw].load.decode(errors='ignore')  # Decode the raw data
        for domain in BLACKLIST:
            if domain in payload:
                return True
    return False

# Callback function for sniffing packets
def block_ads(packet):
    if is_blacklisted(packet):
        print(f"Blocked ad request to: {packet[IP].dst}")

# Start sniffing packets with a timeout
print("Ad blocker running...")
sniff(filter="tcp port 80", prn=block_ads, store=0, timeout=60)  # Stops after 60 seconds
print("Sniffer stopped after timeout.")



#curl http://doubleclick.net
#wget http://adservice.google.com

