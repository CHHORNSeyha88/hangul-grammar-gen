from generate_pdf import create_korean_grammar_pdf
from data import grammar_data

if __name__ == "__main__":
    create_korean_grammar_pdf(grammar_data)
    print("[OK] Korean Grammar Guide PDF generated successfully!")
