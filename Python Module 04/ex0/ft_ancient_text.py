FILENAME = "ancient_fragment.txt"

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print(f"Accessing Storage Vault: {FILENAME}")

try:
    file = open(FILENAME, "r")
    print("Connection established...")
    print("RECOVERED DATA:")
    content = file.read()
    print(content)
    file.close()
    print("Data recovery complete. Storage unit disconnected.")

except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
