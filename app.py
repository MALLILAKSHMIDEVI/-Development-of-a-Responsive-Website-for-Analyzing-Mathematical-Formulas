import streamlit as st
import pytesseract
from PIL import Image
import latex

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, config='--psm 6')
    return text

def convert_to_latex(text):
    # Implement your logic to extract and convert formulas to LaTeX
    # For now, let's assume the text itself is LaTeX code
    return text

def main():
    # Page Configuration
    st.set_page_config(
        page_title="Math Formulas Analyzer",
        page_icon=":pencil2:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Main Title
    st.title("Analyzing Mathematical Formulas")

    # Sidebar
    st.sidebar.header("Settings")

    # File Uploader
    uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "png", "gif", "bmp"])

    if uploaded_file is not None:
        # Main Content Area
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.markdown("---")  # Horizontal line for separation
        st.write("Classifying...")

        # Perform OCR
        extracted_text = perform_ocr(uploaded_file)

        # Convert to LaTeX
        latex_code = convert_to_latex(extracted_text)

        # Display the extracted text
        st.write("Extracted Text:")
        st.info(extracted_text)

        # Display the formulas in LaTeX format
        st.write("Formulas in LaTeX format:")
        st.code(latex_code, language="latex")

        # Display the formulas in HTML canvas using MathJax
        st.write("Formulas in HTML canvas:")
        st.latex(latex_code)

        # Add a download button for the LaTeX code
        st.sidebar.download_button(
            label="Download LaTeX Code",
            data=latex_code,
            file_name="converted_formula.tex",
            key="download_button",
        )

if __name__ == "__main__":
    main()
# app.py
import streamlit as st

def main():
    st.title("Math Formula Analyzer")

    # Your Streamlit app code goes here

if __name__ == "__main__":
    main()
