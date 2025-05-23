from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from chatbot_popu import load_popu_chain
from chatbot_eco import load_eco_chain

# Gunakan lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    global popu_chain, eco_chain
    try:
        popu_chain = load_popu_chain()
        print("✅ popu_chain loaded")
        eco_chain = load_eco_chain()
        print("✅ eco_chain loaded")
    except Exception as e:
        print(f"❌ Error loading chains: {e}")
    yield
    print("🛑 App shutting down")

# Inisialisasi app dengan lifespan
app = FastAPI(lifespan=lifespan)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan domain spesifik di produksi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema query
class Query(BaseModel):
    question: str

# Endpoint untuk Popu
@app.post("/chat/popu")
def chat_popu(q: Query):
    try:
        result = popu_chain.run(q.question)
        if not result:
            return {"result": "Maaf, tidak ada jawaban yang tersedia untuk saat ini."}
        return {"result": str(result)}
    except Exception as e:
        print(f"❌ Error di endpoint /chat/popu: {e}")
        return {"result": f"Terjadi kesalahan pada server: {str(e)}"}

# Endpoint untuk Eco
@app.post("/chat/eco")
def chat_eco(q: Query):
    try:
        result = eco_chain.run(q.question)
        if not result:
            return {"result": "Maaf, tidak ada jawaban yang tersedia untuk saat ini."}
        return {"result": str(result)}
    except Exception as e:
        print(f"❌ Error di endpoint /chat/eco: {e}")
        return {"result": f"Terjadi kesalahan pada server: {str(e)}"}

