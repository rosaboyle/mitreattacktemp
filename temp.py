import subprocess

markdown_string = "# Heading\n\nThis is some markdown content."

# Write markdown string to a temporary file
with open("temp.md", "w", encoding="utf-8") as f:
    f.write(markdown_string)

# Convert markdown file to PDF
subprocess.run(["mdpdf", "-o", "output.pdf", "temp.md"])