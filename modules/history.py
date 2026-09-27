import json
import statistics
from datetime import datetime

def save_history (latency, packet_loss, health_score, status):
    record = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "latency": latency,
        "packet_loss": packet_loss,
        "health_score": round(health_score),
        "status": status}

    try:
        with open("history.json", "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []

    history.append(record)

    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)

    print("\nNetwork result saved to history.")

def view_history():
    print("\n--- NETWORK HISTORY ---")

    try:
        with open("history.json", "r") as file:
            history = json.load(file)

    except FileNotFoundError:
        print("No network history found.")
        return

    if not history:
        print("No network history available.")
        return

    for record in history:
        print("\nTime         :", record["time"])
        print("Latency      :", record["latency"], "ms")
        print("Packet Loss  :", record["packet_loss"], "%")
        print("Health Score :", record["health_score"], "/100")
        print("Status       :", record["status"])

def history_summary():
    print("\n--- NETWORK HISTORY SUMMARY ---")

    try:
        with open("history.json", "r") as file:
            history = json.load(file)

    except FileNotFoundError:
        print("No network history found.")
        return

    if not history:
        print("No network history available.")
        return

    latencies = [record["latency"] for record in history]
    packet_losses = [record["packet_loss"] for record in history]
    health_scores = [record["health_score"] for record in history]

    print("\nTotal Tests       :", len(history))
    print("Average Latency   :", round(statistics.mean(latencies), 2), "ms")
    print("Average Packet Loss:", round(statistics.mean(packet_losses), 2), "%")
    print("Average Health    :", round(statistics.mean(health_scores), 2), "/100")
    print("Best Health Score :", max(health_scores), "/100")
    print("Worst Health Score:", min(health_scores), "/100")