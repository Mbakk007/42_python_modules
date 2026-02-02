def crisis_handler(file_name):
    print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")

    try:
        with open(file_name, 'r') as f:
            content = f.read()
            print(f"SUCCESS: Archive recovered - ``{content.strip()}``")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: Other Error ({e})")
        print("STATUS: Crisis handled, system stable\n")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler('lost_archive.txt')
    crisis_handler('classified_vault.txt')
    crisis_handler('standard_archive.txt')

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
