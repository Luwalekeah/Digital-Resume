# Digital Resume - Multi-Page Streamlit App

A multi-page digital resume built with Streamlit and hosted on Render.

## 🧱 Stack

| Component | Version |
|-----------|---------|
| Python    | 3.13.12 |
| Streamlit | 1.64.0  |
| Pillow    | 12.3.0  |

Dependencies are pinned in `requirements.txt`; the Python version and deploy settings are pinned in `render.yaml`.

## 🚀 Features

- **Home Page**: Overview, work history, skills, and contact information
- **Certifications Page**: Professional certifications with Credly integration and PDF certificate support
- **Projects Page**: Portfolio organized by category (Featured, Professional, Automation, Personal)
- **Luwah Technologies Page**: Services, capabilities, and pricing for Luwah Technologies LLC

## 📁 Project Structure

```
digital-resume/
├── .streamlit/
│   └── config.toml                 # Streamlit theme (see Theme below)
├── Home.py                         # Main landing page (entry point)
├── pages/
│   ├── 1_📜_Certifications.py      # Certifications & credentials
│   ├── 2_🚀_Projects.py            # Project portfolio
│   └── 3_🏢_Luwah_Technologies.py  # Luwah Technologies services
├── static/
│   ├── assets/
│   │   ├── Daniel_Cooke_CV.pdf     # Resume PDF
│   │   ├── profile-pic.png         # Profile picture
│   │   └── certs/                  # PDF certificates
│   └── styles/
│       └── main.css                # Custom CSS styling
├── render.yaml                     # Render deploy config (runtime + start command)
├── requirements.txt                # Pinned Python dependencies
└── Readme.md
```

## 🛠️ Setup

1. **Install dependencies** (Python 3.13 recommended, 3.10+ supported by Streamlit 1.64)
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your assets**
   - Place your profile picture as `static/assets/profile-pic.png`
   - Place your resume PDF as `static/assets/Daniel_Cooke_CV.pdf`
   - Place any PDF certificates in `static/assets/certs/`

3. **Run locally**
   ```bash
   streamlit run Home.py
   ```

## 📄 Adding PDF Certificates

To add a PDF certificate that can be downloaded from the Certifications page:

1. Place the PDF file in `static/assets/certs/`
2. Add (or update) an entry in the `certifications` list in `pages/1_📜_Certifications.py` and set `pdf_file` to the filename. A PDF that no entry references is not shown on the page.
   ```python
   {
       "name": "Your Cert Name",
       "issuer": "Issuing Organization",
       "date": "2024",
       "description": "Description here",
       "skills": ["Skill1", "Skill2"],
       "badge_color": "#FF5733",
       "verify_link": "https://verify-link.com",
       "pdf_file": "your_cert.pdf",  # filename in static/assets/certs/
       "category": "Cloud"
   }
   ```

## 🎨 Customization

### Theme
The theme values live in `.streamlit/config.toml` at the repo root, since that's the only path Streamlit reads config from (the directory it's launched in):
- `primaryColor`: Accent color (#d33682 - magenta)
- `backgroundColor`: Main background (#002b36 - dark blue)
- `secondaryBackgroundColor`: Sidebar (#586e75 - gray)
- `textColor`: Text color (#fff - white)

This applies the dark Solarized theme used across all four pages.

### Content
- **Home Page**: Update `Home.py` with your info
- **Certifications**: Edit `pages/1_📜_Certifications.py`
- **Projects**: Edit `pages/2_🚀_Projects.py`
- **Luwah Technologies**: Edit `pages/3_🏢_Luwah_Technologies.py`

## 🌐 Deployment

The site is deployed on [Render](https://render.com) as a Python web service. The deploy config lives in `render.yaml`:

- **Runtime**: `PYTHON_VERSION` is pinned in `render.yaml` (`envVars`). Update it there when changing Python versions.
- **Build command**: `pip install -r requirements.txt`
- **Start command**: `streamlit run Home.py --server.port $PORT --server.address 0.0.0.0 --server.headless true --browser.gatherUsageStats false`
- **Health check**: `/_stcore/health`

To deploy, create a Blueprint from this repository in the Render dashboard. The `name` in `render.yaml` (and `region`, if not Oregon) must match the existing service for the Blueprint to manage it rather than create a new one.

## 📝 Notes

- Emoji prefixes in page filenames control sidebar order and icons
- Streamlit auto-generates navigation from the `pages/` folder

## 📄 License

MIT License
