import os

import re

def clean_markdown_file(input_file: str, output_file: str):
    """
    Clean Markdown file by:
    - Removing duplicate lines
    - Removing extra blank lines
    - Removing redundant headers (e.g., repeated section titles)

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path for the cleaned Markdown file.
    """
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    # Remove duplicates while maintaining order
    seen = set()
    cleaned_lines = []
    for line in lines:
        # Remove blank lines or lines with only whitespace
        if line.strip() == "":
            continue

        # Remove specific redundant patterns (example: repeated headers)
        if re.match(r"^#+ .*", line) and line in seen:
            continue
        
        if line not in seen:
            cleaned_lines.append(line)
            seen.add(line)

    # Write cleaned content back to file
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.writelines(cleaned_lines)

    print(f"Markdown cleaned and saved as: {output_file}")

# Example usage
clean_markdown_file(input_file="merged_content.md", output_file="cleaned_content.md")

    
def merge_markdown_files(input_folder: str, output_file: str):
    """
    Merge all .md files from a folder into a single file.
    
    Args:
        input_folder (str): Path to the folder containing markdown files.
        output_file (str): Path for the merged markdown file.
    """
    # Get list of .md files in the folder
    md_files = [f for f in os.listdir(input_folder) if f.endswith(".md")]
    
    with open(output_file, "w", encoding="utf-8") as outfile:
        for file in md_files:
            file_path = os.path.join(input_folder, file)
            with open(file_path, "r", encoding="utf-8") as infile:
                content = infile.read()
                
                # Write content and a separator between files
                outfile.write(f"# {file}\n\n")  # Optional: Include filename as a section title
                outfile.write(content)
                outfile.write("\n\n---\n\n")  # Separator between files

    print(f"Markdown files merged into: {output_file}")

# Example usage
merge_markdown_files(input_folder="./Dataset", output_file="./merged_content.md")
clean_markdown_file(input_file="merged_content.md", output_file="cleaned_content.md")

