def detect_issues(log_lines):
    issues = {
        "map_operations": 0,
        "tcap_aborts": 0,
        "timeouts": 0,
        "resource_limitations": 0
    }

    for line in log_lines:

        if "sendRoutingInfoForSM" in line:
            issues["map_operations"] += 1

        if "P_ABORT" in line:
            issues["tcap_aborts"] += 1

        if "timeout" in line.lower():
            issues["timeouts"] += 1

        if "RESOURCE_LIMITATION" in line:
            issues["resource_limitations"] += 1

    return issues
