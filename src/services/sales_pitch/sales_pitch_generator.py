import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from config.config import DEEPSEEK_OPEN_ROUTER_API
from services.sales_pitch.system_prompt import SALES_PITCH_GEN_PROMPT


class User(BaseModel):
    prompt: str


system = SALES_PITCH_GEN_PROMPT


def pitch_generator(user_prompt: User):
    try:
        request = user_prompt.prompt

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=DEEPSEEK_OPEN_ROUTER_API,
        )

        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3.1:free",
            messages=[
                {
                    "role": "system",
                    "content": system,
                },
                {"role": "user", "content": request},
            ],
            temperature=0.7,
            max_tokens=2000,
        )
        
        response = completion.choices[0].message.content
        return {
            "message": "Sales pitch generated successfully",
            "pitch": response
        }

    except Exception:
        print("Something went wrong")
