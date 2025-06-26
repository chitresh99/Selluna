# * Definition & scope of the sector
# * TAM/SAM estimates (if available via scraping or static data)
# * Summary of recent events (M\&A, regulations, trends)Strongly recommended
from langchain_community.tools import DuckDuckGoSearchResults

sector_name = "Oil and gas"

tool = DuckDuckGoSearchResults()

query=f"what is the definition and scope of {sector_name} sector"

reponse = tool.invoke({"args": {"query":query}, "id": "1", "name": tool.name, "type": "tool_call"})

print(reponse)
