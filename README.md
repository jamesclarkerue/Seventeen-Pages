# 📚 Seventeen Pages

AI-powered manuscript editing web application by Seventeen & Willow Press. Helps authors refine their stories through four professional editing modes — **Manuscript Critique**, **Line Edit**, **Copyedit**, and **Proofread**.

## 🎯 Overview

Seventeen Pages combines the power of GPT-4 AI with professional editing expertise to provide authors with instant, high-quality feedback on their manuscripts. Whether you need big-picture story advice or final proofreading, our four editing modes have you covered.

## ✨ Features

### Four Professional Editing Modes

1. **📖 Manuscript Critique**
   - High-level story and structure analysis
   - Character development feedback
   - Plot and pacing observations
   - Strengths and areas for improvement

2. **✍️ Line Edit**
   - Sentence-level improvements
   - Word choice and language effectiveness
   - Flow and readability enhancements
   - Voice and tone consistency

3. **📝 Copyedit**
   - Grammar and syntax corrections
   - Style and formatting consistency
   - Punctuation and capitalization
   - Clarity and precision checks

4. **🔍 Proofread**
   - Spelling error detection
   - Typo and formatting issues
   - Final polish and corrections
   - Line-by-line error identification

## 🏗️ Architecture

- **Frontend**: Next.js 14 with React 18
- **Backend**: FastAPI (Python)
- **AI Engine**: OpenAI GPT-4
- **API**: RESTful endpoints with CORS support

## 🚀 Quick Start

### Prerequisites

- Node.js 18 or higher
- Python 3.8 or higher
- OpenAI API key

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_actual_api_key_here
```

5. Start the backend server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

## 📖 Usage

1. **Select an Editing Mode**: Choose from Manuscript Critique, Line Edit, Copyedit, or Proofread
2. **Paste Your Manuscript**: Enter the text you want to edit in the text area
3. **Get AI Feedback**: Click the submit button to receive professional editing feedback
4. **Review Results**: Read through the detailed feedback and suggestions

## 🔗 API Endpoints

### `GET /`
Get API information and available modes

### `GET /health`
Health check endpoint

### `GET /api/modes`
Get detailed information about all editing modes

### `POST /api/edit`
Submit manuscript for editing

**Request Body:**
```json
{
  "text": "Your manuscript text here",
  "mode": "critique" // or "line_edit", "copyedit", "proofread"
}
```

**Response:**
```json
{
  "mode": "critique",
  "original_text": "Your manuscript text",
  "feedback": "Detailed AI feedback...",
  "suggestions": ["Suggestion 1", "Suggestion 2", ...]
}
```

## 📚 API Documentation

Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🛠️ Development

### Project Structure

```
Seventeen-Pages/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example         # Environment template
│   └── README.md
├── frontend/
│   ├── app/
│   │   ├── layout.js        # Root layout
│   │   ├── page.js          # Main page component
│   │   ├── page.module.css  # Page styles
│   │   └── globals.css      # Global styles
│   ├── package.json
│   ├── next.config.js
│   └── README.md
├── .gitignore
└── README.md
```

### Building for Production

**Frontend:**
```bash
cd frontend
npm run build
npm start
```

**Backend:**
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 License

Copyright © 2024 Seventeen & Willow Press. All rights reserved.

## 💖 About

Seventeen Pages is built with ❤️ to help authors refine every page with heart and precision.

---

**Seventeen & Willow Press** - Where stories come to life.
