FILENAME = "new_discovery.txt"

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
print(f"Initializing new storage unit: {FILENAME}")

try:
    file = open(FILENAME, "w")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")

    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")

    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{FILENAME}' ready for long-term preservation.")

except Exception as e:
    print("ERROR: Could not create storage unit.", e)
