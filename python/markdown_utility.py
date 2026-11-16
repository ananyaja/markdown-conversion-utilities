import sys
import csv
import io

def csv_to_markdown(csv_text):
    """Takes raw CSV text and converts it into a formatted Markdown table."""
    f = io.StringIO(csv_text.strip())
    reader = csv.reader(f)
    rows = list(reader)
    
    if not rows:
        return "No valid CSV data found."
    
    header = rows[0]
    col_count = len(header)
    
    md_lines = []
    # Header row
    md_lines.append("| " + " | ".join(header) + " |")
    # Separator row
    md_lines.append("| " + " | ".join(["---"] * col_count) + " |")
    
    # Data rows
    for row in rows[1:]:
        while len(row) < col_count:
            row.append("")
        md_lines.append("| " + " | ".join(row[:col_count]) + " |")
        
    return "\n".join(md_lines)

def text_to_markdown(raw_data, chunk_size=3):
    """
    Takes raw multiline text and converts it into a Markdown table.
    Automatically groups lines into rows based on the specified chunk size (e.g., 3, 4, 6, 8 columns).
    """
    lines = [line.strip() for line in raw_data.strip().split("\n") if line.strip() and not line.startswith('|') and ':---' not in line]
    
    if len(lines) < chunk_size:
        return f"Error: Not enough lines provided for a chunk size of {chunk_size}."

    rows = []
    for i in range(0, len(lines) - (chunk_size - 1), chunk_size):
        chunk = [lines[i + j].replace('"', '') for j in range(chunk_size)]
        rows.append(chunk)

    if not rows:
        return "No valid rows could be parsed."

    # Default headers based on common 3-chunk structure or generic numbered columns
    if chunk_size == 3:
        headers = ["Time Block", "Focus Area", "Core Activity & Deliverables"]
    else:
        headers = [f"Column {i+1}" for i in range(chunk_size)]

    md_lines = []
    md_lines.append("| " + " | ".join(headers) + " |")
    md_lines.append("| " + " | ".join(["---"] * chunk_size) + " |")

    for row in rows:
        md_lines.append("| " + " | ".join(row) + " |")

    return "\n".join(md_lines)

if __name__ == "__main__":
    print("=== CSV Conversion Test ===")
    sample_csv = "Name,Age,Role,Department\nAlice,30,Engineer,Core\nBob,25,Designer,UI"
    print(csv_to_markdown(sample_csv))
    
    print("\n=== Text Chunk Conversion Test ===")
    sample_text = """
    07:30 AM – 08:00 AM
    Morning Routine & Chess
    Daily chess tactical analysis to prime the mind.
    09:30 AM – 11:30 AM
    Python Automation & GitHub
    Organize scripts into a clean package structure.
    """
    print(text_to_markdown(sample_text, chunk_size=3))
