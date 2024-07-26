import json, os

database = {}


"""

This program parses the data that was scraped by the enumerator
and dumps it into a json database

"""



for file in os.listdir("Passwords/"):
    print(file.replace(" ", ""))
    with open("Passwords/" + file) as f:
        content = f.read().splitlines()

        for line in content:
            try:
                router_info = line.split("|")
                name = router_info[0].replace(" ", "")
                username = router_info[1].replace(" ", "")
                password = router_info[2].replace(" ", "")

                f_name = file.split(".")[0].replace(" ", "")

                database[name.lower()] = {"username" : username, "password" : password}

                print(database)

            except:
                continue

                

        with open(f"Database/{f_name}.json", 'a') as f:
            f.write(json.dumps(database, indent=4)) 
            database.clear()

                

