import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()
api_key = os.getenv('mistral_api_key')
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

system = """
You are an expert AI Sales Agent Assistant, trained on the best practices of B2B and B2C sales across industries. Your task is to generate high-converting, persuasive, and personalized sales pitches for sales representatives who handle the entire sales funnel, from outreach to closing.

You will be given a product description and a target customer persona. Based on this, your output should be a complete sales pitch structured for either cold calls, discovery meetings, or follow-up emails. Make sure your pitch:

Establishes relevance and pain points quickly

Positions the product as a solution

Demonstrates ROI or competitive advantage

Includes social proof or testimonials

Has a compelling call-to-action

Is adaptable to different customer segments and tones
"""

question="""
Product Name: LeadGenX
Product Type: SaaS
Product Description: An AI-powered lead generation platform that helps sales reps find, score, and contact high-intent B2B leads using real-time company data.
Industry: B2B SaaS
Target Customer Persona:
  - Name: Lisa
  - Role: VP of Sales
  - Company Size: 100-300 employees
  - Pain Points: Poor lead quality, long sales cycles, SDR burnout
  - Goals: Shorten sales cycles, improve conversion rates
  - Decision-making power: High
Sales Channel: Email
Tone: Data-driven and consultative
Stage: Cold Outreach
Region: North America
Competitors: ZoomInfo, Apollo

"""

chat_response = client.chat.complete(
    model = model,
    messages = [{"role":"system", "content":system}, {"role":"user", "content":question}],
)

print(chat_response.choices[0].message.content)
