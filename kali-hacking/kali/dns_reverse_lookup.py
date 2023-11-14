from scapy.all import sr1, IP, UDP, DNS, DNSQR, DNSRR

def reverse_dns_lookup(ip_address):
    # Creating a DNS reverse query
    reverse_ip = '.'.join(reversed(ip_address.split('.'))) + ".in-addr.arpa"
    dns_query = sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1, qd=DNSQR(qname=reverse_ip, qtype='PTR')), verbose=0)

    # Extracting the domain name from the response
    if dns_query and dns_query.haslayer(DNS) and dns_query[DNS].ancount > 0:
        domain_name = dns_query[DNS].an.rdata
        return domain_name
    else:
        return "No domain name found for this IP address."

# Example usage
# ip_address = "8.8.8.8"
ip_address = "95.216.138.14"

domain_name = reverse_dns_lookup(ip_address)
print(f"Domain name for IP address {ip_address}: {domain_name}")
