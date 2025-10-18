# 🌿 Seventeen Pages  
**AI-Powered Manuscript Editing by Seventeen & Willow Press**

---

## ✨ Overview
**Seventeen Pages** is an AI-powered web app that helps authors refine their manuscripts with purpose and clarity.  
Designed for writers of children’s, young adult, and faith-inspired books, it provides four levels of editing:

1. **Manuscript Critique** – Get high-level feedback on story structure, character arcs, and pacing.  
2. **Line Edit** – Improve tone, rhythm, and sentence flow while keeping your unique voice.  
3. **Copyedit** – Catch grammar, punctuation, and consistency issues.  
4. **Proofread** – Perform a final polish for typos and layout irregularities.

Seventeen Pages aims to bridge the gap between expensive professional editing and basic grammar tools, giving authors a compassionate AI editor that preserves meaning and voice.

---

## 🧠 Tech Stack
| Layer | Technology |
|-------|-------------|
| Frontend | [Next.js](https://nextjs.org/) + TypeScript |
| Backend | [FastAPI](https://fastapi.tiangolo.com/) |
| AI Engine | GPT-based LLMs (e.g., OpenAI API) |
| Grammar Layer | [LanguageTool](https://languagetool.org/) |
| Document Handling | python-docx, PyMuPDF |
| Styling | React + CSS Modules |
| Storage | Local / S3 compatible bucket |

---

## ⚙️ Local Setup

### Prerequisites
- Node.js 20+  
- Python 3.10+  
- npm or yarn  
- GitHub Copilot enabled  
- (Optional) OpenAI or Anthropic API key  

### Clone and Install
```bash
git clone https://github.com/<your-username>/seventeen-pages.git
cd seventeen-pages
cd api
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
cd ../web
npm install
npm run dev
seventeen-pages/
│
├── api/              # FastAPI backend
├── web/              # Next.js frontend
├── shared/           # Common schemas and prompt templates
├── README.md
└── LICENSE
