import subprocess

def get_network_data():
    try:
        result = subprocess.run(
            ["ping", "8.8.8.8", "-n", "4"],
            capture_output=True,
            text=True,
            timeout=10
        )

        lines = result.stdout.splitlines()

        latency = None
        packet_loss = None

        for line in lines:

            if "Average" in line:
                average_part = line.split("Average = ")[1]
                latency = int(average_part.replace("ms", ""))

            if "% loss" in line:
                loss_part = line.split("(")[1]
                packet_loss = int(loss_part.split("%")[0])

        return latency, packet_loss

    except subprocess.TimeoutExpired:
        print("\nNetwork test timed out.")
        return None, None

    except FileNotFoundError:
        print("\nPing command could not be found.")
        return None, None

    except Exception:
        print("\nUnable to collect network data.")
        return None, None