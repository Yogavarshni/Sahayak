from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from dotenv import load_dotenv
load_dotenv()

from .sub_agents.image_generation_agent.agent import image_agent
from .sub_agents.worksheet_generator_agent.agent import worksheet_agent

MODEL = "gemini-2.0-flash-exp"

root_agent = LlmAgent(
    name="education_helper_agent",
    model=MODEL,
    description="An educational assistant that generates worksheets or visuals",
    instruction=(
        "You are an educational assistant for students and teachers"

        "If the user asks for a diagram, visual explanation, or image (e.g., 'Lifecycle of a butterfly' or 'Show the water cycle'),\n"
        "- Call `image_generation_agent` with a student-friendly version of the request"

        "If the user asks for a worksheet, practice questions, or exercises (e.g., '10 questions on addition' or 'worksheet on fractions'),\n"
        "- Call `worksheet_generator_agent` with the appropriate topic"

        "Do NOT answer directly — always call the correct tool agent."
    ),
    tools=[
        AgentTool(agent=image_agent),
        AgentTool(agent=worksheet_agent)
    ],
)
