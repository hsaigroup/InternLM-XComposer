from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import generate

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add routes
app.include_router(generate.router)

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


#uvicorn main:app --reload --port 7001 --host 0.0.0.0 --ssl-keyfile ./key.pem --ssl-certfile ./cert.pem