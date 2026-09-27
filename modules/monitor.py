import time
from datetime import datetime

from modules.network_data import get_network_data
from modules.health_score import calculate_health_score, get_health_status
from modules.history import save_history


def continuous_monitoring():
    print("\n--- CONTINUOUS NETWORK MONITORING ---")
    print("Network monitoring started.")
    print("The network will be checked every 5 seconds.")
    print("Press Ctrl+C to stop monitoring.\n")

    try:
        while True:
            latency, packet_loss = get_network_data()

            if latency is None or packet_loss is None:
                print("Unable to collect network data.")
            else:
                  health_score = calculate_health_score(latency, packet_loss)
                  status = get_health_status(health_score)
                  
                  print("Time:", datetime.now().strftime("%H:%M:%S"),
                        "| Latency:", latency, "ms",
                        "| Loss:", packet_loss, "%",
                        "| Health:", round(health_score),
                        "|", status)
                  
                  save_history(latency,
                               packet_loss,
                               health_score,
                               status )

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
