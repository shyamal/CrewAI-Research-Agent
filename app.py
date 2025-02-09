"""
Main application file for the Research Agent.
This Streamlit application generates research content using AI agents.
"""

import streamlit as st
import warnings
from crewai import Crew
from typing import Dict, Any, List
import json

# Import all required configuration
from config import (
    PAGE_TITLE,
    PAGE_LAYOUT,
    SIDEBAR_HEADER,
    TOPIC_PLACEHOLDER,
    GENERATE_BUTTON_TEXT,
    MODEL_SELECTOR_LABEL,
    API_KEY_LABEL,
    AVAILABLE_MODELS,
    DEFAULT_MODEL,
    get_model_config,
    setup_environment
)

from tasks import (
    create_planning_task,
    create_writing_task,
    create_editing_task
)

# Suppress warnings
warnings.filterwarnings('ignore')

def initialize_session_state() -> None:
    """Initialize the session state variables."""
    if 'responses' not in st.session_state:
        st.session_state.responses = []
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = DEFAULT_MODEL

def setup_page_config() -> None:
    """Configure the Streamlit page settings."""
    st.set_page_config(page_title=PAGE_TITLE, layout=PAGE_LAYOUT)
    st.title(PAGE_TITLE)

def create_sidebar() -> Dict[str, Any]:
    """Create and return sidebar elements."""
    with st.sidebar:
        st.header(SIDEBAR_HEADER)
        
        # Model Selection
        selected_model = st.selectbox(
            MODEL_SELECTOR_LABEL,
            options=list(AVAILABLE_MODELS.keys()),
            index=list(AVAILABLE_MODELS.keys()).index(st.session_state.selected_model)
        )
        st.session_state.selected_model = selected_model
        
        # API Key input if required
        api_key = None
        model_config = get_model_config(selected_model)
        if model_config["requires_key"]:
            api_key = st.text_input(API_KEY_LABEL, type="password")
            if not api_key:
                st.warning("Please enter your API key.")
        
        # Topic input and generate button
        topic = st.text_input("Enter your research topic:", 
                            placeholder=TOPIC_PLACEHOLDER)
        
        # Disable button if API key is required but not provided
        button_disabled = model_config["requires_key"] and not api_key
        generate_button = st.button(
            GENERATE_BUTTON_TEXT,
            type="primary",
            disabled=button_disabled
        )
        
        if model_config["type"] == "local":
            st.info(
                "Make sure your local LLM server is running at: " +
                model_config["url"]
            )
        
    return {
        "topic": topic,
        "generate_button": generate_button,
        "api_key": api_key
    }

def generate_research(topic: str) -> Dict[str, str]:
    """Generate research content using AI agents.
    
    Args:
        topic: The research topic to generate content about.
    
    Returns:
        Dict[str, str]: Dictionary containing responses from each agent
    """
    # Create individual tasks to capture each agent's response
    planner_task = create_planning_task()
    writer_task = create_writing_task()
    editor_task = create_editing_task()
    
    crew = Crew(
        agents=[],  # Agents are created within tasks
        tasks=[planner_task, writer_task, editor_task],
        verbose=True
    )
    
    result = crew.kickoff(inputs={"topic": topic})
    
    # Extract individual responses
    return {
        "planner": planner_task.output if hasattr(planner_task, 'output') else "No response",
        "writer": writer_task.output if hasattr(writer_task, 'output') else "No response",
        "editor": result.raw  # Final edited content
    }

def display_responses() -> None:
    """Display all generated research responses in tabs."""
    st.header("Generated Research")
    
    for idx, response in enumerate(reversed(st.session_state.responses)):
        with st.expander(
            f"Research: {response['topic']} (using {response.get('model', DEFAULT_MODEL)})", 
            expanded=(idx == 0)
        ):
            # Create tabs for each agent's response
            planner_tab, writer_tab, editor_tab = st.tabs([
                "Content Planner", 
                "Content Writer", 
                "Editor"
            ])
            
            with planner_tab:
                st.markdown("### Content Plan")
                st.markdown(response['content'].get('planner', 'No planner response available'))
            
            with writer_tab:
                st.markdown("### Initial Draft")
                st.markdown(response['content'].get('writer', 'No writer response available'))
            
            with editor_tab:
                st.markdown("### Final Edited Version")
                st.markdown(response['content'].get('editor', 'No editor response available'))

    if not st.session_state.responses:
        st.info("Enter a topic and click 'Generate Research' to get started!")

def main() -> None:
    """Main application function."""
    initialize_session_state()
    setup_page_config()
    
    sidebar_elements = create_sidebar()
    topic = sidebar_elements["topic"]
    generate_button = sidebar_elements["generate_button"]
    api_key = sidebar_elements["api_key"]

    if generate_button and topic:
        # Setup environment variables for the selected model
        setup_environment(st.session_state.selected_model, api_key)
        
        with st.spinner(f'Generating research about "{topic}"...'):
            try:
                responses = generate_research(topic)
                st.session_state.responses.append({
                    "topic": topic,
                    "content": responses,
                    "model": st.session_state.selected_model
                })
                st.success("Research generated successfully!")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    display_responses()

if __name__ == "__main__":
    main()
