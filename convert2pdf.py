from markdown_pdf import MarkdownPdf, Section

# Create a PDF with a Table of Contents (TOC) from headings up to level 2
def convert_to_pdf(huge_markdown, filename, title="Attack Matrix Report"):
    pdf = MarkdownPdf(toc_level=1)
    # Add sections to the PDF
    # pdf.add_section(Section("# Title\n", toc=False))
    # pdf.add_section(Section("# Head1\n\n![python](img/python.png)\n\nbody\n"))
    pdf.add_section(Section(huge_markdown, paper_size="A4-L"))

    # Set PDF metadata
    pdf.meta["title"] = title
    pdf.meta["author"] = "Dheeraj Mohandas Pai"

    # Save the PDF to a file
    pdf.save(filename)