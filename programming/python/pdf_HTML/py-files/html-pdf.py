from pdf2image import convert_from_path
from PIL import Image

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
merged_image_path = 'merged_image.png'
merged_image.save(merged_image_path)

# Step 4: Create an HTML file and embed the image
output_html = "output.html"
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Merged PDF as Image</title>
</head>
<body>
    <h1>Merged PDF Content</h1>
    <img src="{merged_image_path}" alt="Merged PDF Image" style="max-width: 100%; height: auto;">
</body>
</html>
"""

# Write the HTML content to a file
with open(output_html, 'w') as f:
    f.write(html_content)

print(f"HTML file has been created: {output_html}")
