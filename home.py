import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Zeineb Portfolio",
    page_icon="📊",
)


def home_page():
    # ----- Left menu -----
    with st.sidebar:
        st.image("eae_img.png", width=200)
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("***Final Project - Dec 2025***")
        st.write("**Author:** <Zeineb Hachana> ")
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


    # ----- Top title -----
    st.html("""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Zeineb </h1></div>""")  # TODO: Add your name


    # ----- Profile image file -----
    profile_image_file_path = "profile.png"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

    with open(profile_image_file_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


    # ----- Your Profile Image -----
    st.html(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="Zeineb" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """)


    # ----- Personal title or short description -----
    current_role = "Master’s Student in Big Data & Analytics"   # TODO: Change this

    st.html(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""")

    st.write("##")    # Adding some space


    # ----- About me section -----
    st.subheader("About Me")

    # TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
    st.write("""
    - 🧑‍💻 Master’s student in Big Data & Analytics

    - 🛩️ prev: Bachelor in Business Administration

    - ❤️ learning, travel, well-being, and meaningful experiences

    - 🏂 Tennis and Dance

    - 📫 Email: hachhachzeineb@gmail.com

    - 🏠 Barcelona, Spain
    """)
    st.write("Contact information:")
    st.write("🔗 LinkedIn: [Zeineb Hachana](https://www.linkedin.com/in/zeineb-hachana-a5b80126a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)")
    st.markdown("""
**Data & Analytics Master’s student** with a strong interest in turning data into clear insights.  
Background in business, finance, and analytics. Practical and results-oriented.
""")
    st.markdown("### Business & Management Skills")
    st.markdown("""
- Business administration fundamentals  
- Financial analysis basics  
- Strategic thinking  
- Market and company analysis  
- Reporting and presentation skills
""")
    st.markdown("### Data & Analytics Skills")
    st.markdown("""
- Python (data analysis – beginner)  
- Data analytics fundamentals  
- Data visualization (basic)  
- SQL (introductory level)
""")
    st.markdown("### Academic Work & Learning")
    st.markdown("""
- Coursework in data analytics and Python  
- Business and financial analysis from Bachelor studies  
- Ongoing development of practical analytics skills
""")


    # Feel free to add other points like your Linkedin, Github, Social Media, etc.


# This is ensambling the entire app with the different pages and the navigation menu
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("pages/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("pages/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("pages/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])
pg.run()
