import pandas as pd
from fpdf import FPDF

def create_pdf_from_csv(df, output_filename="output.pdf"):
    """
    Ham tao file PDF tu DataFrame.
    """
    pdf = FPDF('L')
    pdf.add_page()
    pdf.set_font("Arial", size=8)

    pdf.cell(200, 10, txt="Data from NewMales.csv", ln=True, align='C')

    col_widths = []
    for column in df.columns:
        if column in ["nr", "year", "health", "school", "exper", "age", "union", "ethn", "maried"]:
            col_widths.append(10)
        elif column in ["rownames"]:
            col_widths.append(15)
        elif column in ["residence", "wage", "exper level", "school level", "wage level"]:
            col_widths.append(20)
        else:
            col_widths.append(40)

    for i, column in enumerate(df.columns):
        pdf.cell(col_widths[i], 10, column, 1, 0, 'C')
    pdf.ln()

    for index, row in df.iterrows():
        for i, item in enumerate(row):
            pdf.cell(col_widths[i], 10, str(item), 1, 0, 'C')
        pdf.ln()

    pdf.output(output_filename)
    return output_filename
