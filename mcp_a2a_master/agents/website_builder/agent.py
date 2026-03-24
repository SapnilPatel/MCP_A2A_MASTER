from utilities.common.file_loader import load_instructions_file # type: ignore
from google.adk.agent import LlmAgent # type: ignore

class WebsiteBuilder:
    """
    A website builder agent that can create a website based on user requirements. 
    and is built using Google's agent development kit (ADK). 
    """

    def __init__(self):
        self.system_instruction = load_instructions_file("agents/website_builder/instructions.txt")
        self.description = load_instructions_file("agents/website_builder/description.txt")

    def _build_agent(self)->LlmAgent:
        return LlmAgent(
            name = "Website_Builder",
            model = "gemini-2.5-flash",
            instruction=self.system_instruction,
            description=self.description,
        )