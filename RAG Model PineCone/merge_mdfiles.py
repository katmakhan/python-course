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

def merge_and_clean_markdown_in_batches(input_folder: str, batch_size: int):
    """
    Merge .md files from a folder into batches and clean each batch.
    
    Args:
        input_folder (str): Path to the folder containing markdown files.
        batch_size (int): Number of files to merge per batch (e.g., 5 files per batch).
    """
    # Get list of .md files in the folder
    md_files = [f for f in os.listdir(input_folder) if f.endswith(".md")]
    num_batches = len(md_files) // batch_size + (1 if len(md_files) % batch_size else 0)

    for batch_num in range(num_batches):
        # Determine the files for the current batch
        start_index = batch_num * batch_size
        end_index = start_index + batch_size
        batch_files = md_files[start_index:end_index]

        # Create the output file name for the current batch
        output_file = f"./Processed/merge_{batch_num + 1}.md"
        
        # Merge and clean the current batch
        with open(output_file, "w", encoding="utf-8") as outfile:
            for file in batch_files:
                file_path = os.path.join(input_folder, file)
                with open(file_path, "r", encoding="utf-8") as infile:
                    content = infile.read()

                    # Write content and a separator between files
                    outfile.write(f"# {file}\n\n")  # Optional: Include filename as a section title
                    outfile.write(content)
                    outfile.write("\n\n---\n\n")  # Separator between files

        # Clean the merged batch file
        clean_markdown_file(input_file=output_file, output_file=output_file)

    print("All batches have been merged and cleaned.")

# Example usage: Merge all Markdown files in the folder into batches of 5 files
input_folder = "./Dataset"
batch_size = 5

# Merge and clean markdown files in batches
merge_and_clean_markdown_in_batches(input_folder=input_folder, batch_size=batch_size)
