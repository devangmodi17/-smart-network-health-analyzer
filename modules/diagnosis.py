def diagnose_network(latency, packet_loss):

    print("\n--- DIAGNOSIS ---")

    if packet_loss > 5:
        print("Issue: High packet loss detected.")
        print("Possible Cause: Unstable connection or network congestion.")
        print("Recommendation: Check the network connection and reduce network load.")

    elif latency > 200:
        print("Issue: High network latency detected.")
        print("Possible Cause: Slow network response or network congestion.")
        print("Recommendation: Check the connection and network usage.")

    elif packet_loss > 2:
        print("Issue: Some packet loss detected.")
        print("Possible Cause: Temporary network instability.")
        print("Recommendation: Monitor the connection for further changes.")

    else:
        print("No major network issues detected.")
        print("Recommendation: Network performance is currently normal.")