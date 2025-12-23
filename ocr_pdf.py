import sys
from pathlib import Path
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict


def ocr_pdf(input_path: str, output_path: str = None):
    """OCR a PDF and save as markdown."""
    input_file = Path(input_path)

    if not input_file.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    if output_path is None:
        output_path = input_file.with_suffix('.md')

    print(f"Loading models...")
    models = create_model_dict()

    print(f"Processing {input_file.name}...")
    converter = PdfConverter(artifact_dict=models)

    rendered = converter(str(input_file))

    Path(output_path).write_text(rendered.markdown, encoding='utf-8')
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocr_pdf.py <input.pdf> [output.md]")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_md = sys.argv[2] if len(sys.argv) > 2 else None
    ocr_pdf(input_pdf, output_md)
