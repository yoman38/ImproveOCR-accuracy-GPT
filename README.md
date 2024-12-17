# ImproveOCR-accuracy-GPT

This repository contains a Python script that utilizes OpenAI's API to clean and improve OCR-extracted text. The script processes a given text file in chunks and sends each chunk to the GPT model, requesting corrections of OCR errors, removal of nonsensical fragments, and preservation of the text structure (like titles, numbering, and layout). The output is a cleaned version of the text saved to a new file.

## Features

- **Chunk-Based Processing:**  
  The script processes the input file in manageable chunks (default size: 4000 characters) to avoid exceeding token limits.

- **Automated OCR Correction:**  
  It leverages OpenAI's GPT-3.5-turbo model to correct text inconsistencies, remove gibberish, and maintain the overall formatting and structure.

- **Minimal Invention:**  
  The instructions to the model explicitly specify not to invent new text, ensuring fidelity to the original content.

- **Flexible Configuration:**  
  You can easily change the input file path, output file path, and chunk size according to your needs.

## Prerequisites

- **Python 3.7+**
- **OpenAI Python Library:**  
  Install via `pip install openai`

- **OpenAI API Key:**  
  You must have an OpenAI API key with access to the GPT-3.5-turbo model.  
  Set your API key as an environment variable `OPENAI_API_KEY`, or directly within the script (not recommended for security reasons).

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ImproveOCR-accuracy-GPT.git
   cd ImproveOCR-accuracy-GPT
