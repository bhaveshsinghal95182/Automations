import re
import os
import json
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="""You are a resume writer bot which takes in the description of the job, relecant projects and details and generates relevant data output \nUse this JSON schema:\nresume_data = {
    "summary": "Passion for building inspiring companies through industry-leading tech...",
    "projects": [
        {
            "name": "Learning Management System",
            "description": "Made a Learning Management System",
            "learning": "learned backed, frontend and integration"
            "github": "github link"
        },
        {
            "name": "jarvis",
            "description": "made a voice operated multi agent ai automation system"
            "learning": "learned to work with a team on different ml projects",
            "github": "github link",
        },
    ],
    "education": "Bachelor of Science in Economics - University of Wisconsin - Madison",
    "softskills": ["Leadership", "Speaking", "Fundraising", "Product Development", "Communication"],
    "technicalskills": ["c++", "PHP", "Javascript"]
} dont give any unnecessary explanations""",
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("""Published time: Sep 14, 2024
Company name: NewPage Solutions Inc
Title: Python Developer
Grades: middle, middle+
Job description: Python Developer role works within the Edison team to build-out features needed by stakeholders. Requires understanding of automated testing, AWS services, and PHP. Clients' web publishing platform allows for safe, quick, and sustainable changes to production. Duties include building out features defined by the product owner and tech lead.
Location: Remote
Anywhere: No
Remote: Yes""")

answer = response.text
print(answer)

match = re.search(r'{(.|\s)*}', answer)  # This will match the JSON across multiple lines

if match:
    # If a match is found, parse and save it
    json_data = match.group()
    data = json.loads(json_data)
    print("___")
    print(data)

    # Save the parsed JSON data into a file
    with open('resume maker\\dataFormat.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("JSON data has been saved to data.json")
else:
    print("No JSON data found in the string.")