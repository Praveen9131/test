from fastapi import FastAPI

app = FastAPI(title="Greeting API")

@app.get("/greet")
def greet(name: str):
    return {"message": f"Welcome to my world, {name}!"}
