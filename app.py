from pathlib import Path

import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Isabel_PT.pdf"
profile_pic = current_dir / "assets" / "profile_pic.jpg"


PAGE_TITLE = "Digital CV | Isabel Barbosa "
PAGE_ICON = ":material/import_contacts:"
NAME = st.secrets["var"]["name"]
DESCRIPTION = "Estudante de Desenvolvimento Web"
EMAIL = "barbosa.isabelcristina@gmail.com"
SOCIAL_MEDIA = {
    "Github": "https://github.com/BellsBarbosa",
    "Linkedin": "https://www.linkedin.com/in/isabel-barbosa-programadora/",
}
PROJECTS = {
    "Fandom Store": "https://miniprojetodescomplica01.netlify.app/",
    "Decode": "https://bellsbarbosa.github.io/ChallengeDecodificadorAluraOne/",
    "Portfolio": "https://bellsbarbosa.github.io/bellsbarbosa.github.io./",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered", initial_sidebar_state="collapsed")


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


col1, col2, = st.columns(2, gap="small")
container = st.container(border=False)
with container:
 with col1:
     st.title(NAME)
     st.write(DESCRIPTION)
     st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",)
     st.write("📫", EMAIL)
     st.write('\n')
     for social_media, link in SOCIAL_MEDIA.items():
         st.write(f"[{social_media}]({link})")   


with col2: 
    st.image(profile_pic, width=230, )


container = st.container(border=False)
with container: 
 st.write('\n')
 st.subheader("Qualificações")
 st.write(
    """FORMAÇÃO EM TECNOLOGIA PRETALAB - Janeiro 2023 - Abril 2023
  - ► Desenvolvimento BackEnd: JavaScript, Lógica de
  - ► Programação, Git e Github.
  - ► Desenvolvimento Front End : HTML e CSS;
  - ► Desenvolvimento de SoftSkills.

  FORMAÇÃO EM TECNOLOGIA DESCOMPLICA - Março 2023 - Julho 2023
  - ► Introdução ao Desenvolvimento Web
  - ► Design Thinking, Ux e Metodologias Ágeis
  - ► HTML, CSS e Bootstrap;
  - ► Javascript, ReactJS;
  - ► Técnicas e ferramentas para gestão de projetos.
     """
  )

col1, col2, = st.columns(2, gap="small")
with col1:
  st.write('\n')
  st.subheader("Hard Skills")
  st.write(
    """
    - ► Web Design
    - ► Design Thinking
    - ► Design Responsivo
    """
)
  with col2:
   st.subheader("Soft Skills")
   st.write(
    """
     - ► Comunicação Inclusiva
     - ► Resolução de Problemas
     - ► Proatividade
     """
 )


st.write('\n')
st.subheader("Histórico de Trabalho")
st.write("---")


st.write("🚧", "**Vinculos Empregatícios**")
st.write(
    """
  
  Usces LLC 2018 - 2019
- ► Assistente Administrativa  - 2018/2019
 
Collective Innovation
 - ►TRADUTORA SÊNIOR - 2019/2020
"""
)



st.write('\n')
st.subheader("Projetos")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
