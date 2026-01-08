from pathlib import Path
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "static" / "styles" / "main.css"
certs_dir = current_dir / "static" / "assets" / "certs"

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Certifications | Daniel Cooke",
    page_icon="👋🏾",
    layout="wide"
)

# --- LOAD CSS ---
if css_file.exists():
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- HEADER ---
st.title("📜 Certifications & Credentials")
st.markdown("Professional certifications and continuous learning achievements")
st.markdown("---")

# --- EXTERNAL CREDENTIAL LINKS ---
st.markdown("### 🔗 Verification Links")
col1, col2 = st.columns(2)
with col1:
    st.markdown("[🏅 View all badges on Credly](https://www.credly.com/users/daniel-cooke.94fe75dd/badges)")
with col2:
    st.markdown("[📋 Microsoft Learn Transcript](https://learn.microsoft.com/en-us/users/dcooke/transcript/vplg0t2qnzxxqrj)")

st.markdown("---")

# --- SUMMARY STATS (MOVED TO TOP) ---
st.markdown("### 📈 Certification Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Certifications", "11")
with col2:
    st.metric("Microsoft Azure", "4")
with col3:
    st.metric("Snowflake", "4")
with col4:
    st.metric("Other", "3")

# --- IN PROGRESS SECTION (MOVED TO TOP) ---
st.markdown("---")
st.markdown("### 📚 Currently Pursuing")

in_progress = [
    {
        "name": "Azure DevOps Engineer Expert (AZ-400)",
        "target": "Q1 2026",
        "progress": 0
    },
    {
        "name": "Docker Certified Associate",
        "target": "Q1 2026",
        "progress": 0
    },
    {
        "name": "Ansible Automation Certification",
        "target": "Q1 2026",
        "progress": 0
    },
    {
        "name": "Kubernetes Administrator (CKA)",
        "target": "Q2 2026",
        "progress": 0
    },
    {
        "name": "HashiCorp Terraform Associate",
        "target": "Q2 2026",
        "progress": 0
    },
    {
        "name": "Proxmox VE Administrator",
        "target": "Q2 2026",
        "progress": 0
    },
]

for cert in in_progress:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown(f"**{cert['name']}**")
    with col2:
        st.markdown(f"Target: {cert['target']}")
    with col3:
        st.progress(cert['progress'] / 100)

st.markdown("---")

