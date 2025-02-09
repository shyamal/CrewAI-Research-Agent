# CrewAI Research Agent

A Streamlit-based application that leverages AI agents to generate comprehensive research content on any given topic. This project uses CrewAI to orchestrate multiple AI agents working together to plan, write, and edit research content.

## Features

- 🤖 Multiple AI Agents working in collaboration
- 📝 Three-stage research process: Planning, Writing, and Editing
- 🎯 Support for various AI models
- 🌐 User-friendly Streamlit interface
- 🔑 Flexible API key configuration
- 📊 Interactive research results display

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CrewaiResearchAgent.git
cd CrewaiResearchAgent
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables (if using OpenAI or other API-based models):
   - Create a `.env` file in the root directory
   - Add your API keys as needed

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Access the application through your web browser (typically at `http://localhost:8501`)

3. In the sidebar:
   - Select your preferred AI model
   - Enter your API key (if required)
   - Input your research topic
   - Click "Generate Research"

4. View the generated research content in three tabs:
   - Content Plan
   - Initial Draft
   - Final Edited Version

## Project Structure

- `app.py`: Main Streamlit application file
- `config.py`: Configuration settings and environment setup
- `agents.py`: AI agent definitions and configurations
- `tasks.py`: Task definitions for the AI agents
- `utils.py`: Utility functions
- `requirements.txt`: Project dependencies

## Dependencies

- crewai: AI agent orchestration
- streamlit: Web interface framework
- openai: OpenAI API integration (if using OpenAI models)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 