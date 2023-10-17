import streamlit as st
import re

def valida_cpf(cpf):
    cpf = re.sub('[^0-9]', '', cpf)
    
    if len(cpf) != 11:
        return False
    
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    resto = total % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    
    if int(cpf[9]) != digito1:
        return False
    
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    resto = total % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    
    if int(cpf[10]) != digito2:
        return False
    
    return True

def valida_cnpj(cnpj):
    cnpj = re.sub('[^0-9]', '', cnpj)
    
    if len(cnpj) != 14:
        return False
    
    def calc_digitos(cnpj, peso):
        total = 0
        for i in range(len(cnpj)):
            total += int(cnpj[i]) * peso[i]
        resto = total % 11
        if resto < 2:
            return 0
        else:
            return 11 - resto
    
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    digito1 = calc_digitos(cnpj[:12], peso1)
    digito2 = calc_digitos(cnpj[:13], peso2)
    
    if int(cnpj[12]) != digito1 or int(cnpj[13]) != digito2:
        return False
    
    return True

st.set_page_config(
    page_title="Validador de CPF e CNPJ",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Validador de CPF e CNPJ")
st.write("Insira um CPF ou CNPJ e clique no botão 'Validar'.")

entrada = st.text_input("Insira um CPF ou CNPJ:")

if st.button("Validar"):
    if re.match(r"^\d{11}$", entrada):
        if valida_cpf(entrada):
            st.success("CPF válido! ✔️")
        else:
            st.error("CPF inválido. ❌")
    elif re.match(r"^\d{14}$", entrada):
        if valida_cnpj(entrada):
            st.success("CNPJ válido! ✔️")
        else:
            st.error("CNPJ inválido. ❌")
    else:
        st.warning("Formato inválido. Insira um CPF com 11 dígitos ou um CNPJ com 14 dígitos. ⚠️")