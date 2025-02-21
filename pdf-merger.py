import gradio as gr
import fitz  # PyMuPDF

def merge_pdfs(files):
    merger = fitz.open()

    for file in files:
        merger.insert_pdf(fitz.open(file.name))  # Merge PDFs

    merged_pdf_path = "/content/merged.pdf"
    merger.save(merged_pdf_path)
    merger.close()

    return merged_pdf_path  # Return merged PDF for download

# Create Gradio UI
gr.Interface(
    fn=merge_pdfs,
    inputs=gr.Files(file_types=[".pdf"], label="Upload PDFs"),  # Use gr.Files instead of gr.File
    outputs=gr.File(label="Download Merged PDF"),
    title="PDF Merger Tool",
    description="Upload multiple PDF files and get a single merged PDF.",
).launch(share=True)
