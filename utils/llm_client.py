from __future__ import annotations

import os
from typing import Optional

import google.generativeai as genai
from dotenv import load_dotenv
from config.model_config import AppConfig, load_config
load_dotenv()

class GeminiClass:
    def __init__(self,api_key : Optional[str] = None, config_path: Optional[str] = None):
        self.app_config = load_config(config_path)
        self.model_cfg = self.app_config.model

        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key must be provided either as an argument or through the GEMINI_API_KEY environment variable.")
        
        # Configure the Gemini API client
        genai.configure(api_key = self.api_key)
        # Initialize the model
        self.model = genai.GenerativeModel(self.model_cfg.name)

    def ask(self, prompt: str) ->str:
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature" : self.model_cfg.temperature,
                "top_p" : self.model_cfg.top_p,
                "max_output_tokens" : self.model_cfg.max_output_tokens
            }  
        )
        if not response or not hasattr(response, 'text'):
            raise ValueError("Received an invalid response from the Gemini API.")
        return response.text