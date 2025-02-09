"""
This module contains the definitions of tasks assigned to AI agents.
Each task represents a specific step in the content creation process.
"""

from crewai import Task
from agents import create_planner_agent, create_writer_agent, create_editor_agent

def create_planning_task() -> Task:
    """Creates a planning task for content research and outline."""
    return Task(
        description="""
        1. Prioritize the latest trends, key players, and noteworthy news on {topic}.
        2. Identify the target audience, considering their interests and pain points.
        3. Develop a detailed content outline including an introduction, key points, and a call to action.
        4. Include SEO keywords and relevant data or sources.
        """,
        expected_output="""A comprehensive content plan document with an outline,
                        audience analysis, SEO keywords, and resources.""",
        agent=create_planner_agent()
    )

def create_writing_task() -> Task:
    """Creates a writing task for content creation."""
    return Task(
        description="""
        1. Use the content plan to craft a compelling blog post on {topic}.
        2. Incorporate SEO keywords naturally.
        3. Sections/Subtitles are properly named in an engaging manner.
        4. Ensure the post is structured with an engaging introduction,
           insightful body, and a summarizing conclusion.
        5. Proofread for grammatical errors and alignment with the brand's voice.
        """,
        expected_output="""A well-written blog post in markdown format,
                        ready for publication, each section should have 2 or 3 paragraphs.""",
        agent=create_writer_agent()
    )

def create_editing_task() -> Task:
    """Creates an editing task for content refinement."""
    return Task(
        description="""Proofread the given blog post for grammatical errors
                    and alignment with the brand's voice.""",
        expected_output="""A well-written blog post in markdown format,
                        ready for publication, each section should have 2 or 3 paragraphs.""",
        agent=create_editor_agent()
    ) 