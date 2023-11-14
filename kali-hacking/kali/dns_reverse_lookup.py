import dns.reversename

# name = dns.reversename.from_address("45.55.99.72")
name = dns.reversename.from_address("95.216.138.14")
print(name)
print(dns.reversename.to_address(name))
