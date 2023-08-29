import whois

domain = "google.com"
d = whois.query(domain, verbose=True)
print(d.__dict__)
