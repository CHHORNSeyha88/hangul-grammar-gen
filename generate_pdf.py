from fpdf import FPDF
import os
import webbrowser
from grammar_data import grammar_data

# Setup PDF
pdf = FPDF()
pdf.add_page()

# Add Korean font
font_path = os.path.join("fonts", "NotoSansKR-Regular.ttf")
pdf.add_font("NotoSansKR", "", font_path)
pdf.set_font("NotoSansKR", size=12)

# Title
pdf.cell(0, 10, "Korean Grammar Guide", new_x="LMARGIN", new_y="NEXT")

# Content
for grammar, meaning in grammar_data:
    pdf.cell(0, 10, f"{grammar} → {meaning}", new_x="LMARGIN", new_y="NEXT")

# Output
output_path = os.path.join(os.path.dirname(__file__), "Korean_Grammar_Guide.pdf")
if os.path.exists(output_path):
    os.remove(output_path)

pdf.output(output_path)
webbrowser.open(f'file://{output_path}')

print("✅ PDF created and opened:", output_path)
