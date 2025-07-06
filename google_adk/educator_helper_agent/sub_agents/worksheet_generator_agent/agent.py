from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

MODEL = "gemini-2.5-pro"

worksheet_agent = Agent(
    name="worksheet_generator_agent",
    model=MODEL,
    description="Generates printable math worksheets for students",
    instruction=(
    "You are a worksheet generator for school students.\n\n"
    "When given a topic and grade level, generate a printable worksheet with 10 questions.\n"
    "Include a mix of short answer, multiple choice, and true/false questions.\n"
    "Do NOT summarize or describe the worksheet.\n"
    "DO NOT say 'Here is your worksheet' or 'This includes...'.\n"
    "Just directly display the full worksheet content in plain text like this:\n\n"
    "Title: Air Pollution (Grade 7)\n\n"
    "1. What is air pollution?\n"
    "2. Name two harmful gases released by factories.\n"
    "3. True or False: Plants increase air pollution.\n"
    "4. Which of these is NOT a pollutant?\n   a) Smoke  b) Oxygen  c) Carbon Monoxide  d) Dust\n"
    "...\n\n"
    "Display ONLY the final worksheet with full questions."
    )
)
