#!/usr/bin/env python3
"""
Clean up fragmented text extracted from PDF

The extraction process broke words across lines. This script attempts to:
1. Join broken words back together
2. Identify section headers
3. Create a more readable markdown structure
"""

import re
import sys

def clean_text(input_file, output_file):
    """Clean up fragmented text"""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Join lines and try to reconstruct words
    cleaned_lines = []
    current_line = ""

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            if current_line:
                cleaned_lines.append(current_line)
                current_line = ""
            continue

        # If line is very short (likely fragment), append to current
        if len(line) < 3 and current_line:
            current_line += line
        # If current line ends with incomplete word pattern, append
        elif current_line and not current_line[-1] in '.!?':
            current_line += " " + line if line[0].isupper() else line
        # Otherwise, save current and start new
        else:
            if current_line:
                cleaned_lines.append(current_line)
            current_line = line

    # Don't forget the last line
    if current_line:
        cleaned_lines.append(current_line)

    # Write cleaned text
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in cleaned_lines:
            f.write(line + '\n\n')

    print(f"Cleaned text written to: {output_file}")
    print(f"Original lines: {len(lines)}")
    print(f"Cleaned lines: {len(cleaned_lines)}")

if __name__ == '__main__':
    input_file = "Context/Sola/Docs/sola-docs-raw.txt"
    output_file = "Context/Sola/Docs/sola-docs-cleaned.txt"

    clean_text(input_file, output_file)
