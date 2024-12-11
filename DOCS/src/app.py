import streamlit as st
from services.blob_services import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Upload de Arquivos")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["jpg", "png", "pdf"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url: 
            st.write(f"Arquivo {fileName} enviado com sucesso")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName}")
            
def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem do Arquivo", use_column_width=True)
    st.write("Validação do Arquivo:")
    if credit_card_info and  credit_card_info["card_name"]:
        st.markdown("<h1 style='color: green;'>Cartão Valido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Número do Cartão: {credit_card_info['card_number']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
    else:
        st.markdown("<h1 style='color: red;'>Cartão Invalido</h1>", unsafe_allow_html=True)
        st.write("Não foi possivel identificar o cartão")
        
if __name__ == "__main__":
    configure_interface()