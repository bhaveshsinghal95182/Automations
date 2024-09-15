from datetime import datetime
import ollama
import json

def scheduler(question: str) -> str:
    """This bot is for the scheduling purposes and it currently only supports my timetable and i dont care how u guys use this logic but meh its a very simple logic anyways

    Arguments:
    question -- A string containing the question to ask the bot.

    Returns:
    A string response based on the current time and day's schedule.
    """

    day = datetime.now().strftime("%A")
    time = datetime.now().strftime("%H:%M:%S")

    intentPrompt = f"the user is asking the question {question}, you are to only reply in ['today', 'any other day'] these two words based on the user prompt"

    intent = ollama.chat(model='mistral', messages=[
        {
            'role': 'user',
            'content': intentPrompt
        }
    ])

    try:
        with open("Scheduler\\3rd_sem_timetable.json") as file:
            whole_schedule = json.load(file)
    except:
        return "Please add a json file of your schedule"

    

    if 'today' in intent:
        try:
            day_schedule = whole_schedule[day.upper()]
        except Exception as e:
            day_schedule = "No college schedule for today"

        prompt: str = f"you are a scheduling bot which takes in the current time {time} and the day's schedule {day_schedule} and respond to the the question: {question} accordingly"
    else:
        prompt: str = f"you are a scheduling bot which takes in the whole schedule {whole_schedule} and respond to the the question: {question} accordingly, today is {day}"

    response = ollama.chat(model='mistral', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])

    return response['message']['content']

while True:  
    prompt = input("whats your question about college schedule\n")

    if "/bye" in prompt:
        break

    print(scheduler(prompt))
