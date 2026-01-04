# Spotify Lyric Search 🎵

This project is a simple **lyric-based song search application** built using **Python, NLP, and Streamlit**.  
It allows users to enter a snippet of song lyrics and retrieves the most relevant songs using the **BM25 ranking algorithm**.

The project is designed as part of a **Python task submission**.

---

## 📂 Project Structure

Spotify-Lyric-Search/
│
├── app.py # Main Streamlit application
├── spotify_song_dataset.csv # Dataset containing song details
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 📊 Dataset Format

The application expects a local file named `spotify_song_dataset.csv` in the project directory.

The CSV file **must contain the following columns**:

- `artist` – Name of the artist  
- `song` – Song title  
- `text` – Full song lyrics  

Example:

```csv
artist,song,text
Taylor Swift,Lover,We could leave the Christmas lights up till January...

⚙️ Installation Guide 
1️⃣ Prerequisites
Python 3.9 or above

Internet connection (for first-time NLTK setup)

2️⃣ Clone the Repository
git clone https://github.com/Anik-d07/spotify-lyric-search
cd spotify-lyric-search

3️⃣ Install Dependencies
Open a terminal inside the project folder and run:

python -m pip install -r requirements.txt
4️⃣ Run the Application
Use the following command (important):

python -m streamlit run app.py
After running, open the browser link shown in the terminal (usually):

http://localhost:8501

🔍 How the Application Works
Lyrics are preprocessed by:

Lowercasing
Removing punctuation
Removing stopwords
Lyrics are tokenized and indexed using BM25
User enters a lyric snippet
The system ranks and displays the Top-K most relevant songs

🧠 Technologies Used

Python
Streamlit (Web Interface)
NLTK (Text preprocessing)
BM25 (rank-bm25) (Information Retrieval)

Pandas (Data handling)
