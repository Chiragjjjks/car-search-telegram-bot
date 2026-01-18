```md
#  Car RAG Telegram Chatbot

A **Retrieval-Augmented Generation (RAG)** based Telegram chatbot that helps users search for cars using **natural language queries**.  
The bot retrieves **structured car data (price, km, year, fuel, color, etc.) and images strictly from a database** and responds with relevant results via Telegram.
```
##  Use Case

Users can ask queries like:

- **"White car under 5 lakhs"**
- **"Diesel sedan below 1 lakh km"**
- **"Red automatic car"**

The chatbot:
1. Understands the user intent using an **LLM**
2. Converts the query into structured filters
3. Retrieves **only existing car metadata and images from the database**
4. Sends results back to the user via **Telegram Bot API**

**No hallucinated data** — all responses are grounded in the database.

---

## Architecture Overview

```

User (Telegram)
      |
      v
Telegram Bot API
      |
      v
Query Parser (LLM)
      |
      v
Structured Filters (price, color, km, fuel...)
      |
      v
Vector / Metadata Search (RAG)
      |
      v
Database (MongoDB)
      |
      v
Images + Car Metadata
      |
      v  
Telegram Response

```

---

##  Tech Stack

- **Python**
- **Telegram Bot API**
- **LLM (OpenAI / Local LLM)**
- **RAG Pipeline**
- **MongoDB** (car metadata & image paths)
- **FAISS / Vector DB** (optional for semantic search)
- **FastAPI** (optional backend layer)


##  Project Structure
```
Rag-Car-Search/
│
├── bot/
│   ├── telegram_bot.py        # Telegram bot entry point
│   ├── handlers.py            # Message handlers
│
├── rag/
│   ├── query_parser.py        # Converts user text to filters
│   ├── retriever.py           # Retrieves cars from DB
│
├── db/
│   ├── mongo.py               # MongoDB connection
│   ├── schema.py              # Car schema
│
├── data/
│   ├── images/                # Car images
│   ├── cars.json              # Sample car metadata
│
├── utils/
│   ├── normalizer.py          # Text normalization
│
├── .env                       # Environment variables
├── .gitignore
├── requirements.txt
└── README.md

```

## Car Data Schema (Example)

```json
{
  "brand": "Honda",
  "model": "City",
  "year": 2014,
  "fuel": "Diesel",
  "color": "White",
  "km": 99000,
  "price": 425000,
  "ownership": "Second",
  "images": [
    "images/honda_city_1.jpg",
    "images/honda_city_2.jpg"
  ],
  "status": "available"
}
````


## 🔍 Query Flow (RAG Logic)

1. User sends a message via Telegram
2. LLM extracts intent and constraints
3. Query is converted into:

   * Price range
   * Color
   * Fuel type
   * Kilometer limit
4. MongoDB is queried using structured filters
5. Matching car metadata + images are retrieved
6. Results are formatted and sent back to the user

---

## 📸 Telegram Response Example

```
🚗 Honda City (2014)
💰 Price: ₹4,25,000
🛣️ KM Driven: 99,000
⛽ Fuel: Diesel
🎨 Color: White
👤 Owner: Second
```

*(Along with car images)*


## 🚀 How to Run

### 1️ Clone the repo

```bash
git clone https://github.com/Chiragjjjks/Rag-Car-Search.git
cd Rag-Car-Search
```

###  Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3️ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️ Set environment variables

Create `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_token_here
MONGO_URI=mongodb://localhost:27017
```

### 5️ Run the bot

```bash
python bot/telegram_bot.py
```


##  Data Safety

* All responses are **retrieved from database only**
* No generated or fabricated car details
* Images are served from stored paths

---

## Future Enhancements

* Semantic search using FAISS
* Multi-image carousel support
* User preference memory
* Admin dashboard for car uploads
* Multi-language support

---

##  Author

**Chirag S**
AI / ML | Backend | RAG Systems

---

##  Star the Repo

If you find this project useful, please ⭐ the repository!

```

```  
