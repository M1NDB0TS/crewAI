# Import necessary packages and modules
import os
import logging
from logging.handlers import RotatingFileHandler
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
import markdown2  # Assuming markdown2 for Markdown processing

# Setup advanced logging to capture all messages in a log file and errors in the console
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_file = 'crewai_activity.log'

logging.basicConfig(level=logging.DEBUG, format=log_format, handlers=[
    RotatingFileHandler(log_file, maxBytes=1024*1024*5, backupCount=5),
    logging.StreamHandler()
])

# Adjust the stream handler to only display ERROR and above levels on the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(logging.Formatter(log_format))
logging.getLogger('').addHandler(console_handler)

logger = logging.getLogger(__name__)

# Initialize the LLM with 'openhermes' model for language tasks
logger.debug("Initializing the Ollama LLM with model 'openhermes'.")
ollama_llm = Ollama(model="openhermes")

# Initialize DuckDuckGo search tool for information gathering
logger.debug("Initializing DuckDuckGo Search tool for web searches.")
search_tool = DuckDuckGoSearchRun()

# Venue Search Agent Configuration
logger.debug("Configuring Venue Search Agent.")
venue_search_agent = Agent(
    role='Venue Search Agent',
    tools=[search_tool],
    llm=ollama_llm,
    goal='Search for venues in Roseburg, Oregon, and compile preliminary details.',
    backstory='Specialized in discovering local venues using web searches.',
    verbose=True
)

# Data Processing Agent Configuration
logger.debug("Configuring Data Processing Agent.")
data_processing_agent = Agent(
    role='Data Processing Agent',
    tools=[],
    llm=ollama_llm,
    goal='Structure the venue data for markdown formatting.',
    backstory='Focuses on refining and structuring information.',
    verbose=True
)

# Markdown Formatting Agent Configuration
logger.debug("Configuring Markdown Formatting Agent.")
markdown_formatting_agent = Agent(
    role='Markdown Formatting Agent',
    tools=[],
    llm=ollama_llm,
    goal='Format structured data into a Markdown file.',
    backstory='Specializes in data presentation in Markdown format.',
    verbose=True
)

# Crew Configuration and Task Setup
logger.debug("Configuring Crew and tasks.")
crew = Crew(
    agents=[venue_search_agent, data_processing_agent, markdown_formatting_agent],
    tasks=[
        Task(description='Gather venue data from Roseburg, Oregon.', agent=venue_search_agent),
        Task(description='Refine and organize the gathered data.', agent=data_processing_agent),
        Task(description='Convert processed data into a Markdown file.', agent=markdown_formatting_agent)
    ],
    process=Process.sequential,
    verbose=True
)

# Execute the Crew tasks
logger.debug("Kicking off the Crew tasks.")
result = crew.kickoff()

# Check and print the result
if isinstance(result, str) and result.endswith('.md'):
    logger.info(f"Markdown file generated at: {result}")
else:
    logger.error("An error occurred during Markdown file generation.")
