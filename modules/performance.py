import subprocess
from modules.network_data import get_network_data

def performance_analysis():
    print("\n--- NETWORK PERFORMANCE ---")
    print("Measuring network performance...")

    latency, packet_loss = get_network_data()

    print("\nLatency    :", latency, "ms")
    print("Packet Loss:", packet_loss, "%")

    if latency is not None:
        if latency < 50:
            rating = "Excellent"
        elif latency < 100:
            rating = "Good"
        elif latency < 200:
            rating = "Fair"
        else:
            rating = "Poor"

        print("Performance :", rating)
    print("\n--- NETWORK PERFORMANCE ---")
    print("Measuring network performance...")

    result = subprocess.run(
        ["ping", "8.8.8.8", "-n", "4"],
        capture_output=True,
        text=True
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

    print("\nLatency    :", latency, "ms")
    print("Packet Loss:", packet_loss, "%")
    if latency is not None:
        if latency < 50:
            rating = "Excellent"
        elif latency < 100:
            rating = "Good"
        elif latency < 200:
            rating = "Fair"
        else:
            rating = "Poor"

        print("Performance :", rating)