# Shift Group Matching Engine

An internal Streamlit-powered tool designed to help Shift Group match top candidates to open roles based on **skill alignment**, **experience**, and **location fit**. Built to scale Shift Group's placement process with clarity and speed.

---

## 🧰 Features

- Job-specific filtering with **minimum match score threshold**
- Keyword search by **candidate name or skill**
- Custom branded UI using Shift Group’s colors, fonts, and logo
- Instant **CSV export** of matched candidates
- Clean, deployable architecture with easy customization

---

## 📁 Project Structure

```
shiftgroup_matching_project/
├── assets/          # Logo and branding images
├── data/            # Candidate match data (not pushed to repo)
├── notebooks/       # Optional analysis notebooks
├── src/             # Core Streamlit app and logic
├── visuals/         # Optional UI mockups or charts
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/cmwardcode/shiftgroup_matching_project.git
cd shiftgroup_matching_project
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**
```bash
streamlit run src/streamlit_match_demo.py
```

---

## 🌐 Deployment

The app is designed to be deployed to:
- [Streamlit Cloud](https://streamlit.io/cloud)
- AWS EC2 / Lightsail
- Azure App Services
- Heroku (via container)

Environment variables, config, and secrets can be managed via `.streamlit/config.toml` for styling and Streamlit Cloud deployment.

---

## 📌 Notes

- The `data/` folder is excluded from version control for privacy.
- Uses custom `style` overrides for full UI control via embedded CSS.
- Designed with modularity in mind to support future V2 backend upgrades.

---

## 🙋‍♂️ Maintained by

Cassidy Ward  
Built for Shift Group – May 2025
