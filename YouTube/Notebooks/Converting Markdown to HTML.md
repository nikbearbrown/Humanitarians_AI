
# Converting Markdown to HTML

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Repository Setup](#repository-setup)
    1. [Step1 Cloning the Repository](#step1-cloning-the-repository)
    2. [Step2 Navigating to the Folder](#step2-navigating-to-the-folder)
    3. [Step3 Creating a Python Script](#step3-creating-a-python-script)
4. [The Conversion Script](#the-conversion-script)
5. [Script Highlights](#script-highlights)
6. [Running the Script](#running-the-script)
7. [Conclusion](#conclusion)

## Introduction
Markdown is a lightweight markup language that allows users to format text with plain syntax. It’s widely used in documentation, blogs, and content creation. However, Markdown files often need to be converted into formats like HTML or EPUB for broader accessibility and presentation. In this chapter, we’ll explore how to convert Markdown files into HTML and package them as an EPUB file for publishing. Using the INFO-7375-Branding-and-AI GitHub repository as an example, we’ll break down the process step by step.

## Prerequisites
To follow along, you'll need:
- **Python**: [Download Python](https://www.python.org)
- **Markdown library**: Install using:

```bash
pip install markdown
```

## Repository Setup

### Step1 Cloning the Repository
Clone the repository:

```bash
git clone https://github.com/nikbearbrown/INFO-7375-Branding-and-AI.git
```

![image](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/1_pngfZIx0GYqyzaY_ce.png)


### Step2 Navigating to the Folder
Navigate to the respective folder:

```bash
cd INFO-7375-Branding-and-AI/Appendix
```

### Step3 Creating a Python Script
Create a `.py` file and copy the script provided in the next section into this file, or place the Python script in this directory.

The directory structire should be as below:

![image](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/Direct2UMR2WtGPDOM_ce.png)

## The Conversion Script
Here's the Python script that handles the conversion process:

```python
import os
import re
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension

# Configure GitHub repository details
GITHUB_USER = "nikbearbrown"
GITHUB_REPO = "INFO-7375-Branding-and-AI"
GITHUB_BRANCH = "main"

# CSS for styling
css_content = """
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 20px;
}

h1, h2, h3, h4, h5, h6 {
    color: #0056b3;
    margin-top: 1em;
}

code {
    background-color: #f4f4f4;
    padding: 4px;
    border-radius: 4px;
    font-family: monospace;
    color: #272822;
}

pre {
    background: #f4f4f4;
    color: #272822;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
    white-space: pre-wrap;
    font-family: monospace;
}

a {
    color: #0056b3;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto;
    object-fit: contain;
}

img[src$=".svg"] {
    background-color: white;
    padding: 10px;
}

img:not([src]), img[src=""] {
    min-width: 100px;
    min-height: 100px;
    background: #f0f0f0;
    border: 1px dashed #999;
}
"""

def fix_github_image_links(md_content):
    """
    Converts GitHub image links (including blob links) to raw content URLs
    """
    def replace_github_link(match):
        image_path = match.group(1)
        
        # Debug: Log the original image path
        print(f"Original image path: {image_path}")
        
        # Transform GitHub blob URLs to raw URLs
        if "github.com" in image_path and "/blob/" in image_path:
            raw_url = image_path.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            print(f"Transformed GitHub blob URL to: {raw_url}")
            return f"![]({raw_url})"
        
        # Skip if already a raw URL
        if image_path.startswith(("http://", "https://")):
            print(f"Skipping already full URL: {image_path}")
            return match.group(0)
        
        # Handle relative paths
        if image_path.startswith("./"):
            image_path = image_path[2:]
        
        # Transform relative paths to raw GitHub URLs
        clean_path = image_path.lstrip("/")
        raw_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{clean_path}"
        print(f"Transformed relative path to: {raw_url}")
        return f"![]({raw_url})"

    # Match all Markdown image links
    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    return image_pattern.sub(replace_github_link, md_content)

def convert_md_to_html(md_content, css_filename="styles.css"):
    """
    Convert markdown content to HTML with proper styling and image handling
    """
    # Fix image links
    md_content = fix_github_image_links(md_content)
    
    # Convert to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=[
            CodeHiliteExtension(linenums=False),
            'fenced_code',
            TocExtension(permalink=True),
            'md_in_html'
        ],
    )
    
    # Create HTML document with error handling
    html_with_css = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{css_filename}">
    <script>
        window.addEventListener('load', function() {{
            document.querySelectorAll('img').forEach(function(img) {{
                img.onerror = function() {{
                    console.error('Failed to load image:', this.src);
                    this.style.border = '1px solid red';
                    this.style.padding = '10px';
                    this.alt = 'Failed to load image: ' + this.src;
                }};
            }});
        }});
    </script>
</head>
<body>
{html_content}
</body>
</html>
"""
    return html_with_css

def process_markdown_files():
    """
    Process all markdown files in the current directory and subdirectories
    """
    css_filename = "styles.css"

    # Save the CSS file
    with open(css_filename, "w", encoding="utf-8") as css_file:
        css_file.write(css_content)
    print(f"CSS saved to {css_filename}")

    # Process markdown files
    for root, _, files in os.walk("."):
        for filename in files:
            if filename.endswith(".md"):
                md_filepath = os.path.join(root, filename)
                try:
                    with open(md_filepath, "r", encoding="utf-8") as md_file:
                        md_content = md_file.read()
                    
                    html_content = convert_md_to_html(md_content, css_filename)
                    html_filename = f"{os.path.splitext(md_filepath)[0]}.html"
                    
                    with open(html_filename, "w", encoding="utf-8") as html_file:
                        html_file.write(html_content)
                    
                    print(f"Converted {md_filepath} to {html_filename}")
                except Exception as e:
                    print(f"Error processing {md_filepath}: {str(e)}")

if __name__ == "__main__":
    process_markdown_files()

```

Save this script as `convert_md_to_html.py` in the `Appendix` directory.

## Script Highlights
1. **Image Handling**: Converts GitHub image links into raw URLs using regex and proper repository paths.
2. **HTML Structure**: Wraps content in a responsive HTML structure with custom CSS.
3. **Recursive Processing**: Processes all Markdown files, including those in nested directories.

## Running the Script
Execute the script in the terminal:

```bash
python convert_md_to_html.py
```

![image](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/md_to_eqKBoKPbBQPN_ce.png)

### Output
- HTML files are generated in the same folders as the original Markdown files.

Below Image is reference for the HTML files created in the same directory.

![image](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/html_f1lyWEIbd7kU6_ce.png)

- Verify that images, TOC, and code blocks are rendered correctly.

## Conclusion
In this chapter, we explored how to efficiently convert Markdown files into HTML using Python. By leveraging libraries like `markdown` and incorporating features such as a Table of Contents, GitHub image handling, and CSS styling, we ensured that the converted HTML files are both functional and visually appealing. The provided script automates the process, making it easy to handle multiple Markdown files, even within nested directories.
This workflow is especially useful for preparing documentation, technical blogs, or eBooks for broader accessibility. With the converted HTML files, you can now move forward to package them into an EPUB or other formats, enhancing their usability across different platforms.
