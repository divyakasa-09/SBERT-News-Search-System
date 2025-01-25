# SBERT-News-Search-System

A  semantic search system leveraging SBERT and ANNOY for efficient article retrieval.

## Tech Stack
- Python 3.8+
- Hugging Face Transformers (via sentence-transformers library)
- SBERT (Sentence-BERT) for embeddings
- ANNOY for approximate nearest neighbor search 
- Flask for API
- Streamlit for UI
- Docker & AWS EC2 for deployment

## Features
- Semantic search across 22,399 news articles
- Fast retrieval using ANNOY indexing
- REST API and Streamlit interface
- Docker containerization
- Cloud deployment support

## Dataset Structure
- article_id: Unique identifier
- category/subcategory: Article classification
- title: Article headline
- published_date: Publication timestamp
- text: Article content
- source: Publication source

## Installation & Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start Flask API
python server.py

# Launch Streamlit UI
streamlit run app.py