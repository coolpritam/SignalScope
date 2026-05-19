def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return []

    except Exception as error:
        print(f"[ERROR] {error}")
        return []
