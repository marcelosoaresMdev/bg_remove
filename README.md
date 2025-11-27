# 🖼️ Remoção de Fundo com Streamlit

Este projeto é uma aplicação web desenvolvida em **Python** utilizando **Streamlit** e a biblioteca **[WithoutBG](https://pypi.org/project/withoutbg/)** para remover o fundo de imagens de forma simples e prática.  

## 🚀 Funcionalidades
- Upload de imagens nos formatos **JPEG** e **PNG**  
- Remoção automática de fundo utilizando modelos da Hugging Face  
- Visualização da imagem original e da versão sem fundo  
- Download da imagem final em **PNG com transparência**  

## 🛠️ Tecnologias Utilizadas
- [Python 3.9+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [WithoutBG](https://github.com/PrithivirajDamodaran/WithoutBG)  
- [Pillow (PIL)](https://pillow.readthedocs.io/)  

## 📦 Instalação

Clone este repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/bg_remove.git
cd bg_remove
pip install streamlit withoutbg pillow
streamlit run bg_remove.py
http://localhost:8501


## ⚠️ Observações
Na primeira execução, a biblioteca WithoutBG baixa modelos do Hugging Face, o que pode levar alguns segundos.

O resultado é gerado em PNG com transparência, ideal para uso em design, e-commerce e criação de conteúdo.

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.


