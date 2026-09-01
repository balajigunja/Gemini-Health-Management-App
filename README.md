# Gemini-Health-Management-App
# 🍎 Gemini Health Management App

A Streamlit-based application that uses **Google Gemini Flash models** to analyze food images and estimate calorie intake.  
The app allows users to upload an image of food, provide a text prompt, and receive a structured breakdown of calories per item along with the total calories.

---

## 🚀 Features
- Upload food images (`jpg`, `jpeg`, `png`)
- Text prompt input for custom instructions
- Uses **Google Gemini 3.5 Flash Lite** (via Generative AI API)
- Outputs structured calorie breakdown and total calories
- Simple Streamlit UI

---

## 📂 Project Structure
.
├── health.py          # Main Streamlit app
├── .env               # Environment variables (API key)
├── requirements.txt   # Python dependencies
└── README.md          # Documentation

Code

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/<balajigunja>/<Gemini-Health-Management-App>.git
cd <repo-name>
2. Create a virtual environment
bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
3. Install dependencies
bash
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the root directory:

env
GOOGLE_API_KEY=your_api_key_here
🔑 Get your API key from Google AI Studio.
Make sure the Generative Language API is enabled in your Google Cloud project and billing is active.

▶️ Running the App
bash
streamlit run health.py
Open the app in your browser at http://localhost:8501.

🧩 Workflow
User uploads an image of food items.

Streamlit displays the image for confirmation.

Prompt is prepared (nutritionist-style instructions).

Gemini API is called with:

Text prompt

Uploaded image (converted to bytes)

User input text

Gemini returns structured response with calorie breakdown.

Streamlit displays the response in the app.

📦 Requirements
Add this to requirements.txt:

Code
streamlit
python-dotenv
google-generativeai
Pillow
📝 Example Output
Code
1. Apple - 95 calories
2. Banana - 105 calories
3. Sandwich - 250 calories
---
Total Calories: 450
⚠️ Notes
Ensure your API key has Gemini model access (403 errors mean project permissions/billing issues).

Current model used: gemini-3.5-flash-lite. You can swap to gemini-3.6-flash if enabled in your project.

Streamlit must be run inside the virtual environment where dependencies are installed.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
