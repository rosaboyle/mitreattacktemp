from md2pdfconvert import convert_to_pdf 
with open("final_report.md", "r") as f:
    huge_markdown = f.read()
convert_to_pdf(huge_markdown, "final_report.pdf", "Profiling Report")