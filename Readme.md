# Digital Resume - Multi-Page Streamlit App

A modern, multi-page digital resume built with Streamlit featuring a dark Solarized theme.

## 🚀 Features

- **Home Page**: Overview, work history, skills, and contact information
- **Certifications Page**: Professional certifications with Credly integration and PDF certificate support
- **Projects Page**: Portfolio organized by category (Featured, Professional, Automation, Personal)

## 📁 Project Structure

```
digital-resume/
├── Home.py                         # Main landing page (entry point)
├── pages/
│   ├── 1_📜_Certifications.py      # Certifications & credentials
│   └── 2_🚀_Projects.py            # Project portfolio
├── static/
│   ├── assets/
│   │   ├── Daniel_Cooke_CV.pdf     # Your resume PDF
│   │   ├── profile-pic.png         # Profile picture
│   │   └── certs/                  # PDF certificates folder
│   │       └── (place PDF certs here)
│   └── styles/
│       └── main.css                # Custom CSS styling
├── .streamlit/
│   └── config.toml                 # Streamlit theme configuration
├── requirements.txt
└── README.md
```

## 🛠️ Setup

1. **Install dependencies**
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

To add PDF certificates that can be downloaded from the Certifications page:

1. Place the PDF file in `static/assets/certs/`
2. The file will automatically appear in the "Additional Certificates" section
3. Or, add it to a specific certification entry in the `certifications` list in `pages/1_📜_Certifications.py`:
   ```python
   {
       "name": "Your Cert Name",
       "issuer": "Issuing Organization",
       "date": "2024",
       "description": "Description here",
       "skills": ["Skill1", "Skill2"],
       "badge_color": "#FF5733",
       "verify_link": "https://verify-link.com",
       "pdf_file": "your_cert.pdf"  # filename in static/assets/certs/
   }
   ```

## 🎨 Customization

### Theme
Edit `.streamlit/config.toml` to change colors:
- `primaryColor`: Accent color (#d33682 - magenta)
- `backgroundColor`: Main background (#002b36 - dark blue)
- `secondaryBackgroundColor`: Sidebar (#586e75 - gray)
- `textColor`: Text color (#fff - white)

### Content
- **Home Page**: Update `Home.py` with your info
- **Certifications**: Edit `pages/1_📜_Certifications.py`
- **Projects**: Edit `pages/2_🚀_Projects.py`

## 🌐 Deployment

### Render
1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `streamlit run Home.py --server.port $PORT`

### Container image (luwah-k3s)

The app also builds as a container image for the homelab cluster.

- `Dockerfile` runs `streamlit run Home.py` as a non-root user on port 8501.
- `.github/workflows/build-image.yml` builds it on every pull request and smoke
  tests it under the same restrictions the pod runs with (read-only root
  filesystem, no capabilities). Pushing a tag like `v0.1.0` also pushes
  `ghcr.io/luwalekeah/digital-resume:v0.1.0`.
- Deploying is a change to the image tag in the `luwah-k3s` repo, not a push here.

### Streamlit Cloud
1. Push to GitHub
2. Connect at share.streamlit.io
3. Set main file as `Home.py`

## 📝 Notes

- Emoji prefixes in page filenames control sidebar order and icons
- Streamlit auto-generates navigation from the `pages/` folder
- All pages share the theme from `config.toml`

## 📄 License

MIT License
