import os
import json 
from google import genai


def answers(prompt):
  client = genai.Client(api_key = "YOUR_API_KEY_HERE")
  response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = str(prompt)
  )
  return json.loads(response.json())
