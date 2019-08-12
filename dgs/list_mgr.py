import csv
import requests
from io import StringIO

domains = []
list_of_contacts = {}

def load_list(list_url):
    resp = requests.get(list_url)
    if resp.status_code != 200:
        print(f'Error loading list: {list_url}')
        return
    r = StringIO(resp.content.decode('utf8'))
    reader = csv.reader(r)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        domain = row[0].lower()
        email = row[6].lower()
        if email == '(blank)':
            email = None
        list_of_contacts[domain] = email
        domains.append(domain)