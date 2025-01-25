import streamlit as st
from datetime import datetime
import requests

# Page config
st.set_page_config(page_title="News Search", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .search-box {padding: 2rem; background: #f8f9fa; border-radius: 10px;}
    .result-card {padding: 1.5rem; background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);}
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🔍 Semantic News Search Engine")
st.markdown("Powered by SBERT and ANNOY")

# Search interface
with st.container():
    col1, col2 = st.columns([3,1])
    with col1:
        query = st.text_input("", placeholder="Enter your search query...")
    with col2:
        k = st.number_input("Results to show", min_value=1, value=5, max_value=20)

if st.button("Search", type="primary"):
    if not query:
        st.error("Please enter a search query")
    else:
        with st.spinner("Searching..."):
            try:
                response = requests.post(
                    "http://localhost:5001/search",
                    json={"query": query, "k": k}
                )
                results = response.json()["results"]
                
                if results:
                    for result in results:
                        with st.container():
                            st.markdown(f"""
                                <div class='result-card'>
                                    <h3>{result['title']}</h3>
                                    <p>Category: <span class='badge'>{result['category']}</span> 
                                       Subcategory: <span class='badge'>{result['subcategory']}</span></p>
                                    <p>Relevance Score: {result['score']:.2f}</p>
                                </div>
                                """, unsafe_allow_html=True)
                            st.divider()
                else:
                    st.info("No results found")
                    
            except Exception as e:
                st.error(f"Error: {e}")


