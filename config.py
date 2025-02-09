"""
Configuration settings for the Research Agent application.
"""

import os
from utils import get_openai_api_key
from typing import Dict, List

# LLM Configuration
AVAILABLE_MODELS: Dict[str, Dict[str, str]] = {
    "OpenAI GPT-3.5": {
        "type": "openai",
        "model": "gpt-3.5-turbo",
        "requires_key": True
    },
    "Local Ollama Llama2": {
        "type": "local",
        "model": "ollama/llama2",
        "url": "http://localhost:11434/v1",
        "requires_key": False
    },
    "Local Ollama Mistral": {
        "type": "local",
        "model": "ollama/mistral",
        "url": "http://localhost:11434/v1",
        "requires_key": False
    },
    "Local Ollama DeepSeek": {
        "type": "local",
        "model": "ollama/deepseek-r1:7b",
        "url": "http://localhost:11434",
        "requires_key": False
    }
}

DEFAULT_MODEL = "OpenAI GPT-3.5"

# OpenAI Configuration
OPENAI_API_KEY = get_openai_api_key()

# Streamlit UI Configuration
PAGE_TITLE = "Research Agent"
PAGE_LAYOUT = "wide"
SIDEBAR_HEADER = "Research Settings"
TOPIC_PLACEHOLDER = "e.g., Artificial Intelligence"
GENERATE_BUTTON_TEXT = "Generate Research"
MODEL_SELECTOR_LABEL = "Select AI Model"
API_KEY_LABEL = "OpenAI API Key"

# Export all configuration variables
__all__ = [
    'PAGE_TITLE',
    'PAGE_LAYOUT',
    'SIDEBAR_HEADER',
    'TOPIC_PLACEHOLDER',
    'GENERATE_BUTTON_TEXT',
    'MODEL_SELECTOR_LABEL',
    'API_KEY_LABEL',
    'AVAILABLE_MODELS',
    'DEFAULT_MODEL',
    'get_model_config',
    'setup_environment'
]

def get_model_config(model_name: str) -> Dict[str, str]:
    """Get the configuration for a specific model."""
    return AVAILABLE_MODELS.get(model_name, AVAILABLE_MODELS[DEFAULT_MODEL])

def setup_environment(model_name: str, api_key: str = None) -> None:
    """Setup environment variables based on selected model."""
    model_config = get_model_config(model_name)
    
    if model_config["type"] == "openai":
        os.environ["OPENAI_API_KEY"] = api_key or OPENAI_API_KEY
        os.environ["OPENAI_MODEL_NAME"] = model_config["model"]
    elif model_config["type"] == "local":
        os.environ["OPENAI_API_BASE"] = model_config["url"]
        os.environ["OPENAI_API_KEY"] = "not-needed"
        os.environ["OPENAI_MODEL_NAME"] = model_config["model"] 