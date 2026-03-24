from a2a.server.events import EventQueue # type: ignore
from a2a.server.tasks import TaskUpdater # type: ignore
from agents.website_builder.agent import WebsiteBuilder # type: ignore
from a2a.server.agent_execution import AgentExecutor, RequestContext 
from a2a.utils import (
    new_task
)

class WebsiteBuilderAgentExecutor(AgentExecutor):
    """
    Implements the AgentExecutor interface tto integrate the website builder simple with the a2a framework.  
    """
    def __init__(self):
        self.agent = WebsiteBuilder()

    async def execute(self, context = RequestContext, event_quque = EventQueue) -> None:
        """
        Executes the website builder agent with the given context and event queue.
        """
        query = context.get_user_input.get()
        task = context.current_task
        if not task:
            task = new_task(context.message)
            await event_quque.enqueue_event(task)

        updater = TaskUpdater(event_quque, task.id, task.contextId)

        