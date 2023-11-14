import dns.resolver
 
hosts = ["python.org", "google.com", "microsoft.com", "temida.si"]

for host in hosts:
    print(host)
    ip = dns.resolver.resolve(host, "A")
    for i in ip:
        print(i)
