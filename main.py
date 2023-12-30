# app.py
import streamlit as st
import sympy as sp

def main():
    st.title("Math Formula Analyzer")

    # User input for mathematical expression
    expression = st.text_input("Enter a mathematical expression:")

    if expression:
        try:
            # Analyze the mathematical expression
            parsed_expr = sp.sympify(expression)
            st.success(f"Successfully parsed the expression: {parsed_expr}")

            # Additional analysis and visualization can be added here
        except sp.SympifyError:
            st.error("Invalid mathematical expression. Please enter a valid expression.")

if __name__ == "__main__":
    main()
