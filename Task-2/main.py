from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/courses")
def get_courses():
    return {"courses": ["Frontend Development", "Generative AI", "Backend Development", "Data Science", "Cloud Computing", "DevOps", "Cyber Security", "Mobile Development", "UI/UX Design"]}