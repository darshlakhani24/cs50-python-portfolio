from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", align="C", ln=True)

def main():
    name = input("Name: ").strip()
    make_shirtificate(name)

def make_shirtificate(name):
    pdf = PDF()
    pdf.add_page()

    pdf.set_auto_page_break(auto=True, margin=15)

    # Add shirt image
    pdf.image("shirtificate.png", x=20, y=60, w=170)

    # Add name over the shirt
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)  # white text

    # Position the name around the middle of the image
    pdf.set_y(135)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
