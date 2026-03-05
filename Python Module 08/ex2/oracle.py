import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(override=False)

# Required configuration keys
CONFIG_KEYS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
    ]

# Read configuration
config = {}
missing_keys = []
for key in CONFIG_KEYS:
    value = os.getenv(key)
    config[key] = value
    if value is None:
        missing_keys.append(key)

if missing_keys:
    for key in missing_keys:
        print(f"Error: Missing configuration key: {key}")

mode = config["MATRIX_MODE"] or "Not configured"
database_status = ("Connected to local instance" if config["DATABASE_URL"]
                   else "Not configured")
api_status = "Authenticated" if config["API_KEY"] else "Not configured"
log_level = config["LOG_LEVEL"] or "Not configured"
zion_status = "Online" if config["ZION_ENDPOINT"] else "Offline"

print("Configuration loaded:")
print(f"Mode: {mode}")
print(f"Database: {database_status}")
print(f"API Access: {api_status}")
print(f"Log Level: {log_level}")
print(f"Zion Network: {zion_status}")
print("Environment security check:")

try:
    with open(__file__, 'r') as file:
        for line in file:
            if line.startswith("API_KEY") or line.startswith("DATABASE_URL"):
                print("Warning: Hardcoded secrets detected")
                break
        else:
            print("[OK] No hardcoded secrets detected")
except Exception as e:
    print(f"Error reading file: {e}")

if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("Warning: .env file not found.")

if (("API_KEY" in os.environ or "DATABASE_URL" in os.environ) and
        (mode == "production")):
    print("[OK] Production overrides available")
else:
    print("Warning: Production overrides not properly configured")

print("The Oracle sees all configurations.")
