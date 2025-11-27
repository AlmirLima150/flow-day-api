from fastapi import FastAPI

app = FastAPI(
    title="Flow Day API",
    description="API para gerenciamento pessoal modular, começando com rotina diária.",
    version="0.1.0"
)

@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}

@app.get("/health")
def health() -> dict:
    return {
            "status": "ok", 
            "service": "flow-day-api", 
            "version": "0.1.0"
            } 