
# Image to Excel App

This application extracts text from an image of a receipt using Optical Character Recognition (OCR) and saves the extracted information into an Excel file. The program is particularly useful for converting receipt images into structured Excel data, which can be further processed or analyzed.

## Features

- **OCR with Tesseract:** Converts receipt images into text using the Tesseract OCR engine.
- **Excel Output:** Saves the extracted items and costs into an Excel file.
- **GUI for File Selection:** Uses file dialogs to allow users to select the input image and output Excel file locations.

## Project Structure

- **`main.py`**: The main script that handles the entire process, including OCR, parsing, and saving to Excel.
- **`requirements.txt`**: A list of Python dependencies required to run the project.

## Requirements

- Python 3.x
- Tesseract OCR installed on your system (with `tesseract` in your `PATH`)
- Python libraries:
  - `pytesseract`
  - `Pillow`
  - `pandas`
  - `tkinter` (usually comes pre-installed with Python)

## Installation

### 1. Install Python Dependencies

You can install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

Or install them individually:

```bash
pip install pytesseract pillow pandas
```

### 2. Install Tesseract OCR

#### **Windows:**

1. Download the Tesseract installer from [this link](https://github.com/UB-Mannheim/tesseract/wiki).
2. Run the installer and follow the installation instructions.
3. Ensure the installation path (e.g., `C:\Program Files\Tesseract-OCR\`) is added to your system's `PATH` environment variable.

#### **macOS:**

If you have Homebrew installed, run:

```bash
brew install tesseract
```

#### **Linux:**

Use your package manager to install Tesseract. For example, on Ubuntu:

```bash
sudo apt-get install tesseract-ocr
```

## How to Run

1. **Run the Script:**

   Execute the `main.py` script. A file dialog will appear, allowing you to select the receipt image file.

```bash
python main.py
```

2. **Select the Image File:**

   Choose the image file of the receipt that you want to convert to Excel.

3. **Process the Receipt:**

   The application will use OCR to extract text from the image and parse it into items and costs.

4. **Save the Excel File:**

   After processing, another file dialog will prompt you to choose where to save the Excel file.

5. **Review the Excel File:**

   Open the resulting Excel file to see the extracted items and costs organized in a spreadsheet.

## Example

### Input:

An image of a receipt with items and their costs.

### Output:

An Excel file with two columns: `Item` and `Cost`.

| Item               | Cost |
|--------------------|------|
| AKS Water 4-Pack   | 3.99 |
| Thai Jasmine Rice  | 18.99|
| KS Dog Food        | 34.99|

## Troubleshooting

### Tesseract Not Found

If you encounter an error indicating that Tesseract is not found, ensure that Tesseract is correctly installed and added to your system's `PATH`. You can verify the installation by running:

```bash
tesseract --version
```

If Tesseract is not in your `PATH`, you can specify the path in your Python script:

```python
import pytesseract

# Set the tesseract_cmd to the path of your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## License

This project is licensed under the MIT License.
