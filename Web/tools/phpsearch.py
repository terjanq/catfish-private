#!/usr/bin/env python3
import re
import argparse
import grequests

patterns = {
    re.compile(r'([^\/]*\.php\d{0,1})', re.IGNORECASE):
    (r'.\1.swp', r'.\1.swn', r'.\1.swo', r'\1.bak', r'\1.zip', r'.\1.txt',
     r'\1.~', r'\1~', r'\1.bak', r'\1.bak~', r'\1.source', r'\1_source',
     r'\1.old', '\1_old', r'\1.new', r'\1_new', r'.\1.un~', r'\1-', r'\1_'),
    re.compile(r'([^\/]*\.)(php\d{0,1})', re.IGNORECASE):
    (r'\1txt', r'\1bak', r'.\1swp', r'\1swn', r'\1swo', r'\1zip', r'\1~',
     r'\1bak.\2', r'\1rar', r'\1tar.gz', r'\1tar.xz', r'\g<1>7z', r'\1new.\2',
     r'\1new_\2', r'\1~\2')
}

def prepare_urls(urls, patterns=patterns):
    urls_to_scan = []
    for url in urls:
        if not url.endswith('.php'):
            print('[!] Warning: url {} doesnt end with .php'.format(url))
            continue
        for regex in patterns:
            subs = patterns[regex]
            for sub in subs:
                try:
                    urls_to_scan.append(regex.sub(sub, url))
                except:
                    print('[!] Warning: regex {} failed with url {}'.format(
                        sub, url))
    return urls_to_scan


def scan(urls):
    urls_to_scan = prepare_urls(urls)

    req = (grequests.get(url) for url in urls_to_scan)

    for url, res in zip(urls_to_scan, grequests.map(req)):
        if res is not None and res.status_code != 404:
            print('[+] Found({}): {}'.format(res.status_code, url))


def parse_args():
    parser = argparse.ArgumentParser(description='')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', type=str, help='path to file containing urls')
    group.add_argument('--url', type=str, nargs='+', help='urls to be scanned')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    urls = []

    if args.f is not None:
        with open(args.f, 'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                urls.append(line)
    else:
        for url in args.url:
            urls.append(url)

    scan(urls)


if __name__ == '__main__':
    main()