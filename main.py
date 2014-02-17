#!/usr/bin/env python3
import os
import csv
import threading
from queue import Queue
import itertools

from craigsgenerator import Section, fulltext

from dates import is_date_range, dates, month

proxy_schemes = {'http','https'}
if len(proxy_schemes.intersection(os.environ.keys())) > 0:
    proxies = {s:os.environ[s] for s in proxy_schemes if s in os.environ}
else:
    try:
        from config import proxies
    except ImportError:
        proxies = None


def sink(queue, fn = '/tmp/sublets.csv'):
    fieldnames = [
        'subdomain','section',
        'title', 'date', 'price',
        'longitude', 'latitude',
        'url', 'body',
    ]
    with open(fn, 'w') as fp:
        w = csv.DictWriter(fp, fieldnames)
        w.writeheader()

    for i in itertools.count(1):
        listing = queue.get()
        with open(fn, 'a') as fp:
            w = csv.DictWriter(fp, fieldnames)
            w.writerow(listing)

        if i % 100 == 0:
            print('Written %d records' % i, end = '\r')

def main():
    queue = Queue()
    threading.Thread(target = sink, args = (queue,)).start()
    for subdomain in ['austin','newyork','sfbay','philadelphia','chicago','washingtondc','portland','seattle','boston']:
        for sectionslug in ['roo','sub','hsw','swp','vac','prk','off','rea']:
#   for subdomain in ['austin']:
#       for sectionslug in ['roo']:
            t = threading.Thread(target = search_section, args = (subdomain, sectionslug, queue))
            t.start()

def search_section(subdomain, sectionslug, queue):
    for listing in Section(subdomain, sectionslug, proxies = proxies, scheme = 'https'):
        # Make this parallel?
        try:
            body = fulltext(listing)
        except KeyError:
            body = ''
        listing['body'] = body

        listing['subdomain'] = subdomain
        listing['section'] = sectionslug
        listing['url'] = listing['href']

        del(listing['href'])
        del(listing['listing'])
        queue.put(listing)

if __name__ == '__main__':
    print(proxies)
    aoeu
    main()