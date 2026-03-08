import socket
import datetime

print("\nSubdomain Enumeration Tool\n")

target= input("Enter the target domain: ").strip().lower()
wordlist_path = input("Enter the wordlist path: ").strip()

total = 0
found = 0

#Get the start time to measure how long enumeration takes
start_time = datetime.datetime.now()

print("\n[*]Starting enumeration...\n")

try:
    with open(wordlist_path, "r") as f:
        for line in f:
            prefix = line.strip()
            subdomain = f"{prefix}.{target}"
            total += 1

            try:
                ip = socket.gethostbyname(subdomain)
                print(f"[found]{subdomain} -> {ip}")
                found += 1
            except socket.gaierror:
                pass
except FileNotFoundError:
    print("[!] Wordlist file not found.")

end_time = datetime.datetime.now()

print("\n[*]Enumeration completed.")
print(f"[*]Subdomains tested : {total}")
print(f"[*]Subdomains found : {found}")
print(f"[*]Time taken : {end_time - start_time}")