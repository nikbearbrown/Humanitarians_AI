# Markdown to PDF Converter

Convert your Markdown files into beautifully formatted PDFs using LaTeX and Python! This modular tool handles everything from parsing markdown and executing code blocks to generating LaTeX and compiling to PDF.

---

## Features

- Convert Markdown to LaTeX
- Execute code blocks and include output
- Generate clean, professional PDFs
- Modular design for easy extension and maintenance

---

## Project Structure
```
markdown-to-pdf/
├── assets/                # Optional assets (images, etc.)
├── markdown-to-pdf/
│ ├── code_handlers.py     # Executes and processes code blocks
│ ├── file_utils.py        # File I/O operations
│ ├── formatting_utils.py  # Utility functions for formatting
│ ├── latex_converter.py   # Converts markdown to LaTeX
│ ├── latex_generators.py  # Generates LaTeX-specific content
│ ├── main.py              # Entry point and CLI logic
│ ├── pdf_generator.py     # Compiles LaTeX to PDF
├── output/                # Output PDFs are saved here
├── pyproject.toml         # Poetry config
├── poetry.lock            # Poetry dependency lock file
└── README.md              # You’re reading it!
```

---

## Usage

### 1. Install dependencies

```bash
poetry install
```

### 2. Run the converter
```bash
poetry run python markdown-to-pdf/main.py path/to/input.md
```
This will:
- Parse your Markdown
- Convert it to LaTeX
- Execute code blocks and embed results
- Generate a PDF in the `output/` folder

---

## Prerequisites

- Python 3.8+
- LaTeX (installed on your system: e.g., `pdflatex`)
- Poetry

### Install TeX Distribution
- **macOS (via Homebrew)**:
`brew install mactex`
- **Windows**:
Download and install MiKTeX: [Installation Guide](https://miktex.org/howto/install-miktex)

---

## How the Project Works
This tool converts a Markdown (.md) file into a PDF by internally translating it into LaTeX and then compiling it. Here’s a breakdown of what happens behind the scenes:

### 1. Entry Point (`main.py`)
- This is the starting script.
- It accepts a Markdown file path as input (e.g., via CLI).
- Calls functions from other modules to:
  - Read the file.
  - Process its contents.
  - Generate and compile the final PDF.

### 2. Reading the Markdown File (`file_utils.py`)
- Responsible for:
  - Reading Markdown content from the file.
  - Saving intermediate or final LaTeX and PDF outputs.

### 3. Converting Markdown to LaTeX (`latex_converter.py`)
- This module takes the parsed Markdown content and transforms it into LaTeX format.
- It handles:
  - Headings (`#`, `##`) → `\section{}`, `\subsection{}`
  - Paragraphs → LaTeX paragraphs
  - Lists → `\begin{itemize}` or `\begin{enumerate}` blocks
  - Images, links, bold/italic → Proper LaTeX formatting

### 4. Handling Code Blocks (`code_handlers.py`)
- Extracts code blocks (e.g., Python, JavaScript) from the Markdown.
- Executes them (if enabled) and captures:
  - Console output
  - Errors (optional)
-Both the code and its output are rendered in the final PDF using LaTeX syntax (e.g., `\begin{verbatim}`).

### 5. Generating Final LaTeX Document (`latex_generators.py`)
- Combines:
  - LaTeX headers and packages
  - Converted content from `latex_converter.py`
  - Code + output from `code_handlers.py`
  - Creates a complete `.tex` file ready for compilation.

### 6. Formatting Utilities (`formatting_utils.py`)
- Contains helper functions to:
- Escape LaTeX special characters (e.g., `#`, `%`)
- Clean whitespace, fix encoding issues
- Apply consistent styles

### 7. Compiling LaTeX to PDF (`pdf_generator.py`)
- Uses a LaTeX compiler like `pdflatex` or `xelatex` to:
- Compile the `.tex` file.
- Save the resulting `.pdf` to the `/output` folder.
- Also handles:
  - Compilation errors
  - Cleanup of intermediate files

### 8. Optional: `assets/` Folder
- You can store images, LaTeX templates, or logos here.
- These assets can be referenced from within Markdown and embedded into the PDF.
