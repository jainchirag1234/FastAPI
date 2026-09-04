from fastapi import FastAPI

app=FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message":"Welcome to FastAPI"}

#About Route
@app.get("/about")
def about():
    return {"message":"This is an about Page"}
#Users Route
@app.get("/users")
def about():
    return {"users":["Mohit","Rohit","Amit"]}