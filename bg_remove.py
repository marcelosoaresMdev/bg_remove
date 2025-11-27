import streamlit as st
from withoutbg import WithoutBG
from PIL import Image
import io
import base64

# --- Configuração da Página ---
st.set_page_config(
    page_title="Remoção de Fundo com Streamlit",
    layout="centered"
)

st.title("Remova o fundo de imagens!")
st.caption("_______________________________")
st.markdown("Faça o upload de uma imagem para remover o fundo usando a biblioteca `WithoutBG`.")
st.caption("Atenção: A biblioteca WithoutBG baixa modelos do Hugging Face na primeira execução, o que pode levar alguns segundos.")

@st.cache_resource
def load_model():
    """Carrega e armazena em cache o modelo WithoutBG."""
    try:
        model = WithoutBG.opensource()
        return model
    except Exception as e:
        st.error(f"Erro ao carregar o modelo WithoutBG: {e}")
        return None

model = load_model()

if model is None:
    st.stop() # Para a execução se o modelo não puder ser carregado

# --- Uploader de Arquivo ---
uploaded_file = st.file_uploader(
    "Escolha uma imagem (JPEG ou PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # 1. Carregar a Imagem Original
    # O Streamlit fornece o arquivo como um objeto que pode ser lido pela PIL
    original_image = Image.open(uploaded_file)
    
    st.subheader("Imagem Original")
    st.image(original_image, caption="Sua imagem original.")
    
    # 2. Processar a Imagem (Remover Fundo)
    if st.button("✨ Remover Fundo"):
        with st.spinner("Removendo fundo... por favor, aguarde."):
            try:
                # O remove_background pode aceitar um objeto PIL Image diretamente, mas
                # para maior compatibilidade com a versão mostrada, é melhor salvar
                # temporariamente em um buffer ou usar o método de passagem de bytes
                
                # Para simplificar, vamos passar o buffer de bytes do arquivo carregado:
                image_bytes = uploaded_file.getvalue()
                
                # A função remove_background aceita o caminho do arquivo, bytes, ou um objeto PIL Image
                # Se usarmos o objeto PIL Image carregado:
                result_pil_image = model.remove_background(original_image)
                
                st.subheader("Imagem Sem Fundo")
                st.image(result_pil_image, caption="Imagem com fundo removido.")

                # 3. Gerar Opção de Download
                # Converter a imagem PIL resultante para bytes PNG para download
                buf = io.BytesIO()
                # Salva a imagem PIL (que já está em RGBA para ter transparência) no buffer
                result_pil_image.save(buf, format="PNG")
                png_bytes = buf.getvalue()

                # Cria o botão de download
                st.download_button(
                    label="📥 Baixar Imagem Sem Fundo (PNG)",
                    data=png_bytes,
                    file_name="imagem_sem_fundo.png",
                    mime="image/png"
                )
                
            except Exception as e:
                st.error(f"Ocorreu um erro durante a remoção do fundo: {e}")


