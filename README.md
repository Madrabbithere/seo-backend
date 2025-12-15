# SEO Brief Generator - Backend API

A FastAPI backend service that generates comprehensive SEO content briefs using Google's Gemini AI.

## 🚀 Tech Stack

- **FastAPI** - Modern, fast Python web framework
- **Pydantic v2** - Data validation using Python type hints
- **Google Gemini AI** - AI-powered content generation
- **Uvicorn** - Lightning-fast ASGI server

## 📁 Project Structure

```
seo-backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   └── brief.py     # Brief generation endpoint
│   │       └── router.py        # API router
│   ├── core/
│   │   ├── config.py            # Settings management
│   │   └── prompts.py           # AI prompts
│   ├── schemas/
│   │   └── brief.py             # Pydantic models
│   ├── services/
│   │   └── gemini.py            # Gemini API client
│   └── main.py                  # FastAPI app entry
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🛠️ Setup

### Prerequisites

- Python 3.11+
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Mathankrsh/seo-backend.git
cd seo-backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

5. Run the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

#### `POST /api/v1/generate-brief`

Generate an SEO content brief.

**Request Body:**
```json
{
  "title": "Best Running Shoes 2024",
  "target_audience": "Marathon runners aged 25-45",
  "primary_keywords": ["running shoes", "marathon shoes"],
  "secondary_keywords": ["cushioning", "durability"]
}
```

**Response:**
```json
{
  "success": true,
  "brief": {
    "meta_title": "Best Running Shoes 2024 | Top Marathon Shoes",
    "meta_description": "Discover the best running shoes for marathon runners...",
    "h1_suggestion": "The Ultimate Guide to Best Running Shoes",
    "content_outline": ["Introduction", "Key Features", "..."],
    "word_count_recommendation": 2500,
    "keyword_placement_tips": ["Include primary keyword in first 100 words"],
    "internal_linking_suggestions": ["Link to shoe sizing guide"]
  }
}
```

#### `GET /health`

Health check endpoint for deployment monitoring.

## 🚢 Deployment (Railway)

1. Push to GitHub
2. Connect repository to Railway
3. Add environment variables:
   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `ALLOWED_ORIGINS_STR`: Comma-separated allowed origins (e.g., `https://your-app.vercel.app`)
4. Deploy!

## 📄 License

MIT
