from typing import AsyncIterable
from google.adk import Runner # type: ignore
from google.adk.agents import LlmAgent
from requests import session  # type: ignore
from utilities.common.file_loader import load_instructions_file 
from google.adk.artifacts import InMemoryArtifactService 
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.genai import types 

class WebsiteBuilder:
    """
    A website builder agent that can create a website based on user requirements. 
    and is built using Google's agent development kit (ADK). 
    """

    def __init__(self):
        self.system_instruction = load_instructions_file("agents/website_builder/instructions.txt")
        self.description = load_instructions_file("agents/website_builder/description.txt")
        self._agent = self._build_agent()
        self._user_id = "website_builder_user"
        self.runner = Runner(
            app_name = self._agent_name,
            agent = self._agent,
            artifact_service=InMemoryArtifactService(),
            session_service=InMemorySessionService(),
            memory_service=InMemoryMemoryService()
        )

    def _build_agent(self)->LlmAgent:
        return LlmAgent(
            name = "Website_Builder",
            model = "gemini-2.5-flash",
            instruction=self.system_instruction,
            description=self.description,
        )
    
    async def invoke(self, query: str, session_id: str)-> AsyncIterable[dict]:
        """
        Invoke the agent 
        Return a stream of updates back to the caller as agent process the query

        {
            'is_task_complete': bool, # indicates if the agent has completed processing the query
            'updates': str, # intermediate updates from the agent while processing the query
            'content': str # final content/result from the agent after processing the query
        }
        """
        session = await self._runner.session_service.get_session(
            app_name=self._agent.name,
            session_id=session_id,
            user_id=self._user_id    
        )

        if not session:
            session = await self._runner.session_service.create_session(
                app_name=self._agent.name,
                session_id=session_id,
                user_id=self._user_id
            )
        
        user_content = types.Content(
            role = "user",
            parts = [types.Part.from_text(text=query)]
        )

        async for event in self._runner.run_async(
            user_id = self._user_id,
            session_id = session_id,
            new_messages = user_content
        ):
            if event.is_final_response:
                final_response = ""
                if event.contgent and event.content.parts and event.content.parts[-1].text:
                    final_response = event.content.parts[-1].text

                yield{
                    'is_task_complete': True,
                    'content': final_response
                }
            else:
                yield {
                    'is_task_complete': False,
                    'updates': event.content.parts[-1].text
                }