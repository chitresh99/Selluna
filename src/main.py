from fastapi import FastAPI
from services.sales_pitch.sales_pitch_generator import pitch_generator,User
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class UserPromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Welcome to Selluna"}

@app.post("/selly")
def selly(user_request: UserPromptRequest):
    try:
        user_prompt = User(prompt=user_request.prompt)
        result = pitch_generator(user_prompt)        
        return result
    except Exception as e:
        print(f"Something went wrong: {e}")

@app.get("/health")
def health_check():
    return {"status": "healthy"}