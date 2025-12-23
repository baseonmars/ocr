# PDF OCR

Python script to OCR PDFs using [marker](https://github.com/VikParuchuri/marker) and [Surya](https://github.com/VikParuchuri/surya). Outputs markdown with preserved document structure (headings, lists, tables).

## Features

- Automatically extracts native text from pages that have it
- OCRs scanned/image pages using Surya (state-of-the-art ML OCR)
- GPU acceleration on both Apple Silicon (MPS) and NVIDIA (CUDA)
- Outputs markdown preserving document structure

## Installation

### macOS (Apple Silicon)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows (NVIDIA GPU)

For best performance with NVIDIA GPUs, install PyTorch with CUDA first:

```bash
python -m venv venv
venv\Scripts\activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt
```

**Note:** Make sure you have the latest NVIDIA drivers installed.

## Usage

```bash
python ocr_pdf.py <input.pdf> [output.md]
```

Examples:

```bash
# Output to same directory as PDF (document.pdf -> document.md)
python ocr_pdf.py document.pdf

# Specify output path
python ocr_pdf.py document.pdf output.md
```

## Notes

- First run downloads ~2GB of ML models
- Processing time depends on page count and how many pages need OCR
- Memory usage scales with document complexity
