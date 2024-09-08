import tls_client, json
from bs4 import BeautifulSoup

# This is code I recently developed as part of my Osint.Kit project
# I was going to use routfault however the code for it was lackluster
# to say the least so I decided to use my improved skills to code a 
# version in one file.

session = tls_client.Session()
rots = []

def get_links():
    links = []
    api = "https://portforward.com/router-password/"
    r = session.get(api)
    soup = BeautifulSoup(r.text, 'html.parser')
    a = soup.find_all('a', href=True)
    for link in a:
        if "/passwords" in link.get('href'):
            links.append([link.get_text(), link.get('href')])

    return links

def format_array(array):
    ""

def get_passwords(link):

    data = []
    r = session.get("https://portforward.com" + link)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find_all('table', class_="table")
    tr = table[0].find_all('tr')
    for t in tr:
        th = t.find_all('td')
        name = th[0].get_text()
        username = th[1].get_text()
        password = th[2].get_text()
        dump = {
            "brand" : link.split("/")[1],
            "model" : name,
            "protocol" : "(none)",
            "username" : username,
            "password" : password
        }
        data.append(dump)
    return data
    

links = get_links()
for l in links:
    print(f"{str(links.index(l))}/{str(len(links))}: {l[0]}")
    passwords = get_passwords(l[1])
    for p in passwords:
        rots.append(p)
with open("rots.json", "w") as f:
    json.dump(rots, f, indent=4)
