import subprocess

def connectivity_test():
    print("\n--- CONNECTIVITY TEST ---")
    print("Testing internet connection...")

    result = subprocess.run (["ping", "8.8.8.8", "-n", "4"],
        capture_output=True,
        text=True)

    if result.returncode == 0:
        print("Internet Connection : CONNECTED")
    else:
        print("Internet Connection : NOT CONNECTED")