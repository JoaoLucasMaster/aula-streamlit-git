import streamlit as st

st.header("Calculadora", divider="gray")

st.write("Digite uma expressão matemática:")
expression = st.text_input("Entre com os valores")

if (expression):
  result = eval(expression)

  st.write("O resultado é:", result)
