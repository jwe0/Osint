import os
from pystyle import *


def Art():
    ascii_art = """


░█▀█░█░█░█▀▀░█▀█░█░█
░█▀▀░░█░░▀▀█░█▀▀░░█░
░▀░░░░▀░░▀▀▀░▀░░░░▀░
    
    """

    print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(ascii_art)))
    print(Center.XCenter("http://127.0.0.1:5000"))

def Clear_Screen():
    os.system("cls") if os.name == "nt" else os.system("clear")

def Set_Title(args=None):
    os.system("title pyspy ^| Developed by /jwe0") if args == None else os.systsem(f"title pyspy ^| Developed by /jwe0 ^| {args}")