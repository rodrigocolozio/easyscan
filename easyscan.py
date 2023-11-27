### Automated nmap scanning tool
### Gathering information about target 

import os
import subprocess
import cowsay
import time

# boring animation
def welcome_art():
    print('''
 ___________________________________________________________   __
___  ____/__    |_  ___/__  ____/_  ___/_  ____/__    |__  | / /
__  __/  __  /| |____ \__  __/  _____ \_  /    __  /| |_   |/ / 
_  /___  _  ___ |___/ /_  /___  ____/ // /___  _  ___ |  /|  /  
/_____/  /_/  |_/____/ /_____/  /____/ \____/  /_/  |_/_/ |_/   
                                                                                                      
          ''')

### DEF SECTION
def perform_super_stealthy_recon(IP, port):
    print("In super stealth recon mode you must indicate which Ports you want to perform the scan")
    command = f'nmap -D RND:10 -sS -T4 -p{port} --open --reason --script=default {IP} -oN port_scanning.txt'
    subprocess.run(command, shell=True)
    print("Super Stealthy port scanning completed.")

def perform_stealthy_recon(IP):
    command = f'nmap {IP} -sS -T4 --open -oN port_scanning.txt'
    subprocess.run(command, shell=True)
    print("Stealthy port scanning completed.")

def perform_aggressive_recon(IP):
    command = f'nmap {IP} -T4 -A -sC -sV --traceroute -oN port_scanning.txt'
    subprocess.run(command, shell=True)
    print("Aggressive port scanning completed.")

def perform_normal_mode(IP):
    print("Performing normal port scanning -oN port_scanning.txt")
    command = f'nmap {IP} -T3 -sN -v'
    subprocess.run(command, shell=True)
    print("Normal mode port scanning completed.")

def perform_nslookup(domain):
    print(f"Performing nslookup for domain: {domain}")
    command = f'nslookup {domain} >> additional_information.txt'
    subprocess.run(command, shell=True)
    print("Nslookup completed.")


### HELP SECTION
def display_help_menu():
    print("\n======= Help Menu =======")
    print("Welcome to the Scan Automation Tool!")
    print("This tool streamlines and automates the port scanning process.")
    print("Usage:")
    print("  1. Choose the scan type:")
    print("     - Enter '1' for Stealthy scan")
    print("     - Enter '2' for Super Stealthy scan")
    print("     - Enter '3' for Aggressive scan")
    print("     - Enter '4' for Normal mode scan")
    print("     - Enter '5' to Quit")
    print("  2. Follow the prompts to enter target IP, port (if applicable), and additional information.")
    print("  3. Optionally, perform additional information gathering such as nslookup.")
    print("  4. Results are saved to 'port_scanning.txt' and 'additional_information.txt'.")
    print("  5. If you need help, enter '--help' to view this help menu\n\n\n\n")
    time.sleep(2)


### MAIN
def main():
    # header
    welcome_art()
    time.sleep(2)
    cowsay.daemon(                    "WELCOME\nTO\nEASYSCAN")
    print("This script streamlines and automates the port scanning process, providing a more user-friendly experience.")
    print("If you want help with the tool feel free to type '--help' for assistance\n\n")
    print("All the outputs will be saved into files, check for help to understand more.")
    print("\n\nTo Quit the application just type 'quit' or  press number five into Scan Options")

    while True:
        print("\nScan Automation Script\nChoose the scan type:")
        print("1) Stealthy")
        print("2) Super Stealthy")
        print("3) Aggressive")
        print("4) Normal mode")
        print("5) Quit\n")

        choice = input("Enter the number corresponding to your choice: ")
        print(f"You've chosen {choice}.")

        if choice == "5" or choice == "quit".lower():
            print("Exiting.\n\n\nYви́димcя позже\n")
            break  
        elif choice == "--help":
            display_help_menu()
        elif choice in ["1", "2", "3", "4"]:
            IP = input("Enter the target IP or hostname: ")
            if choice == "2":
                port = input("Enter the port number: ")
                perform_super_stealthy_recon(IP, port)
            elif choice == "1":
                perform_stealthy_recon(IP)
            elif choice == "3":
                perform_aggressive_recon(IP)
            elif choice == "4":
                perform_normal_mode(IP)

            additional_action = input("Do you want to perform additional information gathering?\n\n1) yes\n2) no\n").lower()
            if additional_action == '1' or additional_action == "yes":
                domain = input('What is the domain?   ')
                print(f"Starting nslookup.\n{time.sleep(1)}..\n{time.sleep(1)}...\n{time.sleep(1)}....\n{time.sleep(1)}.....")
                perform_nslookup(domain)
            else:
                print("Not performing nslookup.")
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()
