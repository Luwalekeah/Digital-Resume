from pathlib import Path
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "static" / "styles" / "main.css"

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Luwah Technologies | Daniel Cooke",
    page_icon="👋🏾",
    layout="wide"
)

# --- LOAD CSS ---
if css_file.exists():
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- HEADER ---
st.title("🏢 Luwah Technologies LLC")
st.markdown("*Where Simplicity Meets Innovation*")
st.markdown("""
Founded in 2025, Luwah Technologies helps small businesses and individuals harness technology 
without the complexity. Based in Aurora, Colorado.
""")
st.markdown("---")

# --- SERVICES ---
st.markdown("## What We Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### ⚙️ Automation
    
    Eliminate repetitive tasks with automated workflows that run in the background. 
    Pre-built templates offer quick solutions, while custom development tackles unique challenges.
    
    **Recent work:**
    - Email sorting systems
    - Smart home integrations
    - Notification workflows
    - Subscription management
    """)

with col2:
    st.markdown("""
    ### 🔧 Technology Advisory
    
    Unbiased guidance for confident technology decisions. Strategic advice on hardware, 
    software, and business infrastructure that prioritizes your goals.
    
    **Recent work:**
    - Business technology setup
    - Hardware consultation
    - Platform selection
    - Cost optimization strategies
    """)

with col3:
    st.markdown("""
    ### 📚 Education
    
    Personalized training to build technology confidence and skills. From basic computer 
    literacy to tech career transitions, education is tailored to your pace and learning style.
    
    **Recent work:**
    - Tech career coaching
    - Digital literacy training
    - Blog articles
    - YouTube tutorials
    """)

st.markdown("---")

# --- CAPABILITIES SHOWCASE ---
st.markdown("## Real Solutions for Real People")
st.markdown("*Technology should work for you, not confuse you. Here's how we've helped others save time, money, and frustration:*")

capabilities = [
    {
        "title": "Communication Automation",
        "description": "Built a one-tap notification system for a chess club coordinator to message 100+ members instantly—works even when they're unavailable."
    },
    {
        "title": "Smart Home Setup",
        "description": "Configured automated lighting and appliances that save on energy bills—lights turn off when you leave, and everything adjusts to your schedule."
    },
    {
        "title": "Intelligent Reminders",
        "description": "Set up automated notifications for subscription renewals, important deadlines, and recurring tasks—customized to your schedule so nothing falls through the cracks."
    },
    {
        "title": "Business Launch Support",
        "description": "Guided multiple clients through business setup: custom email addresses, document organization systems, and software recommendations—everything needed to start professional."
    },
    {
        "title": "Simplified Tech Support",
        "description": "Helped an elderly client use her phone and computer confidently—from video calls with grandkids to organizing photos—saving hundreds compared to repair shops."
    },
    {
        "title": "Computer Basics Training",
        "description": "Taught clients to organize files, manage emails, and edit photos digitally—eliminating printing costs and saving hours of time each week."
    },
    {
        "title": "Content Summaries",
        "description": "Created automatic summaries of long content (podcasts, videos, articles) delivered via email or text with key takeaways—stay informed without spending hours."
    },
    {
        "title": "Career Transition Coaching",
        "description": "Mentored individuals switching to tech careers—created study plans, provided practice tests, and helped choose between bootcamps, self-paced courses, or university programs."
    },
]

# Display in 2 columns
col1, col2 = st.columns(2)
for i, cap in enumerate(capabilities):
    with col1 if i % 2 == 0 else col2:
        with st.expander(f"✅ {cap['title']}", expanded=False):
            st.markdown(cap['description'])

st.markdown("---")

# --- ADVANCED AUTOMATION ---
st.markdown("## Advanced Automation (What's Possible)")
st.markdown("*Systems we've developed and deployed—proven capabilities ready to customize for your needs:*")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **📧 Smart Email Management**
    
    Automatically sorts inbox by importance, deletes promotional emails on schedule, 
    creates calendar events from certain messages, and logs key details to spreadsheets—keeping 
    your inbox at zero without manual effort.
    """)
    
    st.markdown("""
    **💰 Replace Expensive Subscriptions**
    
    Host your own cloud storage instead of paying Google or Apple monthly. Access files 
    from any device with enterprise-grade security—saving $50-200/month while keeping 
    full control of your data.
    """)

with col2:
    st.markdown("""
    **🏠 Energy-Saving Smart Home**
    
    Lights and appliances automatically adjust when you leave or go to bed. Voice control 
    everything. Calendar events announce on speakers before they start—reducing energy 
    bills while adding convenience.
    """)
    
    st.markdown("""
    **🤖 AI-Powered Documentation**
    
    Automatically generate meeting summaries, project documentation, or reports using 
    AI—saving hours of writing time while maintaining your voice and style.
    """)

st.markdown("---")

# --- TECHNOLOGY STACK ---
st.markdown("## 🛠️ Technology Stack")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    **Financial & Billing**
    - Invoice Ninja
    - Wave Apps
    - Canvas Credit Union
    - GoFundMe
    """)

with col2:
    st.markdown("""
    **Business Operations**
    - Microsoft Office
    - SignRequest
    - Vikunja
    - BookStack
    """)

with col3:
    st.markdown("""
    **Automation & Dev**
    - n8n
    - Shlink
    - LinkStack
    """)

with col4:
    st.markdown("""
    **Social & Marketing**
    - YouTube
    - LinkedIn
    - Instagram
    - Facebook
    - WhatsApp
    """)

st.markdown("---")

# --- HOW WE WORK ---
st.markdown("## 💼 How We Work")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("**✓ FREE 30-minute consultation**\n\nLet's discuss your needs and explore solutions")

with col2:
    st.success("**✓ Project-based pricing**\n\nComplete project quotes including implementation and support")

with col3:
    st.success("**✓ Hourly consulting available**\n\n$30/hour for ongoing advisory or one-off questions")

st.markdown("---")

# --- ABOUT ---
st.markdown("## About Luwah Technologies")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    Founded by **Daniel Cooke**, a Senior Data Engineer with nearly a decade of enterprise experience 
    at UnitedHealthcare and Fortune 500 companies. I specialize in turning complex automation 
    capabilities into practical, accessible solutions for small businesses and individuals.
    
    **Technical Expertise:**
    - Snowflake, Databricks, Azure ML platforms
    - Python scripting & data pipeline development
    - n8n workflow automation & Apple Shortcuts
    - Self-hosted infrastructure (Proxmox homelab)
    
    **Our Mission:** Minimize manual intervention so you can focus on high-value work through 
    smart workflows, practical training, and reliable technology solutions.
    """)

with col2:
    st.markdown("""
    **📞 Contact**
    
    📧 info@luwahtechnologies.com
    
    📱 +1 (720) 421-7184
    
    📍 Aurora, Colorado
    """)

st.markdown("---")

# --- CTA ---
st.markdown("## 📅 Let's Work Together")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #d3368222 0%, #d3368244 100%);
        border: 2px solid #d33682;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
    '>
        <h3 style='margin-top: 0;'>Book your free 30-minute consultation today</h3>
        <p>Let's discuss how technology can work better for you.</p>
        <a href="https://luwahtechnologies.com" target="_blank" style='
            background-color: #d33682;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        '>🌐 Visit Our Site</a>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #586e75;'>
        Luwah Technologies LLC | Aurora, Colorado | Founded 2025
    </div>
    """,
    unsafe_allow_html=True
)