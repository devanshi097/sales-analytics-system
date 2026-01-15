def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues
    Returns: list of raw lines (strings)
    """
    encodings = ['utf-8', 'latin-1', 'cp1252']
    lines = []

    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()
            break
        except UnicodeDecodeError:
            continue

    if not lines:
        raise FileNotFoundError(f"Could not read file: {filename}")

    cleaned_lines = []
    for line in lines[1:]:
        line = line.strip()
        if line:
            cleaned_lines.append(line)

    return cleaned_lines
