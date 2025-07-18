from crewai_tools import WebsiteSearchTool
from dotenv import load_dotenv

load_dotenv()

def get_website_tool(website: str):
    return WebsiteSearchTool(website=website)
