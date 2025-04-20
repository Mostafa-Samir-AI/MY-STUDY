import markdown
from bs4 import BeautifulSoup

# Read the Markdown content
def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


# Convert Markdown to HTML
def markdown_to_html(md_content):
    html_content = markdown.markdown(md_content)
    return html_content

# Add basic CSS for styling
def add_css(html_content):
    css = '''
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            margin: 20px;
            padding: 20px;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #333;
        }
        p {
            margin-bottom: 10px;
        }
        code {
            background-color: #f9f9f9;
            padding: 2px 4px;
            font-family: Consolas, monospace;
            border-radius: 4px;
        }
        pre {
            background-color: #333;
            color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
        }
        blockquote {
            border-left: 4px solid #ccc;
            margin-left: 0;
            padding-left: 10px;
            color: #555;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    '''
    soup = BeautifulSoup(html_content, "html.parser")
    head = soup.new_tag("head")
    style = soup.new_tag("style")
    style.append(css)
    head.append(style)
    soup.html.insert(0, head)
    return str(soup)

# Write the final HTML with CSS to a file
def write_html(html_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Main function to convert markdown to HTML with CSS
def convert_markdown_to_html(input_md_path, output_html_path):
    md_content = read_markdown('input_md_path')
    html_content = markdown_to_html(md_content)
    final_html = add_css(html_content)
    write_html(final_html, output_html_path)
    print(f"Converted {input_md_path} to {output_html_path}")

# Example usage:
input_md = "git and github.md"  # Path to your Markdown file
output_html = 'markdown.html'  # Output HTML file
convert_markdown_to_html(input_md, output_html)
