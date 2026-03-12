# 🚗 car-search-telegram-bot

A Telegram bot that helps users find used cars from a MongoDB inventory using natural language keyword matching — no AI APIs required.

---

## 💡 How It Works

User sends a message like:
> *"I need a diesel car under 5 lakh"*

The bot:
1. Extracts filters using keyword matching (`diesel` → fuel type, `5 lakh` → price limit)
2. Queries MongoDB for matching cars with `status: not_sold`
3. Replies with matching car details and photos

---

## 🗂️ Project Structure

```
car-search-telegram-bot/
├── app/
│   ├── config/
│   │   └── settings.py          # Env vars (Mongo URI, Telegram token, etc.)
│   ├── db/
│   │   └── mongo.py             # MongoDB connection
│   ├── filters/
│   │   ├── parser.py            # Keyword extraction from user text
│   │   └── apply.py             # Apply extracted filters to car list
│   └── services/
│       └── car_service.py       # Query MongoDB, return matching cars
├── ingest.py                    # One-time script: local folders → Cloudinary + MongoDB
├── bot.py                       # Telegram bot entry point
├── .env                         # Your secrets (never commit this)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/car-search-telegram-bot.git
cd car-search-telegram-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
TELEGRAM_TOKEN=your_telegram_bot_token
MONGO_URI=mongodb://localhost:27017
DB_NAME=cars_db
COLLECTION_NAME=cars
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 4. Ingest car data into MongoDB

Organise your car folders like this:

```
Cars/
  Ertiga-Vxi-O/
    metadata.json
    images/
      1.jpeg
      2.jpeg
      ...
```

Each `metadata.json` should follow this structure:

```json
{
  "brand": "Maruti",
  "model": "Ertiga",
  "variant": "VXI (O)",
  "year": 2022,
  "fuel_type": "petrol",
  "transmission": "manual",
  "km_driven": 31400,
  "price": 1100000,
  "owner_count": 1,
  "body_type": "MPV",
  "segment": "MPV",
  "seat_count": 7,
  "engine_cc": 1462,
  "mileage_kmpl": 20.5,
  "airbags": 2,
  "tags": ["family_car", "7_seater", "low_km"],
  "description": "Maruti Ertiga VXI(O) petrol 7 seater MPV."
}
```

Then run:

```bash
python ingest.py --cars-dir "C:/path/to/Cars"
```

This uploads images to Cloudinary and inserts each car into MongoDB with `status: not_sold`.

### 5. Run the bot

```bash
python bot.py
```

---

## 🔍 Supported Keyword Filters

| What user says | Filter applied |
|---|---|
| `diesel`, `petrol`, `cng` | `fuel_type` |
| `automatic`, `manual` | `transmission` |
| `under 5L`, `less than 5 lakh`, `below 5 lakh` | `price <` |
| `honda`, `maruti`, `hyundai` | `brand` |
| `sedan`, `hatchback`, `MPV`, `van` | `body_type` |
| `7 seater`, `5 seater` | `seat_count` |
| `low km`, `under 50000 km` | `km_driven` |
| `first owner`, `single owner` | `owner_count` |

---

## 🛠️ Tech Stack

- **Python** — bot logic and ingestion script
- **python-telegram-bot** — Telegram bot framework
- **MongoDB** — car inventory database
- **Cloudinary** — image storage and delivery
- **Keyword Matching** — rule-based NLP filter extraction (no external AI APIs)

---

## 📦 requirements.txt

```
python-telegram-bot==20.7
pymongo==4.6.1
cloudinary==1.36.0
python-dotenv==1.0.0
```

---

## 🚧 Roadmap

- [x] Keyword-based filter extraction
- [x] MongoDB car search
- [x] Cloudinary image storage
- [x] Telegram bot replies with car details
- [ ] Send car photos via Telegram
- [ ] Multi-filter support (e.g. diesel + under 5L + automatic)
- [ ] `/list` command to browse all available cars
- [ ] Mark car as sold via admin command

---

## 📄 License

MIT