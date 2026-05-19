def generate_report(issues):

    print("\n========== Analysis Report ==========\n")

    print(f"MAP Operations Detected : {issues['map_operations']}")
    print(f"TCAP Aborts Detected    : {issues['tcap_aborts']}")
    print(f"Timeout Events          : {issues['timeouts']}")
    print(f"Resource Limitations    : {issues['resource_limitations']}")

    print("\n========== RCA Suggestion ==========\n")

    if issues["tcap_aborts"] > 0:
        print("- Possible stale TCAP context detected")

    if issues["timeouts"] > 0:
        print("- Investigate transaction timeout thresholds")

    if issues["resource_limitations"] > 0:
        print("- Check SMSC/IPSTG resource utilization")

    print("\n========== Analysis Completed ==========\n")
