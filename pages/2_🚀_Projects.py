from pathlib import Path
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "static" / "styles" / "main.css"

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Projects | Daniel Cooke",
    page_icon="👋🏾",
    layout="wide"
)

# --- LOAD CSS ---
if css_file.exists():
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 Projects & Accomplishments")
st.markdown("A showcase of my technical projects and side ventures")
st.markdown("---")

# --- FEATURED PROJECTS ---
st.markdown("### ⭐ Featured Projects")
st.markdown("<p style='color:red; font-style:italic;'>Note: Render-hosted projects may take up to 2 mins to load on first visit. If unsuccessful, please refresh.</p>", unsafe_allow_html=True)

featured_projects = [
    {
        "title": "🏆 Places Search",
        "description": "Working with the Google Maps Places API to search and explore locations.",
        "link": "https://luwah-places-search.onrender.com",
        "technologies": ["Python", "Streamlit", "Google Maps API"],
        "status": "Live"
    },
    {
        "title": "🏆 Citation Machine",
        "description": "A robust way to cite sources without ads - clean and easy to use citation generator.",
        "link": "https://luwahs-citation-machine.onrender.com",
        "technologies": ["Python", "Streamlit"],
        "status": "Live"
    },
    {
        "title": "🏆 GSheets Database",
        "description": "Query an Excel file like a database table - bringing SQL-like functionality to spreadsheets.",
        "link": "https://luwah-gs-db.streamlit.app/",
        "technologies": ["Python", "Streamlit", "Pandas", "SQL"],
        "status": "Live"
    },
]

