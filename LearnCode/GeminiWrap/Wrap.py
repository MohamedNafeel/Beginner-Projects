import os
import json 
from google import genai


def answers(prompt):
  client = genai.Client(api_key = "AQ.Ab8RN6JlDBQC0ABBr8RTmDpDZc8wgutdmyVOwb3Nvba8XiLHgw")
  response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = str(prompt)
  )
  return json.loads(response.json())