import json, os


"""

This program searches the database given by the parser

"""


art = """
╦═╗╔═╗╦ ╦╔╦╗╔═╗╔═╗╦ ╦╦ ╔╦╗
╠╦╝║ ║║ ║ ║ ╠╣ ╠═╣║ ║║  ║ 
╩╚═╚═╝╚═╝ ╩ ╚  ╩ ╩╚═╝╩═╝╩ 
> A default router password enumerator
> Developed by /jwe0
> Run &help for commands
"""

print(art)


while True:

    name = input("[COMND] > ")


    if name == "&models":
        print()
        for model in config:
            print(f"[MODEL] > {model}")
        print() 

    elif "&search " in name:

        search_data = name.split(" ")
        brand = search_data[1].lower()
        model = search_data[2].lower()



        with open(f"Database/{brand}.json") as f:
            config = json.load(f)

            if f"{brand}.json" in os.listdir("Database"):

                username = config[model]["username"]
                password = config[model]["password"]

                print(f"\n{model}\n----------\nUsername: {username}\nPassword: {password}\n")
            else:
                print("\n[ERROR] > Model not found in database\n")

    elif name == "&help":
        options = """
&search [BRAND] [MODEL]    >     Displays the username and password of the given router model
&models                    >     Display all models in database
&help                      >     Returns this help message 
        """
        print(options)

    else:
        print("\n[ERROR] > Command not found\n")
        