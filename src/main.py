from pydantic import BaseModel
import uvicorn

from fastapi import FastAPI
from tasks.router import router as task_router 

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}   

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
