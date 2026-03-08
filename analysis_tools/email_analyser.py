header_file = "email_headers.txt"
fields = {
    "From": None,
    "Reply-To": None,
    "To": None,
    "Subject": None,
    "Date": None,
    "Received": None,
    "X-Originating-IP": None,
    "Authentication-Results": None
}
try:
    with open(header_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        
        if ":" in line:
            field, value = line.split(":", 1)
            field = field.strip()
            value = value.strip()

            if field in fields:

                #store first received ine only
                if field == "Received":
                    if fields[field] is None:
                        fields[field] = value
                else:
                    fields[field] = value
except FileNotFoundError:
    print(f"[!] {header_file} not found.")
    exit()

print("==== EMAIL HEADER ANALYSIS REPORT ===")

print("\nFrom :", fields["From"])
print("\nReply-To :", fields["Reply-To"])
print("\nTo :", fields["To"])
print("\nSubject :", fields["Subject"])
print("\nDate :", fields["Date"])
print("\nReceived (first hop):", fields["Received"])
print("\nX-Originating-IP :", fields["X-Originating-IP"])
print("\nAuthentication-Results:", fields["Authentication-Results"])

print("\n----- PHISHING INDICATORS -----")

# Check Reply-To mismatch
if fields["From"] and fields["Reply-To"] and fields["From"] != fields["Reply-To"]:
    print("[!] WARNING: Reply-To differs from From address.")
    print(f"From: {fields['From']}")
    print(f"Reply-To: {fields['Reply-To']}")
    print("This is a common phishing tactic to redirect replies to the attacker.\n")

# Check SPF/DKIM failures
auth = fields["Authentication-Results"]
if auth and ("fail" in auth.lower()):
    print("[!] WARNING: Authentication failure detected (SPF/DKIM/DMARC).")
    print("This email may have been spoofed or sent from an unauthorised server.")

print("=========================================")

