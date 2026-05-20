def calculate_metrics(issues):

    metrics = {}

    total_events = (
        issues["map_operations"]
        + issues["tcap_aborts"]
        + issues["timeouts"]
        + issues["resource_limitations"]
    )

    # ONLY real telecom failures
    total_errors = sum(
        issues["telecom_errors"].values()
    )

    successful_operations = max(
        0,
        issues["map_operations"] - total_errors
    )

    if issues["map_operations"] > 0:

        success_ratio = (
            successful_operations
            / issues["map_operations"]
        ) * 100

    else:
        success_ratio = 0

    failure_ratio = 100 - success_ratio

    # Telecom health scoring
    health_score = max(
        0,
        100 - (
            issues["tcap_aborts"] * 15
            + issues["timeouts"] * 10
            + total_errors * 5
        )
    )

    metrics["total_events"] = total_events
    metrics["successful_operations"] = successful_operations
    metrics["success_ratio"] = round(success_ratio, 2)
    metrics["failure_ratio"] = round(failure_ratio, 2)
    metrics["health_score"] = round(health_score, 2)

    return metrics