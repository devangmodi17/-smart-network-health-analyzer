import socket
import subprocess
import json
from datetime import datetime 
import statistics
import time

from modules.network_info import network_information
from modules.connectivity import connectivity_test
from modules.performance import performance_analysis
from modules.health_score import calculate_health_score, get_health_status
from modules.network_data import get_network_data
from modules.diagnosis import diagnose_network
from modules.history import save_history, view_history, history_summary
from modules.monitor import continuous_monitoring


print("=" * 55)
print("        SMART NETWORK HEALTH ANALYZER")
print("     Python-Based Network Monitoring System")
print("=" * 55)

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the Smart Network Health Analyzer.")

print("\nWelcome to the Network Health Analyzer!")
print("This system will check your network connectivity,")
print("performance, and overall network health.")
print("\nLet's begin the analysis...\n")


def network_health():
    print("\n--- NETWORK HEALTH ---")
    print("Analyzing network health...")

    latency, packet_loss = get_network_data()

    if latency is None or packet_loss is None:
        print("Unable to collect network data.")
        return

    health_score = calculate_health_score(latency, packet_loss)
    status = get_health_status(health_score)

    print("\nLatency      :", latency, "ms")
    print("Packet Loss  :", packet_loss, "%")
    print("Health Score :", round(health_score), "/100")
    print("Health Status:", status)
    diagnose_network(latency, packet_loss)

   
while True:

    print("\n" + "=" * 55)
    print("                 MAIN MENU")
    print("=" * 55)

    print("1. Check Network Information")
    print("2. Test Connectivity")
    print("3. Analyze Network Performance")
    print("4. Check Network Health")
    print("5. View Network History")
    print("6. history summary")
    print("7. Continuous Monitoring")
    print("0. Exit")

    choice = input("\nEnter your choice (1-7 or 0 to exit): ").strip()

    if choice == "1":
        network_information()

    elif choice == "2":
        connectivity_test()

    elif choice == "3":
        performance_analysis()

    elif choice == "4":
        network_health()

    elif choice == "5":
        view_history()

    elif choice == "6":
        history_summary()

    elif choice == "7" :
        continuous_monitoring()


    elif choice == "0":
        print("\nThank you for using Smart Network Health Analyzer!")
        break

    else:
         print("\nInvalid choice.")
         print("Please enter a number from 0 to 7.")