"""
This module contains the definitions of AI agents used in the research process.
Each agent has a specific role in the content creation pipeline.
"""

from crewai import Agent

def create_planner_agent() -> Agent:
    """Creates a Content Planner agent responsible for research planning."""
    return Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory="""You're working on planning a blog article about the topic: {topic}.
                  You collect information that helps the audience learn something
                  and make informed decisions. Your work is the basis for
                  the Content Writer to write an article on this topic.""",
        allow_delegation=False,
        verbose=True
    )

def create_writer_agent() -> Agent:
    """Creates a Content Writer agent responsible for article writing."""
    return Agent(
        role="Content Writer",
        goal="Write insightful and factually accurate opinion piece about the topic: {topic}",
        backstory="""You're working on writing a new opinion piece about the topic: {topic}.
                  You base your writing on the work of the Content Planner, who provides
                  an outline and relevant context about the topic. You follow the main
                  objectives and direction of the outline, as provided by the Content Planner.
                  You provide objective and impartial insights and back them up with information
                  provided by the Content Planner. You acknowledge in your opinion piece
                  when your statements are opinions as opposed to objective statements.""",
        allow_delegation=False,
        verbose=True
    )

def create_editor_agent() -> Agent:
    """Creates an Editor agent responsible for content review and refinement."""
    return Agent(
        role="Editor",
        goal="Edit a given blog post to align with the writing style of the organization.",
        backstory="""You are an editor who receives a blog post from the Content Writer.
                  Your goal is to review the blog post to ensure that it follows
                  journalistic best practices, provides balanced viewpoints when
                  providing opinions or assertions, and also avoids major controversial
                  topics or opinions when possible.""",
        allow_delegation=False,
        verbose=True
    ) 