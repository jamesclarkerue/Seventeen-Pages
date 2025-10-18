"""
Seventeen Pages - AI-Powered Manuscript Editing API
Backend service providing four editing modes for authors.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Seventeen Pages API",
    description="AI-powered manuscript editing with four professional editing modes",
    version="1.0.0"
)

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")


class ManuscriptRequest(BaseModel):
    """Request model for manuscript editing."""
    text: str
    mode: str  # "critique", "line_edit", "copyedit", "proofread"
    

class EditResponse(BaseModel):
    """Response model for editing results."""
    mode: str
    original_text: str
    feedback: str
    suggestions: list[str] = []


# System prompts for each editing mode
EDITING_PROMPTS = {
    "critique": """You are a professional manuscript critique editor. Analyze the provided text and provide:
1. Overall story assessment
2. Character development feedback
3. Plot structure analysis
4. Pacing and flow observations
5. Strengths and areas for improvement
Be constructive, specific, and encouraging.""",
    
    "line_edit": """You are a professional line editor. Focus on:
1. Sentence structure and flow
2. Word choice and language effectiveness
3. Paragraph transitions
4. Voice and tone consistency
5. Clarity and readability
Provide specific suggestions for improvement while preserving the author's voice.""",
    
    "copyedit": """You are a professional copyeditor. Check for:
1. Grammar and syntax errors
2. Punctuation and capitalization
3. Consistency in style and formatting
4. Factual accuracy
5. Clarity and precision
Flag issues and suggest corrections.""",
    
    "proofread": """You are a professional proofreader. Identify:
1. Spelling errors
2. Typos and formatting issues
3. Punctuation mistakes
4. Missing or repeated words
5. Final polish items
List all errors found with line references."""
}


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Seventeen Pages API",
        "version": "1.0.0",
        "description": "AI-powered manuscript editing service",
        "modes": ["critique", "line_edit", "copyedit", "proofread"]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/api/edit", response_model=EditResponse)
async def edit_manuscript(request: ManuscriptRequest):
    """
    Edit manuscript text using AI based on the selected mode.
    
    Modes:
    - critique: High-level story and structure feedback
    - line_edit: Sentence-level improvements
    - copyedit: Grammar, style, and consistency checks
    - proofread: Final error detection and corrections
    """
    if request.mode not in EDITING_PROMPTS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid mode. Choose from: {list(EDITING_PROMPTS.keys())}"
        )
    
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )
    
    try:
        # Call OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": EDITING_PROMPTS[request.mode]},
                {"role": "user", "content": f"Please review this manuscript text:\n\n{request.text}"}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        feedback = response.choices[0].message.content
        
        # Parse suggestions from feedback (simplified)
        suggestions = []
        for line in feedback.split('\n'):
            if line.strip() and (line.strip().startswith('-') or line.strip().startswith('•')):
                suggestions.append(line.strip().lstrip('-•').strip())
        
        return EditResponse(
            mode=request.mode,
            original_text=request.text,
            feedback=feedback,
            suggestions=suggestions[:10]  # Limit to top 10 suggestions
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )


@app.get("/api/modes")
async def get_modes():
    """Get available editing modes with descriptions."""
    return {
        "modes": [
            {
                "id": "critique",
                "name": "Manuscript Critique",
                "description": "High-level feedback on story, characters, plot, and pacing"
            },
            {
                "id": "line_edit",
                "name": "Line Edit",
                "description": "Sentence-level improvements for flow, clarity, and voice"
            },
            {
                "id": "copyedit",
                "name": "Copyedit",
                "description": "Grammar, style, consistency, and accuracy checks"
            },
            {
                "id": "proofread",
                "name": "Proofread",
                "description": "Final error detection including spelling, typos, and punctuation"
            }
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
