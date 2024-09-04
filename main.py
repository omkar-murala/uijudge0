from fastapi import FastAPI
from Models.Auth.Auth_Model import Auth   # Renamed to avoid conflict


# Server initialization
app = FastAPI()

@app.get("/")
def helloworld():
    return {"data": "Hello world"}

@app.post("/auth")
def auth(auth: Auth):  # Use the model as a parameter type
    if not auth.email:
        return {"message": "Email is required", "status": 404}
    return {"message": "Success", "status": 200}
