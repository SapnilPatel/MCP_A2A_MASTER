from a2a.types import AgentSkill, AgentCard, AgentCapabilities
import click

@click.command()
@click.option('--host', default='localhost', help='Host to run the agent server')
@click.option('--port', default=10000, help='Port to run the agent server')
def main(host: str, port: int):
    skill = AgentSkill(
        id = "website_builder_skill",
        name="Website Builder_skill",
        description="A website builder agent that can create a website based on user requirements. and is built using Google's agent development kit (ADK).",
        tags=["website", "builder", "html", "css", "javascript"],
        examples=[
            """{create a website for a local bakery that includes a homepage, menu page, and contact page. The website should have a warm and inviting design with images of baked goods and a color scheme that reflects the bakery's brand.}""",
            """{build a personal portfolio website for a graphic designer. The website should include sections for the designer's work, an about page, and a contact form. The design should be modern and visually appealing, with a focus on showcasing the designer's creativity and skills.}""",
            """{create a website for a fitness trainer that includes a homepage, services page, and blog. The website should have a clean and professional design with a color scheme that reflects the trainer's brand. The homepage should include a call-to-action for potential clients to book a consultation, and the services page should provide detailed information about the trainer's offerings. The blog should feature articles on fitness tips and success stories from the trainer's clients.}""",        
        ]
    )

    agent_card = AgentCard(
        name = "Website Builder Agent",
        description = "A website builder agent that can create a website based on user requirements. and is built using Google's agent development kit (ADK).",
        skills = [skill],
        url="http://{host}:{port}/",
        version="1.0.0",
        default_input_modes=["text"],
        default_output_modes=["text"],
        capabilities=AgentCapabilities(streaming=True)
    )