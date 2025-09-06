from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to Selluna"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}