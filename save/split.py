from math import ceil

ss = open('btc_xfer_report.csv').read().split('\n')

tenth = int(ceil(len(ss) / 10.0))

new = [ss[i*tenth:(i+1)*tenth] for i in xrange(10)]

for i, n in enumerate(new):
    open('xfer_report_%d.csv' % i, 'w').write('\n'.join(n))
