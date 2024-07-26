# Routfault

```
╦═╗╔═╗╦ ╦╔╦╗╔═╗╔═╗╦ ╦╦ ╔╦╗
╠╦╝║ ║║ ║ ║ ╠╣ ╠═╣║ ║║  ║
╩╚═╚═╝╚═╝ ╩ ╚  ╩ ╩╚═╝╩═╝╩
> A default router password enumerator
> Developed by /jwe0
> Run &help for commands
```

Routfault is a program that can scrape default password for routers from `https://portforward.com/router-password/` it then compiles all of these password to a directory called `/Passwords` this directory is then used by the parser I wrote to form a json database that can then be used by the client to search for default router credentials in a nice simple cli interface.

# Install
1. Run the command `git clone https://github.com/jwe0/routfault`
2. Run `pip install -r requirements.txt` to install nescessary modules
3. The database is already compiled and parsed for your convenience
4. Run `cd Finder` to go to the folder of the client
5. Run `python client.py` to open the client
6. Type &help for help commands


# Setup
1. Run the `main.py` to scrape router names and grab the passwords.
2. The `main.py` will output the `passwords` folder put this in the parser folder and run the `json_parse.py` to form a database folder with all the credentaisl in.
3. Put the `Database` folder in the `Finder` directory and run the `client.py` to open the cli.




# Directory format explained

## /Enumerator
This folder contains the `main.py` script responsible for scraping and parsing the base data needed by the program.

## /Extra
Contains the pre compiled wordlist of default passwords.

## /Finder
This contains the `client.py` script which is a cli that parses the database formed by `/Parser`.

## /Parser
This takes the folder `/Passwords` that was formed by the `main.py` and turns it into a `database.json` that the `client.py` in `/Finder` uses.





# Regards
I take no legal responsibility for any negative actions committed with my software. This was made for ethical purposes only <3.
