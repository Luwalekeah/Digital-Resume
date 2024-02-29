from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Daniel_Cooke_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Daniel Cooke"
PAGE_ICON = ":wave:"
NAME = "Daniel Cooke"
DESCRIPTION = """
Senior Data Engineer
"""
EMAIL = "daniel.cooke900@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/daniel-cooke/",
    "GitHub": "https://github.com/Luwalekeah",
    "Credly": "https://www.credly.com/users/daniel-cooke.94fe75dd/badges",
}
PROJECTS = {
    "🏆 Places Search - Working with the Google Maps Places API ": "https://luwah-places-search.onrender.com",
    "🏆 Citation Machine - A robust way to cite sources w/ out ads": "https://luwahs-citation-machine.onrender.com",
    "🏆 GSheets Database - This will be live soon": "https://github.com/Luwalekeah/Google-Sheets-Database",
    "🏆 Recent Certificaiton - Microsoft Certified: Azure Fundamentals (AZ-900) ": "https://learn.microsoft.com/en-us/users/dcooke/transcript/vplg0t2qnzxxqrj",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- SUMMARY ---
st.write('\n')
st.subheader("Summary")
st.write(
    """
Senior Data Engineer with over 6 years of hands-on experience in leveraging data to
drive strategic decision-making and achieve business success. Known for the ability to rapidly
grasp new software tools and technologies, transforming them into powerful data solutions. A
natural problem solver and expert in the field, I bring a proven track record of delivering impactful
data-driven solutions.
"""
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 6 Years expereince extracting actionable insights from data
- ✔️ Strong working expereience in Python, SQL, and Tableau
- ✔️ Excellent knowledge in building data pipelines and finding anomolies
- ✔️ Great team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, Numpy), SQL, SAS
- 📊 Data Visulization: Tableau, Excel, SAP BOBJ
- 📚 Software: Airflow, Azure {DevOps, Synapse Analytics, Machine Learning}
- 🗄️ Databases: Snowflake, MS SQL Server, MySQL
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.write("---")
st.subheader("Projects & Accomplishments")
st.markdown("<p style='color:lavender; font-style:italic;'>First two links may take up to 2 mins to load. If unsuccessful, please refresh the window.</p>", unsafe_allow_html=True)
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- WORK HISTORY ---
st.write('\n')
st.write("---")
st.subheader("Work History")

# --- JOB 1
st.write("🚧", "**Senior Data Engineer | United Healthcare (M&R Stars)**")
st.write("10/2022 - Present")
st.write(
    """
- ► Developed and sustained Airflow DAGs for the automation of scheduled job executions.
- ► Effectively migrated extensive datasets from diverse systems, including SQL Server, Hive, and Teradata, to Snowflake, employing Python, SAS, and SnowSQL.
- ► Redesigned scripts from SAS to Python that saw a 25% speed in run time 
- ► Served as the Subject Matter Expert (SME) for Snowflake & all datasets consumed by my team.
- ► Developed Tableau dashboards for internal consumption while providing vital data to various teams on a monthly and weekly basis.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Business Intelligence Developer | Tuff Shed**")
st.write("10/2019 - 10/2022")
st.write(
    """
- ► Developed Continuous Integration & Continuous Deployment (CI/CD) functionality for Azure DevOps on our Azure Synapse Analytics workspaces.
- ► Optimized SAP Business Objects (BOBJ) reports to load/refresh within 30 sec from previous 30 min through the use of T-SQL stored procedures.
- ► Built core reports, business trusted data flows/sources with the use of Tableau Desktop, Tableau Prep Builder, and Tableau Online.
- ► Utilized Salesforce reporting to deliver business answers and drive insights.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**SAP Business Intelligence Intern | Woodward Inc.**")
st.write("01/2019 - 09/2019")
st.write(
    """
- ► Advanced understanding of Universe Design and Development using Information Design Tool and Universe Design Tool (IDT & UDT)
- ► Developing semi-complex reports and maintained complex reports using Web Intelligence (Webi) Rich Client, Design Studio, and Business Objects (BOBJ)
- ► Proven ability to work in cross-functional teams with high sense of ownership and strong customer focus
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Business Intelligence Intern | Emerson | Micro Motion Inc.**")
st.write("05/2018 - 01/2019")
st.write(
    """
- ► Database code synchronization process using Redgate Tools
- ► Standardize BI SSRS report filters so users can filter by multiple sites
- ► SSIS standardization: added global variables to check for local server name; created email notification standards
"""
)


# --- JOB 5
st.write('\n')
st.write("🚧", "**Web Developer | Lory Student Center Catering**")
st.write("02/2018 - 09/2019")
st.write(
    """
- ► National Association of College & Universities Food Services (NACUFS) 2019 Gold prize winner for Large Schools
- ► Proficiently employed JavaScript and Bootstrap 4.0 to implement 'Collapse' functionality in the Catering Menu.
- ► Demonstrated intermediate-level proficiency in HTML5 and CSS as a web developer.
- ► Skillfully leveraged Adobe Photoshop and Illustrator for the design and editing of website assets.
- ► Effectively collaborated with team members to ensure the timely delivery of requested items, consistently meeting deadlines.
"""
)

