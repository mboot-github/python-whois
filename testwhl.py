import whois

for tld in whois.validTlds():
    hint = whois.getTestHint(tld)
    if hint:
        print(f"# == {hint}")
        d = whois.query(hint, verbose=True)
        for k,v in d.__dict__.items():
            print(f"\t{k}\t{v}")
        print("")
