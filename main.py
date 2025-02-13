from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running with NumPy!"}

# You can add more endpoints here later.
