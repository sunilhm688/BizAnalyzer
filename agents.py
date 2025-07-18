from crewai import Agent
from dotenv import load_dotenv
import os
from tools import get_website_tool

load_dotenv()

if "OPENAI_API_KEY" not in os.environ:
    raise EnvironmentError("OPENAI_API_KEY not found. Please set it in Render → Environment")

def analyze_website(website_url: str):
    websearchtool = get_website_tool(website_url)

    website_agent = Agent(
        role="Website Researcher & Business Model Analyst",
        goal=f"Study the website {website_url} and write a concise business model analysis, "
             "including key value propositions, target customers, revenue streams, and partners.",
        backstory="You are an expert business analyst and website researcher, skilled at extracting business models "
                  "from websites and summarizing them effectively.",
        tools=[websearchtool],
        verbose=True
    )

    initial_messages = [
        {
            "role": "user",
            "content": (
                f"Please analyze the website {website_url}. "
                "Write a detailed business model assessment covering the company's value proposition, "
                "target market, key activities, revenue streams, and partnerships based on the website content. "
                "If information is not clearly available, try to make a reasonable assumption based on what the site offers."
            )
        }
    ]

    result = website_agent.kickoff(initial_messages)
    return result.raw