# --- CERTIFICATIONS DATA ---
certifications = [
    # Microsoft Azure Certifications
    {
        "name": "Microsoft Certified: Azure Fundamentals (AZ-900)",
        "issuer": "Microsoft",
        "date": "February 2024",
        "description": "Demonstrates foundational knowledge of cloud concepts, Azure services, Azure workloads, security and privacy in Azure, as well as Azure pricing and support.",
        "skills": ["Azure", "Cloud Computing", "Cloud Services", "Azure Architecture"],
        "badge_color": "#0078D4",
        "verify_link": "https://learn.microsoft.com/en-us/users/dcooke/transcript/vplg0t2qnzxxqrj",
        "pdf_file": "ACG Microsoft AZ-900 Certificate of completion.pdf",
        "category": "Cloud"
    },
    {
        "name": "Microsoft Certified: Azure Data Scientist Associate (DP-100)",
        "issuer": "Microsoft",
        "date": "May 2021",
        "description": "Validates expertise in applying data science and machine learning to implement and run machine learning workloads on Azure.",
        "skills": ["Azure ML", "Machine Learning", "Data Science", "Python", "MLOps"],
        "badge_color": "#0078D4",
        "verify_link": "https://learn.microsoft.com/en-us/users/dcooke/transcript/vplg0t2qnzxxqrj",
        "pdf_file": "DP100 Certificate.pdf",
        "category": "Cloud"
    },
    {
        "name": "Microsoft Certified: Azure Data Engineer Associate (DP-200)",
        "issuer": "Microsoft",
        "date": "May 2021",
        "description": "Validated skills in implementing data storage solutions, managing and developing data processing, and monitoring and optimizing data solutions using Azure services.",
        "skills": ["Azure Data Factory", "Azure Synapse", "Data Pipelines", "ETL"],
        "badge_color": "#0078D4",
        "verify_link": "https://learn.microsoft.com/en-us/users/dcooke/transcript/vplg0t2qnzxxqrj",
        "pdf_file": "DP200 Certificate.pdf",
        "category": "Cloud",
        "retired": True
    },
    {
        "name": "Microsoft Certified: Azure Data Engineer Associate (DP-201)",
        "issuer": "Microsoft",
        "date": "December 2021",
        "description": "Validated expertise in designing Azure data storage solutions, data processing solutions, and data security and compliance solutions.",
        "skills": ["Azure Architecture", "Data Solution Design", "Security", "Compliance"],
        "badge_color": "#0078D4",
        "verify_link": "https://learn.microsoft.com/en-us/users/dcooke/transcript/vplg0t2qnzxxqrj",
        "pdf_file": "DP 201 Certificate.pdf",
        "category": "Cloud",
        "retired": True
    },
    
    # Tableau
    {
        "name": "Tableau Desktop Specialist",
        "issuer": "Tableau",
        "date": "December 2021",
        "description": "Demonstrates foundational skills in Tableau Desktop, including connecting to data, creating visualizations, and building dashboards.",
        "skills": ["Tableau", "Data Visualization", "Dashboards", "Analytics"],
        "badge_color": "#E97627",
        "verify_link": None,
        "pdf_file": "Tableau Desktop Specialist Certificate.pdf",
        "category": "Analytics"
    },
    
    # Snowflake Hands-On Essentials
    {
        "name": "Snowflake Hands-On Essentials: Data Warehouse",
        "issuer": "Snowflake",
        "date": "December 2022",
        "description": "Completed hands-on training covering Snowflake data warehouse fundamentals, including loading data, querying, and performance optimization.",
        "skills": ["Snowflake", "Data Warehousing", "SQL", "Data Loading"],
        "badge_color": "#29B5E8",
        "verify_link": None,
        "pdf_file": "HandsOnEssentials-DataWarehouse_Badge20221205-30-1fjwjp2.pdf",
        "category": "Data Platform"
    },
    {
        "name": "Snowflake Hands-On Essentials: Data Lake",
        "issuer": "Snowflake",
        "date": "May 2023",
        "description": "Completed hands-on training for working with data lakes in Snowflake, including external stages, file formats, and semi-structured data.",
        "skills": ["Snowflake", "Data Lake", "Semi-structured Data", "External Stages"],
        "badge_color": "#29B5E8",
        "verify_link": None,
        "pdf_file": "HandsOnEssentials-DataLake_Badge20230510-28-157fx9j.pdf",
        "category": "Data Platform"
    },
    {
        "name": "Snowflake Hands-On Essentials: Data Sharing",
        "issuer": "Snowflake",
        "date": "December 2022",
        "description": "Completed hands-on training covering Snowflake's secure data sharing capabilities, including creating and managing shares.",
        "skills": ["Snowflake", "Data Sharing", "Data Marketplace", "Secure Sharing"],
        "badge_color": "#29B5E8",
        "verify_link": None,
        "pdf_file": "HandsOnEssentials-DataSharing_Badge20221205-30-4lwm72.pdf",
        "category": "Data Platform"
    },
    {
        "name": "Snowflake Hands-On Essentials: Data Applications",
        "issuer": "Snowflake",
        "date": "December 2022",
        "description": "Completed hands-on training for building data applications with Snowflake, including Snowpark and application development patterns.",
        "skills": ["Snowflake", "Snowpark", "Data Applications", "Python"],
        "badge_color": "#29B5E8",
        "verify_link": None,
        "pdf_file": "HandsOnEssentials-DataApplications_Badge20221205-30-48wjwh.pdf",
        "category": "Data Platform"
    },
    
    # Sololearn
    {
        "name": "Python for Beginners",
        "issuer": "Sololearn",
        "date": "December 2022",
        "description": "Completed comprehensive Python programming course covering fundamentals, data structures, and basic programming concepts.",
        "skills": ["Python", "Programming Fundamentals", "Data Structures"],
        "badge_color": "#2ECC71",
        "verify_link": None,
        "pdf_file": "Sololearn Python for Beginners.pdf",
        "category": "Programming"
    },
    {
        "name": "SQL",
        "issuer": "Sololearn",
        "date": "December 2022",
        "description": "Completed SQL course covering database queries, joins, aggregations, and data manipulation.",
        "skills": ["SQL", "Database Queries", "Data Manipulation"],
        "badge_color": "#2ECC71",
        "verify_link": None,
        "pdf_file": "Sololearn SQL.pdf",
        "category": "Programming"
    },
]

