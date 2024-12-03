from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

user_inputs = {}

class UserInputs(BaseModel):
    age: int
    first_verb: str
    second_verb: str

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/submit_data")
async def submit_data(data: UserInputs):
    user_inputs["age"] = data.age
    user_inputs["first_verb"] = data.first_verb
    user_inputs["second_verb"] = data.second_verb
    return {"message": "Data received successfully"}

@app.get("/generate_story")
async def generate_story():
    if "age" in user_inputs and "first_verb" in user_inputs and "second_verb" in user_inputs:
        story = f"At the age of {user_inputs['age']}, you decided to {user_inputs['first_verb']} all day long. Then, you felt the urge to {user_inputs['second_verb']} even more!"
        return {"story": story}
    return {"story": "Please provide all inputs first."}

@app.get("/", response_class=HTMLResponse)
async def get_html():
    with open("static/index.html", "r") as file:
        content = file.read()
    return content