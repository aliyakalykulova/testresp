from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_db = {
    "husky": 20,
    "labrador": 25
}

class DogRequest(BaseModel):
    breed: str

@app.post("/get-weight")
async def get_weight(request: DogRequest):
    weight = fake_db.get(request.breed, 0)
    return {"weight": weight}
