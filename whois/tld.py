from . import tld_regexpr

TLD_RE = {}
def get_tld_re(tld):
	if tld in TLD_RE: return TLD_RE[tld]
	v = getattr(tld_regexpr, tld)
	extend = v.get('extend')
	if extend:
		e = get_tld_re(extend)
		TLD_RE[tld] = e.copy()
		TLD_RE[tld].update(v)

	else:
		TLD_RE[tld] = v

	if 'extend' in TLD_RE[tld]: del TLD_RE[tld]['extend']


[get_tld_re(tld) for tld in dir(tld_regexpr) if tld[0] != '_']