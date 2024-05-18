import subprocess

def convert_to_pdf(huge_markdown, filename, title="Attack Matrix Report"):

    # Write markdown string to a temporary file
    with open("temp.md", "w", encoding="utf-8") as f:
        f.write(huge_markdown)

    # Convert markdown file to PDF
    subprocess.run(["mdpdf", "-o", filename, "temp.md"])