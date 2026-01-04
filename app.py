import streamlit as st
import pandas as pd
import string
import nltk

from rank_bm25 import BM25Okapi
from nltk.corpus import stopwords

# -----------------------
# Setup
# -----------------------
nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))

st.set_page_config(
    page_title="Spotify Lyric Search",
    layout="centered"
)

# -----------------------
# Text Cleaning
# -----------------------
def clean_text(text):
    text = str(text).lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    tokens = [w for w in tokens if w not in stop_words]
    return tokens

# -----------------------
# Load Model (Cached)
# -----------------------
@st.cache_resource
def load_model():
    data = pd.read_csv("spotify_song_dataset.csv")
    data.dropna(subset=["text"], inplace=True)

    data["tokenized_lyrics"] = data["text"].apply(clean_text)
    corpus = data["tokenized_lyrics"].tolist()

    bm25 = BM25Okapi(corpus)
    return data, bm25

# -----------------------
# Search Function
# -----------------------
def search_lyrics(query, data, bm25, top_k):
    query_tokens = clean_text(query)
    scores = bm25.get_scores(query_tokens)

    top_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "Artist": data.iloc[idx]["artist"],
            "Song": data.iloc[idx]["song"],
            "Score": round(scores[idx], 2)
        })

    return results

# -----------------------
# UI
# -----------------------
st.title("Spotify Lyric Search")
st.caption("Find the exact song & artist from a lyric snippet")

data, bm25 = load_model()

# Search settings
with st.expander("Search settings"):
    top_k = st.slider("Number of results", 1, 10, 3)

query = st.text_area(
    "Enter lyrics snippet",
    placeholder="search lyrics...",
    height=100
)

if st.button("🔍 Search"):
    if not query.strip():
        st.warning("Please enter a lyric snippet.")
    else:
        results = search_lyrics(query, data, bm25, top_k)

        st.success(f"✅ Top {len(results)} result(s)")
        for r in results:
            st.markdown(
                f"**{r['Song']}** by *{r['Artist']}*  \nSimilarity Score: `{r['Score']}`"
            )

st.caption(f"Dataset size: {len(data)} songs indexed")