for project in featured_projects:
    with st.container():
        st.markdown(
            f"""
            <div style='
                background-color: #073642;
                border-left: 4px solid #d33682;
                border-radius: 0 10px 10px 0;
                padding: 1.5rem;
                margin-bottom: 1rem;
            '>
                <h4 style='margin-top: 0;'>{project['title']}</h4>
                <p style='color: #93a1a1;'>{project['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            tech_badges = " ".join([f"`{tech}`" for tech in project['technologies']])
            st.markdown(f"**Tech:** {tech_badges}")
        with col2:
            st.markdown(f"**Status:** {project['status']}")
        with col3:
            st.markdown(f"[🔗 View Project]({project['link']})")
        
        st.markdown("")

st.markdown("---")

# --- PROJECT CATEGORIES ---
tab1, tab2, tab3 = st.tabs(["💼 Professional Work", "🔧 Automation", "🏠 Personal/Homelab"])

# --- PROFESSIONAL PROJECTS ---
with tab1:
    st.markdown("### Professional Highlights")
    
    professional_work = [
        {
            "title": "Data Migration to Snowflake",
            "company": "United Healthcare",
            "description": "Led migration of extensive datasets from SQL Server, Hive, and Teradata to Snowflake using Python, SAS, and SnowSQL.",
            "impact": "Successfully migrated terabytes of data while maintaining data integrity",
            "technologies": ["Snowflake", "Python", "SAS", "SnowSQL", "SQL Server", "Hive", "Teradata"]
        },
        {
            "title": "SAS to Python Script Optimization",
            "company": "United Healthcare",
            "description": "Redesigned legacy SAS scripts in Python, achieving significant performance improvements.",
            "impact": "25% improvement in script runtime",
            "technologies": ["Python", "SAS", "Pandas", "NumPy"]
        },
        {
            "title": "Airflow DAG Development",
            "company": "United Healthcare",
            "description": "Developed and maintained Airflow DAGs for automating scheduled job executions and data pipelines.",
            "impact": "Automated critical data workflows",
            "technologies": ["Apache Airflow", "Python", "SQL"]
        },
        {
            "title": "SAP BOBJ Report Optimization",
            "company": "Tuff Shed",
            "description": "Optimized SAP Business Objects reports using T-SQL stored procedures.",
            "impact": "Reduced load/refresh time from 30 minutes to 30 seconds",
            "technologies": ["SAP BOBJ", "T-SQL", "SQL Server"]
        },
        {
            "title": "Azure DevOps CI/CD Implementation",
            "company": "Tuff Shed",
            "description": "Developed CI/CD functionality for Azure DevOps on Azure Synapse Analytics workspaces.",
            "impact": "Streamlined deployment process for analytics workspaces",
            "technologies": ["Azure DevOps", "Azure Synapse Analytics", "CI/CD"]
        },
    ]
    
    for work in professional_work:
        with st.expander(f"📊 {work['title']} - {work['company']}", expanded=False):
            st.markdown(work['description'])
            st.markdown(f"**📈 Impact:** {work['impact']}")
            tech_badges = " ".join([f"`{tech}`" for tech in work['technologies']])
            st.markdown(f"**Technologies:** {tech_badges}")

# --- AUTOMATION PROJECTS ---
with tab2:
    st.markdown("### Automation & Integration Projects")
    
    automation_projects = [
        {
            "title": "Smart Email Management System",
            "description": "Automatically sorts inbox by importance, deletes promotional emails on schedule, creates calendar events from messages, and logs key details to spreadsheets—keeping inbox at zero without manual effort.",
            "technologies": ["n8n", "Gmail API", "Google Sheets", "Google Calendar"],
            "features": ["Auto-sorting by importance", "Scheduled promo deletion", "Calendar event creation", "Spreadsheet logging"]
        },
        {
            "title": "Communication Automation - Chess Club",
            "description": "Built a one-tap notification system for a chess club coordinator to message 100+ members instantly—works even when they're unavailable.",
            "technologies": ["n8n", "Twilio", "Apple Shortcuts"],
            "features": ["One-tap mass messaging", "100+ member reach", "Works offline", "Instant delivery"]
        },
        {
            "title": "AI-Powered Documentation Generator",
            "description": "Automatically generate meeting summaries, project documentation, or reports using AI—saving hours of writing time while maintaining voice and style.",
            "technologies": ["n8n", "OpenAI API", "Google Docs", "Notion"],
            "features": ["Meeting summaries", "Project documentation", "Custom voice/style", "Multi-platform output"]
        },
        {
            "title": "Content Summarization System",
            "description": "Created automatic summaries of long content (podcasts, videos, articles) delivered via email or text with key takeaways—stay informed without spending hours.",
            "technologies": ["n8n", "OpenAI API", "YouTube API", "Email/SMS"],
            "features": ["Podcast summaries", "Video transcription", "Article extraction", "Email/text delivery"]
        },
        {
            "title": "Intelligent Reminder System",
            "description": "Automated notifications for subscription renewals, important deadlines, and recurring tasks—customized to schedule so nothing falls through the cracks.",
            "technologies": ["n8n", "Google Calendar", "Twilio", "Discord"],
            "features": ["Subscription tracking", "Deadline reminders", "Custom schedules", "Multi-channel alerts"]
        },
        {
            "title": "Goals Tracking Web Application",
            "description": "Comprehensive goals tracking system with Google Sheets integration. Features yearly/quarterly/monthly/weekly goal tracking with Adventure Challenge integration.",
            "technologies": ["Python", "Streamlit", "Google Sheets API", "OAuth2"],
            "features": ["Multi-level goal hierarchy", "Shared access for collaboration", "Progress visualization", "Adventure Challenge tracking"]
        },
        {
            "title": "Fantasy Premier League Monitor",
            "description": "Automated n8n workflow for monitoring FPL team performance, player updates, and gameweek notifications.",
            "technologies": ["n8n", "FPL API", "Discord Webhooks", "JavaScript"],
            "features": ["Real-time team updates", "Transfer suggestions", "Gameweek reminders", "Performance analysis"]
        },
        {
            "title": "Referee Payment Tracking System",
            "description": "MySQL-based system for tracking referee game assignments and payments from Assignr with automated reconciliation.",
            "technologies": ["MySQL", "n8n", "Assignr API", "Python"],
            "features": ["Payment reconciliation", "Expected vs actual comparison", "Automated notifications", "Report generation"]
        },
    ]
    
    for project in automation_projects:
        with st.expander(f"🔄 {project['title']}", expanded=False):
            st.markdown(project['description'])
            
            st.markdown("**Key Features:**")
            for feature in project['features']:
                st.markdown(f"- {feature}")
            
            tech_badges = " ".join([f"`{tech}`" for tech in project['technologies']])
            st.markdown(f"**Technologies:** {tech_badges}")

# --- HOMELAB/PERSONAL PROJECTS ---
with tab3:
    st.markdown("### Homelab & Personal Projects")
    
    st.markdown("""
    I maintain a sophisticated self-hosted infrastructure for learning, experimentation, and running production services.
    This setup powers many of my automation projects and replaces expensive cloud subscriptions.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🖥️ Infrastructure Stack:**
        - Proxmox VE (Virtualization)
        - OpenMediaVault NAS
        - LXC Containers & Docker
        - Custom VLAN networking
        - Enterprise-grade backups
        """)
    
    with col2:
        st.markdown("""
        **🛠️ Self-Hosted Services:**
        - n8n (Workflow Automation)
        - Invoice Ninja (Billing)
        - BookStack (Documentation)
        - Vikunja (Task Management)
        - Shlink (URL Shortener)
        - LinkStack (Link Hub)
        """)
    
    st.markdown("---")
    st.markdown("### 💡 Self-Hosted Solutions")
    
    st.info("""
    **Replace Expensive Subscriptions:** Host your own cloud storage instead of paying Google or Apple monthly. 
    Access files from any device with enterprise-grade security—saving $50-200/month while keeping full control of your data.
    """)
    
    homelab_projects = [
        {
            "title": "Energy-Saving Smart Home",
            "description": "Lights and appliances automatically adjust when leaving or going to bed. Voice control everything. Calendar events announce on speakers before they start—reducing energy bills while adding convenience.",
            "status": "Completed"
        },
        {
            "title": "Personal Cloud Storage",
            "description": "Self-hosted file sync and backup solution replacing Google Drive/iCloud. Full control over data with access from any device.",
            "status": "Completed"
        },
        {
            "title": "Linkstack Deployment",
            "description": "Personal link management solution for consolidating social and professional links in one place.",
            "status": "Completed"
        },
        {
            "title": "Sunset Notification System",
            "description": "Automated system that sends notifications based on sunset times—useful for outdoor activities and soccer refereeing.",
            "status": "Completed"
        },
        {
            "title": "Internal Documentation Wiki",
            "description": "BookStack-powered knowledge base for documenting processes, configurations, and project notes.",
            "status": "Completed"
        },
        {
            "title": "Call of Duty Patch Notes Extractor",
            "description": "Automated extraction and parsing of CoD patch notes for tracking game updates and changes.",
            "status": "Completed"
        },
    ]
    
    for project in homelab_projects:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"**{project['title']}**")
            st.markdown(f"_{project['description']}_")
        with col2:
            status_color = "#2ecc71" if project['status'] == "Active" else "#586e75"
            st.markdown(f"<span style='background-color: {status_color}; padding: 2px 8px; border-radius: 10px; font-size: 0.8rem;'>{project['status']}</span>", unsafe_allow_html=True)
        st.markdown("---")


# --- GITHUB SECTION ---
st.markdown("### 💻 More on GitHub")
st.markdown("""
Check out more of my projects and contributions on GitHub:

[🔗 github.com/Luwalekeah](https://github.com/Luwalekeah)
""")


# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #586e75;'>
        🔨 Always building something new | 
        <a href="https://github.com/Luwalekeah">View GitHub Profile</a>
    </div>
    """,
    unsafe_allow_html=True
)