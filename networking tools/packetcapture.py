import pyshark
from scapy.all import wrpcap
from scapy.all import sniff

# This function will handle each captured packet
def packet_callback(packet):
    print(packet.show())  # Display the packet details

# Start sniffing on all network interfaces
#sniff(prn=packet_callback, store=0)
#sniff(prn=packet_callback, store=0, filter="tcp port 80")

def interfaces():
    interfaces = pyshark.LiveCapture().interfaces
    print("Available interfaces:", interfaces)

def capture_and_save():
    packets = sniff(count=10, filter="tcp port 80")  # Capture 10 packets
    wrpcap("captured_packets.pcap", packets)  # Save to a pcap file

icmp_count = 0
tcp_count = 0
udp_count = 0

def packet_callback(packet):
    global icmp_count, tcp_count, udp_count
    if packet.haslayer("ICMP"):
        icmp_count += 1
    elif packet.haslayer("TCP"):
        tcp_count += 1
    elif packet.haslayer("UDP"):
        udp_count += 1

    print(f"ICMP: {icmp_count}, TCP: {tcp_count}, UDP: {udp_count}")

    sniff(prn=packet_callback, store=0)

#capture_and_save()
#\\Device\\NPF_Loopback  local traffic only 
# Ethernet adapter Ethernet 3:

import scapy.all as scapy
import networkx as nx
import matplotlib.pyplot as plt

# Initialize a graph object
def visual():
    G = nx.Graph()

    # Callback function to process each packet
    def packet_callback(packet):
        # Check if packet has an IP layer
        if packet.haslayer(scapy.IP):
            # Get source and destination IPs
            src_ip = packet[scapy.IP].src
            dst_ip = packet[scapy.IP].dst

            # Add nodes (IPs) to the graph if they don't exist
            if not G.has_node(src_ip):
                G.add_node(src_ip)
            if not G.has_node(dst_ip):
                G.add_node(dst_ip)

            # Add an edge between the source and destination IPs
            if not G.has_edge(src_ip, dst_ip):
                G.add_edge(src_ip, dst_ip, weight=1)
            else:
                G[src_ip][dst_ip]['weight'] += 1

            # Print information about the packet
           # print(f"Packet from {src_ip} to {dst_ip}")

    # Start sniffing for packets (limit to 100 packets in this example)
    scapy.sniff(prn=packet_callback, count=10000, store=0)

    # Visualize the network graph
    plt.figure(figsize=(10, 8))

    # Draw the network graph
    pos = nx.spring_layout(G)  # Layout for positioning nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Show the plot
    plt.title("Network Traffic Visualization")
    plt.show()

visual()