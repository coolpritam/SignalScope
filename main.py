from analyzer.parser import read_log_file
from analyzer.detector import detect_issues
from analyzer.report import generate_report


def main():
    log_path = "logs/sample_log.txt"

    print("\n========== Telecom Log Analyzer ==========\n")

    log_data = read_log_file(log_path)

    detected_issues = detect_issues(log_data)

    generate_report(detected_issues)


if __name__ == "__main__":
    main()
