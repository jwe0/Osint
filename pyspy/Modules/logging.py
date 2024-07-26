from colorama import Fore
from datetime import datetime

def success(message):
    print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.LIGHTBLACK_EX}[{Fore.GREEN}#{Fore.LIGHTBLACK_EX}]{Fore.RESET}\t{message}")

def errror(message):
    print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.LIGHTBLACK_EX}[{Fore.RED}#{Fore.LIGHTBLACK_EX}]{Fore.RESET}\t{message}")

def notify(message):
    print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}#{Fore.LIGHTBLACK_EX}]{Fore.RESET}\t{message}")