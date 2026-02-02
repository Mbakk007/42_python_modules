print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print("Initiating secure vault access...")

try:
    with open("classified_data.txt", "r") as vault:
        print("Vault connection established with failsafe protocols")
        print("SECURE EXTRACTION:")
        for line in vault:
            print(f"[CLASSIFIED] {line.strip()}")
except FileNotFoundError:
    print("ERROR: Vault not found.")

with open("new_security_protocols.txt", "w") as vault:
    print("SECURE PRESERVATION:")
    vault.write("[CLASSIFIED] New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived")
print("Vault automatically sealed upon completion")
print("All vault operations completed with maximum security.")
