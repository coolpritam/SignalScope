def generate_report(issues, metrics):

    print("\n========== SignalScope Analysis Report ==========\n")

    print(f"Total Events             : {metrics['total_events']}")
    print(f"Transaction Count        : {issues['transaction_count']}")
    print(f"MAP Operations Detected  : {issues['map_operations']}")
    print(f"TCAP Aborts Detected     : {issues['tcap_aborts']}")
    print(f"Timeout Events           : {issues['timeouts']}")
    print(f"Resource Limitations     : {issues['resource_limitations']}")

    print("\n========== Operational Metrics ==========\n")

    print(f"Successful Operations    : {metrics['successful_operations']}")
    print(f"Success Ratio            : {metrics['success_ratio']}%")
    print(f"Failure Ratio            : {metrics['failure_ratio']}%")
    print(f"Protocol Health Score    : {metrics['health_score']}%")

    print("\n========== Telecom Error Summary ==========\n")

    if issues["telecom_errors"]:

        for error_name, count in issues["telecom_errors"].items():
            print(f"{error_name} : {count}")

    else:
        print("No telecom errors detected.")

    print("\n========== Informational Events ==========\n")

    if issues["telecom_info_events"]:

        for info_name, count in issues["telecom_info_events"].items():
            print(f"{info_name} : {count}")

    else:
        print("No informational events detected.")

    print("\n========== Unknown Telecom Events ==========\n")

    if issues["unknown_events"]:

        for event_name, count in issues["unknown_events"].items():
            print(f"{event_name} : {count}")

    else:
        print("No unknown telecom events detected.")

    print("\n========== IMSI Summary ==========\n")

    if issues["unique_imsis"]:

        for imsi in issues["unique_imsis"]:
            print(imsi)

    else:
        print("No IMSI values detected.")

    print("\n========== RCA Suggestion ==========\n")

    if issues["tcap_aborts"] > 0:
        print("- Possible stale TCAP transaction context")

    if issues["timeouts"] > 0:
        print("- Investigate timeout thresholds and delayed responses")

    if issues["resource_limitations"] > 0:
        print("- Check SMSC/IPSTG utilization and memory usage")

    if metrics["health_score"] < 80:
        print("- Subscriber flow health degraded")

    print("\n========== Analysis Completed ==========\n")