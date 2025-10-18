# Seventeen Pages Backend

FastAPI backend service for AI-powered manuscript editing.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file:
```bash
cp .env.example .env
```

3. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_actual_key_here
```

## Running the Server

```bash
python main.py
```

Or with uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Editing Modes

1. **Manuscript Critique** - High-level story analysis
2. **Line Edit** - Sentence-level improvements
3. **Copyedit** - Grammar and style checks
4. **Proofread** - Final error detection
