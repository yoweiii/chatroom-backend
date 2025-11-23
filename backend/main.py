from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS：讓 Vercel 前端可呼叫 API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 聊天記錄
chat_history = []

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    user_msg = req.message
    chat_history.append({"role": "user", "msg": user_msg})

    # 假 AI 回覆（如果你要串 GPT，我也能幫你加）
    bot_msg = f"AI 回覆：{user_msg}"
    chat_history.append({"role": "bot", "msg": bot_msg})

    return {
        "reply": bot_msg,
        "history": chat_history
    }

@app.get("/")
def root():
    return {"message": "FastAPI Backend Ready!"}
