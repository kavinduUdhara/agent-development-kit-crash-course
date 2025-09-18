from google.adk.agents import Agent
from .sub_agents.make_vision.agent import make_vision
root_agent = Agent(
    name="manager",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash-exp",
    # model="gemini-2.0-flash",
    description="Greeting Agent",
    instruction="""
    you are a helpful agent

    if user aked you to make a vision, then use make_vision agent
    You are responsible for delegating tasks to the following agent:
    - smake_vision
    """,
    sub_agents=[make_vision],
    tools=[]
)
