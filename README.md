# 🔧 AI Debugging Assistant

An intelligent debugging assistant powered by Google's Generative AI (Gemini) that helps you analyze Python code and error messages. Simply paste your code or error traceback, and the assistant will provide detailed debugging suggestions and solutions.

## Features

- **Code Analysis**: Paste Python code to get intelligent debugging suggestions
- **Error Message Analysis**: Provide error tracebacks for detailed troubleshooting
- **AI-Powered Insights**: Leverages Google Gemini AI for accurate and helpful debugging advice
- **User-Friendly Interface**: Built with Streamlit for an intuitive web-based experience
- **Real-time Processing**: Get instant feedback on your code issues

## Project Structure

```
GenAI Project/
├── apps/
│   └── debugging_assistant/
│       ├── app.py              # Main Streamlit application
│       └── prompts.py          # Prompt templates
├── config/
│   ├── config.yaml             # Configuration settings
│   ├── model_config.py         # Model configuration
├── utils/
│   ├── llm_client.py           # Gemini AI client
│   ├── debugging_helper.py     # Debugging helper functions
│   ├── text_helpers.py         # Text processing utilities
│   ├── itinerary_helper.py     # Itinerary utilities
│   ├── mcp_helper.py           # Model Context Protocol helpers
│   └── prompts/                # Prompt templates in JSON
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Prerequisites

- Python 3.10+
- Google Generative AI API key
- Virtual environment (recommended)

## Installation

1. **Clone or download the project**
   ```bash
   cd "GenAI Project"
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   myenv\Scripts\Activate.ps1
   ```
   
   On macOS/Linux:
   ```bash
   source myenv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your environment variables**
   
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_google_generative_ai_api_key_here
   ```

## Running the Application

Navigate to the project directory and run:

```bash
streamlit run apps/debugging_assistant/app.py
```

The application will open in your default browser at `http://localhost:8501`

### Alternative: Using Python Module Invocation

```bash
python -m streamlit run apps/debugging_assistant/app.py
```

## Usage

1. Open the Streamlit app in your browser
2. Paste your Python code or error message in the text area
3. Click the "Debug Code" button
4. Wait for the AI to analyze and provide debugging suggestions
5. Review the detailed suggestions provided

## Dependencies

Key libraries used in this project:

| Library | Version | Purpose |
|---------|---------|---------|
| `streamlit` | 1.41.0 | Web framework for UI |
| `google-generativeai` | 0.7.2 | Google Gemini AI SDK |
| `python-dotenv` | 1.0.1 | Environment variable management |
| `pydantic` | 2.9.0 | Data validation |
| `pandas` | 2.2.3 | Data processing |
| `beautifulsoup4` | 4.12.3 | Web scraping support |
| `pyyaml` | 6.0.2 | YAML configuration parsing |

## Configuration

Configuration settings are managed through:
- `config/config.yaml` - General application settings
- `config/model_config.py` - AI model configuration

## Troubleshooting

### Virtual Environment Issues
If you encounter issues with the virtual environment, try:
```bash
# Remove and recreate
rmdir myenv
python -m venv myenv
```

### Streamlit Not Found
Ensure the virtual environment is activated and streamlit is installed:
```bash
pip install streamlit
```

### API Key Issues
- Verify your Google Generative AI API key is correctly set in the `.env` file
- Check that you have API access enabled for your Google Cloud project
- Ensure the `.env` file is in the project root directory

## Contributing

Feel free to extend this project by:
- Adding new debugging features
- Improving the UI/UX with Streamlit
- Enhancing prompt engineering for better suggestions
- Adding support for other programming languages

## License

This project is part of DSA GenAI LearnYard.

## Support

For issues, questions, or suggestions, please check the project structure and ensure all dependencies are properly installed.

## Demo
<img width="1872" height="952" alt="image" src="https://github.com/user-attachments/assets/304965ff-bdd1-4512-bcba-3a60c8509cad" />