# --- GROUP BY CATEGORY ---
categories = {}
for cert in certifications:
    cat = cert.get('category', 'Other')
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(cert)

# Define category order and icons
category_order = [
    ("Cloud", "☁️"),
    ("Data Platform", "❄️"),
    ("Analytics", "📊"),
    ("Programming", "💻"),
]

# --- DISPLAY CERTIFICATIONS BY CATEGORY ---
for cat_name, cat_icon in category_order:
    if cat_name in categories:
        st.markdown(f"### {cat_icon} {cat_name} Certifications")
        
        for cert in categories[cat_name]:
            with st.container():
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    # Certificate badge
                    retired_badge = "<br><span style='font-size: 0.6rem; color: #e74c3c;'>RETIRED</span>" if cert.get('retired') else ""
                    st.markdown(
                        f"""
                        <div style='
                            background: linear-gradient(135deg, {cert['badge_color']}22 0%, {cert['badge_color']}44 100%);
                            border: 2px solid {cert['badge_color']};
                            border-radius: 10px;
                            padding: 15px;
                            text-align: center;
                            min-height: 90px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        '>
                            <div>
                                <div style='font-size: 1.8rem;'>🏆</div>
                                <div style='font-size: 0.75rem; color: {cert['badge_color']}; font-weight: bold;'>{cert['issuer']}{retired_badge}</div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                with col2:
                    # Title with retired indicator
                    title = cert['name']
                    if cert.get('retired'):
                        title += " *(Retired Exam)*"
                    st.markdown(f"#### {title}")
                    st.markdown(f"**{cert['issuer']}** | Issued: {cert['date']}")
                    st.markdown(cert['description'])
                    
                    # Skills tags
                    skills_html = " ".join([
                        f"<span style='background-color: #586e75; color: white; padding: 3px 10px; border-radius: 15px; margin-right: 5px; font-size: 0.8rem;'>{skill}</span>"
                        for skill in cert['skills']
                    ])
                    st.markdown(skills_html, unsafe_allow_html=True)
                    
                    # Action buttons
                    btn_col1, btn_col2 = st.columns([1, 3])
                    
                    with btn_col1:
                        # PDF Download button
                        if cert.get('pdf_file'):
                            pdf_path = certs_dir / cert['pdf_file']
                            if pdf_path.exists():
                                with open(pdf_path, "rb") as pdf_file:
                                    st.download_button(
                                        label="📄 Download Certificate",
                                        data=pdf_file.read(),
                                        file_name=cert['pdf_file'],
                                        mime="application/pdf",
                                        key=f"download_{cert['name']}"
                                    )
                            else:
                                st.caption(f"_PDF not found_")
                    
                    with btn_col2:
                        if cert.get('verify_link'):
                            st.markdown(f"[🔗 Verify on Microsoft Learn]({cert['verify_link']})")
                
                st.markdown("---")


# --- FOOTER ---
st.markdown(
    """
    <div style='text-align: center; color: #586e75;'>
        💡 Certifications are regularly updated | 
        <a href="https://www.credly.com/users/daniel-cooke.94fe75dd/badges">View on Credly</a> | 
        <a href="https://learn.microsoft.com/en-us/users/dcooke/transcript/vplg0t2qnzxxqrj">Microsoft Transcript</a>
    </div>
    """,
    unsafe_allow_html=True
)