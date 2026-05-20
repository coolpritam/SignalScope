import re
from collections import Counter


# Real telecom failure events
ERROR_EVENTS = {
    "absentSubscriberSM",
    "facilityNotSupported",
    "systemFailure",
    "dataMissing",
    "unexpectedDataValue"
}

# Informational telecom workflow events
INFO_EVENTS = {
    "alertServiceCentre"
}


def detect_issues(log_data):

    issues = {}

    # Detect MAP operations
    map_operations = re.findall(
        r"sendRoutingInfoForSM|mt-forwardSM",
        log_data
    )

    issues["map_operations"] = len(map_operations)

    # Detect TCAP aborts
    tcap_aborts = re.findall(
        r"\bP_ABORT\b|\bABORT\b",
        log_data
    )

    issues["tcap_aborts"] = len(tcap_aborts)

    # Detect timeout events
    timeouts = re.findall(
        r"timeout",
        log_data,
        re.IGNORECASE
    )

    issues["timeouts"] = len(timeouts)

    # Detect resource limitation errors
    resource_limitations = re.findall(
        r"resource limitation|RESOURCE_LIMITATION",
        log_data,
        re.IGNORECASE
    )

    issues["resource_limitations"] = len(
        resource_limitations
    )

    # Extract telecom events dynamically
    telecom_events = re.findall(
        r"localValue:\s*([A-Za-z0-9_-]+)",
        log_data
    )

    # Exclude MAP operation names
    excluded_operations = {
        "sendRoutingInfoForSM",
        "mt-forwardSM"
    }

    filtered_events = [
        event for event in telecom_events
        if event not in excluded_operations
    ]

    # Separate event categories
    error_summary = {}
    info_summary = {}
    unknown_summary = {}

    for event in filtered_events:

        if event in ERROR_EVENTS:

            error_summary[event] = (
                error_summary.get(event, 0) + 1
            )

        elif event in INFO_EVENTS:

            info_summary[event] = (
                info_summary.get(event, 0) + 1
            )

        else:

            unknown_summary[event] = (
                unknown_summary.get(event, 0) + 1
            )

    issues["telecom_errors"] = error_summary
    issues["telecom_info_events"] = info_summary
    issues["unknown_events"] = unknown_summary

    # Extract transaction IDs
    transaction_ids = re.findall(
        r"Transaction Id:\s*([A-Fa-f0-9]+)",
        log_data
    )

    issues["transaction_count"] = len(
        set(transaction_ids)
    )

    # Extract IMSI values
    imsis = re.findall(
        r"IMSI:\s*(\d+)",
        log_data
    )

    issues["unique_imsis"] = list(
        set(imsis)
    )

    return issues