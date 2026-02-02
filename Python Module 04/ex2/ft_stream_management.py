import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

archivist_id = input("Input Stream active. Enter archivist ID: ")
status_report = input("Input Stream active. Enter status report: ")

print(f"[STANDARD] Archive status from {archivist_id}: {status_report}",
      file=sys.stdout)
print("[ALERT] System diagnostic: Communication channels verified",
      file=sys.stderr)
print("[STANDARD] Data transmission complete", file=sys.stdout)

print("Three-channel communication test successful.")
