import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("gemini_api_key")

loader = WebBaseLoader("https://www.oilandgasiq.com/oil-gas/articles/the-top-10-oil-gas-companies-in-2025")
docs = loader.load()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

prompt = PromptTemplate.from_template("""
Extract only the names of the top oil and gas companies mentioned in the following article. 
Do not include any other information, explanations, or text. Return them as a list.

Article:
{article}
""")

chain = prompt | llm | StrOutputParser()

output = chain.invoke({"article": docs[0].page_content})
print(output)
