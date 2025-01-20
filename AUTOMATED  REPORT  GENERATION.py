import pandas as pd
from fpdf import FPDF

# Reading data from File
df = pd.read_csv('C:\\Users\\Aniket\\Desktop\\code tech it solutions pvt lt\\Task 2\\dataset.csv')

# Analyzing data
sample_data = df.head()
meta_data = df.describe().round(2)  # Rounding values to 2 decimal places

# Creating an object from FPDF class to create pdf
pdf = FPDF()

# Adding a page
pdf.add_page()

# Setting font
pdf.set_font('Courier', 'BU', 20)

# Writing the title
pdf.cell(200, 10, 'Dataset Report', align='C')
pdf.ln(20)

pdf.set_font('Courier', 'B', 20)

# Format 
# Width and Height is set as frame/box and inside that we right things
# pdf.cell(<width>, <height>, <string>, <alignment>)

pdf.cell(30, 10,"Dataset:'Phone usage in INDIA' ", align='L')

# Move to next line
pdf.ln(15)

pdf.set_font('Arial', 'B', 16)
# Writing the title
pdf.cell(200, 12, 'Dataset Sample :', ln=True, align='L')


# Writing Sample Data Table with Borders
pdf.set_font('Arial', 'B', 10)
# Writing column headers
for col in sample_data.columns:
    pdf.cell(30, 10, col, border=1, align='C')
pdf.ln()

pdf.set_font('Arial', '', 10)
# Writing sample data rows
for index, row in sample_data.iterrows():
    for col in sample_data.columns:
        pdf.cell(30, 10, str(row[col]), border=1, align='C')
    pdf.ln()

# Move to next line
pdf.ln(10)



pdf.set_font('Arial', 'B', 16)

# Writing the title
pdf.cell(200, 12, 'Dataset Analysis :', ln=True, align='L')

# Writing Meta Data Table with Borders
pdf.set_font('Arial', 'B', 10)
# Writing the index column header as empty since it will be used for row names (count, mean, etc.)
pdf.cell(30, 10, '', border=1, align='C')  # Empty cell for row names (index)

# Writing column headers for describe data
for col in meta_data.columns:
    pdf.cell(30, 10, col, border=1, align='C')
pdf.ln()

pdf.set_font('Arial', '', 10)

# Writing meta data rows
for index, row in meta_data.iterrows():
    # Writing the index value (row name) in the first column
    pdf.cell(30, 10, str(index), border=1, align='C')
    for value in row:
        pdf.cell(30, 10, str(value), border=1, align='C')
    pdf.ln()

pdf.cell(30, 10,"Where :", align='L')
pdf.ln()

pdf.cell(30, 10,"ST  - Screen Time (Hrs/Day)", align='L')
pdf.ln()

pdf.cell(30, 10,"DU  - Data Usage (GB/Month)", align='L')
pdf.ln()

pdf.cell(30, 10,"MRC - Monthly Recharge Cost (INR)", align='L')


# Saving the PDF
pdf.output('Report.pdf', 'F')