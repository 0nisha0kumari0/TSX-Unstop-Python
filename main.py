import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Portfolio", layout="wide")

# html is used only here
with st.container():
    st.markdown("""
    <div class='navbar' style="font-weight: bold;">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects-and-achievements">Projects & Achievements</a>
        <a href="#contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)

# Home
st.markdown("---")
st.markdown("""<h2 id="home">🏠 Home</h2>""", unsafe_allow_html=True)
col1, col2 = st.columns([1, 2])

with col1:
    st.image("Photograph.jpg", width=250, caption="Nisha Kumari", output_format="auto")

with col2:
    st.subheader("Hey, I am")
    st.subheader("Nisha Kumari")
    st.markdown("#### Graduating in B.Tech IT")
    st.markdown("#### Driven by degree,")
    st.markdown("#### powered by passion!")
    with open("Resume.pdf", "rb") as file:
        st.download_button("📄 Download Resume", file, "Resume.pdf")
    with open("CV.pdf", "rb") as file:
        st.download_button("📃 Download CV", file, "CV.pdf")

# About
st.markdown("---")
st.markdown("""<h2 id="about">📖 About</h2>""", unsafe_allow_html=True)
st.code("""
#Code to decode me ;)
I'm Nisha Kumari, pursuing my B.Tech. in Information Technology(Batch:2022-2026) from Bharati Vidyapeeth's College of Engineering, New Delhi affiliated from Guru Gobind Sing Indraprastha University.
I am intrested in the domain of data science along with AI & ML.
Python is my go to language.
I love exploring new domains & technologies.
""")

# Skills
st.markdown("---")
st.markdown("""<h2 id="skills">💼 Skills</h2>""", unsafe_allow_html=True)
skills = ["Python", "Streamlit", "HTML", "CSS", "JavaScript", "Machine Learning", "Data Analysis"]
cols = st.columns(3)
for idx, skill in enumerate(skills):
    with cols[idx % 3]:
        st.button(skill, use_container_width=True)

# Projects & Achievements
st.markdown("---")
st.markdown("""<h2 id="projects-and-achievements">🏆 Projects & Achievements</h2>""", unsafe_allow_html=True)
st.markdown(f"""
    ### 📌 Project {1}: Platemate
    - Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    - [🔗 View Project](https://www.linkedin.com/posts/oorgita-sur-258b36253_hackathon-ai-diabetes-activity-7180632782702800896-kXMV?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE04i64Bqp7jUE4HbkM4W7LxTuXUlTENTp0)
    """)
st.markdown(f"""
    ### 📌 Project {2}: Easer
    - Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    - [🔗 View Project](https://www.linkedin.com/posts/shyam-agarwal-926521273_innovicon-softwareexpo-webd-activity-7317754568124035073-C0Lb?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE04i64Bqp7jUE4HbkM4W7LxTuXUlTENTp0)
    """)
st.markdown(f"""
    ### 📌 Project {3}: Pixelate: Sustainable Resources
    - Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    - [🔗 View Project](https://drive.google.com/file/d/1vG55VTP2vnGZ-aiZokUBvtFMRVbcg7LQ/view?usp=sharing)
    """)

# Contact
st.markdown("---")
with st.container():
    st.markdown("""<h2 id="contact">📬 Contact</h2>""", unsafe_allow_html=True)
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")

    if submit_button:
        df = pd.DataFrame([[name, email, message]], columns=["Name", "Email", "Message"])
        df.to_csv("contact_submissions.csv", mode='a', header=False, index=False)
        st.success(f"Thanks {name}, your message has been sent!")

st.markdown("---")
with st.container():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("Photograph.jpg", width=80)
    with col2:
        st.markdown("""
        **Nisha Kumari**  
        🏠 New Delhi, India  
        📞 +91-9798080231  
        📧 namenishakumari@gmail.com  
        [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue)](https://www.linkedin.com/in/nisha-kumari-492a64301/)  
        [![GitHub](https://img.shields.io/badge/-GitHub-black)](https://github.com/0nisha0kumari0)
        """)

