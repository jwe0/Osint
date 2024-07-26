from requests_html import HTMLSession
from bs4 import BeautifulSoup
import os


"""

This script scrapes all the models from https://portforward.com/router-password/
It then dumps them into txt files in the /Passwords directory sorted by the router model
The script then proceeds to format the databsae into more readable text split by |
The script then compiles all passwords into one big default router password wordlist

The passwords in /Passwords are used by the parser to get the json database needed for
the client

"""



def scrape_links():
    print("[DEBUG] > (STARTED URL SCRAPE)")
    session = HTMLSession()
    urls = ""
    data = session.get("https://portforward.com/router-password/")

    for link in data.html.absolute_links:
        if "/passwords" in link:
            urls += f"{link}\n"


    with open("models.txt", 'w') as f:
        f.write(urls)

    print("[DEBUG] > (SCRAPED URLS)")


def scrape_models():
    session = HTMLSession()
    print("[DEBUG] > (STARTED SCRAPING DATA)")

    with open("models.txt") as f:


        for line in f.read().splitlines():
            data = session.get(line)

            soup = BeautifulSoup(data.text, 'html.parser')

            tr_elements = soup.find_all("tr")

            name = line.split("https://portforward.com/")[1].split("passwords/")[0].replace("/", "main.py")
            print("[DEBUG] > (SCRAPED DATA FOR {})".format(name))

            for tr in tr_elements:
                td = tr.find_all("td")


                
                with open(f"Passwords/{name}.txt", 'a') as f:
                    f.write(f"{str(td)}\n")
            print("[DEBUG] > (WROTE HTML DATA FOR {})".format(name))


def parse_files():
    print("[DEBUG] > (STARTED PARSING DATA)")
    for file in os.listdir("Passwords/"):
        passwords = ""
        with open("Passwords/" + file) as f:
            lines = f.read().splitlines()

            for line in lines:
                data = line.split(",")
                try:
                    name = data[0].replace("<strong>", "").replace("</strong>", "").replace("<td>", "").replace("</td>", "").replace("[", "")
                    username = data[1].replace("<td>", "").replace("</td>", "")
                    password = data[2].replace("<td>", "").replace("</td>", "").replace("]", "")

                except:
                    continue

                #print(name, username, password)

                passwords += f"{name} | {username} | {password}\n"
            print("[DEBUG] > (PARSED DATA FOR {})".format(file))

        with open(f"Passwords/{file}", 'w') as f:
            print("[DEBUG] > (WROTE CRED DATA FOR {})".format(file))
            f.write(passwords)
            passwords = ""
    

def only_passwords():
    print("[DEBUG] > (MAKING WORDLIST)")
    for file in os.listdir("Passwords/"):
        passwords = []
        with open("Passwords/" + file) as f:
            lines = f.read().splitlines()
            for line in lines:

                x = line.split('|')[2].replace(' ', '')

                with open("WORDLIST.txt", 'a') as f:
                    if x not in passwords:
                        if "router" not in x:
                            f.write(f"{x}\n")
                            passwords.append(x)
    print("[DEBUG] > (WORDLIST CREATED)")



if __name__ == "__main__":
    print("\n[STARTED SCRAPING URLS FROM TARGET]\n")
    scrape_links()
    print("\n[STARTED SCRAPING MODEL DATA]\n")
    scrape_models()
    print("\n[STARTED PARSING DATA]\n")
    parse_files()
    print("\n[STARTED FORMING WORDLIST]\n")
    only_passwords()