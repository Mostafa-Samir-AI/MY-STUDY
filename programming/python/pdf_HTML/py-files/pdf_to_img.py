from pdf2image import convert_from_path
from PIL import Image
from reportlab.pdfgen import canvas

# Step 1: Convert PDF pages to images
pdf_path = 'git and github.pdf'  # Your input PDF file
images = convert_from_path(pdf_path)

# Step 2: Combine the images vertically
widths, heights = zip(*(i.size for i in images))
total_height = sum(heights)
max_width = max(widths)

# Create a blank image with the combined height of all pages
merged_image = Image.new('RGB', (max_width, total_height))

y_offset = 0
for img in images:
    merged_image.paste(img, (0, y_offset))
    y_offset += img.size[1]

# Step 3: Save the merged image
merged_image.save('merged_image.png')

# Step 4: Convert the image back into a PDF
output_pdf = "output.pdf"
c = canvas.Canvas(output_pdf)
c.drawImage('merged_image.png', 0, 0, width=max_width, height=total_height)
c.showPage()
c.save()

print(f"PDF has been converted into one merged page: {output_pdf}")
