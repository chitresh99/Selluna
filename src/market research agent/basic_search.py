from langchain_community.tools import DuckDuckGoSearchResults

tool = DuckDuckGoSearchResults()

query='What are the top 10 oil companies by valuation 2025'

reponse = tool.invoke({"args": {"query":query}, "id": "1", "name": tool.name, "type": "tool_call"})

print(reponse)