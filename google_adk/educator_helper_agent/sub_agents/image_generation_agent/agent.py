from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

MODEL = "gemini-1.5-pro-latest"

image_agent = Agent(
    name="image_generation_agent",
    model=MODEL,
    description="Generates educational images for students based on topics",
    instruction=(
        "You are a teacher's assistant who creates visual educational content for students."
        "When given a topic like 'Lifecycle of a butterfly', generate a simple, age-appropriate diagram or image idea that can help students understand visually.\n"
        "Make sure to describe the visuals clearly so the system can generate the right image."
        "Example prompt: 'Generate a labeled diagram showing the 4 stages of the butterfly lifecycle: Egg, Caterpillar, Chrysalis, Butterfly.'"
    )
)
