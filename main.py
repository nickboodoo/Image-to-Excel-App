import pytesseract
from PIL import Image
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def ocr_receipt(image_path):
    """Extract text from a receipt image using OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def parse_receipt_text(text):
    """Parse the extracted text into items and costs."""
    lines = text.split('\n')
    items = []
    
    for line in lines:
        if line.strip():  # Ignore empty lines
            parts = line.split()
            if len(parts) > 1 and parts[-1].replace('.', '', 1).isdigit():
                item = ' '.join(parts[:-1])
                cost = float(parts[-1])
                items.append((item, cost))
    
    return items

def save_to_excel(items, file_path):
    """Save the parsed items and costs to an Excel file."""
    df = pd.DataFrame(items, columns=['Item', 'Cost'])
    df.to_excel(file_path, index=False)

def main():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user to select an image file
    image_path = filedialog.askopenfilename(
        title="Select the receipt image file",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    )

    if not image_path:
        print("No image selected. Exiting.")
        return

    # Perform OCR on the selected image
    text = ocr_receipt(image_path)

    # Parse the OCR text into items and costs
    items = parse_receipt_text(text)

    if not items:
        print("No items found in the receipt. Exiting.")
        return

    # Prompt the user to save the parsed data to an Excel file
    output_file_path = filedialog.asksaveasfilename(
        title="Save the Excel file",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )

    if not output_file_path:
        print("No file selected for saving. Exiting.")
        return

    # Save the items to the Excel file
    save_to_excel(items, output_file_path)
    print(f"Receipt data saved to {output_file_path}")

if __name__ == "__main__":
    main()
