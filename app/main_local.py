import uvicorn
from main import app

print("Starting...")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    