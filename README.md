# 🇰🇷 Korean Grammar Guide PDF Generator

This Python script generates a multi-page, cleanly formatted **Korean Grammar Guide PDF** using the [fpdf2](https://py-pdf.github.io/fpdf2/) library and Korean-friendly fonts.

📦 Features
- Supports full Korean character rendering
- Automatically opens the PDF after generating
- Built with Unicode-safe fonts to avoid "missing glyphs" (e.g. seeing `??` or `□`)
- 50+ grammar points (editable)
- Auto PDF generation and open
- Unicode-safe with `NotoSansKR` font

### 📌 Requirements
- Python 3.8+
- `fpdf2` (PDF generation)
- `NotoSansKR-Regular.ttf` (Unicode Korean font)

### 🔤 Why NotoSansKR?
Using a Unicode font like `NotoSansKR` is essential to prevent:
- `??` or blank boxes in your PDF (caused by **missing glyphs**)
- Improper rendering of Korean characters
- Encoding errors during PDF export

## 🛠️ How to Use

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the script:
    ```bash
    python generate_pdf.py
    ```

3. Your `Korean_Grammar_Guide.pdf` will open and be saved in the same folder.

## 📝 Customize
Add/remove grammar items in [`grammar_data.py`](grammar_data.py).

## 📄 License
MIT — free for personal and educational use.

---
