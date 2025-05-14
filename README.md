<h1 align="center">🇮🇳 India Cultural Heritage API</h1>
<p align="center">
  <i>A FastAPI project to explore India's rich cultural legacy through data.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/fastapi-0.110+-brightgreen" />
  <img src="https://img.shields.io/badge/python-3.10+-blue" />
  <img src="https://img.shields.io/github/license/yourusername/india-heritage-api" />
</p>

---

## 📚 Project Overview

This API provides structured and searchable access to:

- 🏛️ **Historical Sites** – Monuments, temples, and landmarks recognized by UNESCO and ASI  
- 🎭 **Cultural Events** – Festivals, fairs, and regional celebrations  
- 🎨 **Art Installations** – Public art, urban sculptures, and mural districts  
- 🧶 **Local Traditions** – Folk arts, oral history, and intangible heritage

Perfect for travel apps, cultural guides, academic tools, or museum kiosks.

---

## 🚀 Getting Started

<details>
<summary><b>Step-by-step setup</b></summary>

1. **Clone the repository**
   git clone https://github.com/yourusername/india-heritage-api.git
   cd india-heritage-api

2. **Install dependencies**
    pip install -r requirements.txt
    
3. **Run the server**
    uvicorn main:app --reload --port 8801

4. **Access your API**
    Root: http://localhost:8801

    Swagger Docs: http://localhost:8801/docs

    Redoc: http://localhost:8801/redoc

</details>
🧭 API Routes
Endpoint	Method	Description
/sites/	GET	Returns a list of historical heritage sites
/events/	GET	Lists cultural events and festivals
/art/	GET	Shows public art installations
/traditions/	GET	Displays traditional customs and folk arts
/docs	GET	Interactive Swagger UI

📁 Project Structure
pgsql
Copy
Edit
india-heritage-api/
├── main.py                       # FastAPI app
├── data/
│   ├── historical_sites.json
│   ├── cultural_events.json
│   ├── art_installations.json
│   └── local_traditions.json
├── requirements.txt
└── README.md

<hr><br><br>
Made with ❤️ by [Harsh Gupta]