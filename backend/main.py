from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import employees
from app.api import inventory
from app.api import invoices
from app.api import procurement
from app.api import knowledge
from app.api import chat

app = FastAPI(
    title="AI ERP Assistant",
    description="AI-powered ERP assistant for NovaTech Industries",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routers
app.include_router(employees.router)
app.include_router(inventory.router)
app.include_router(invoices.router)
app.include_router(procurement.router)
app.include_router(knowledge.router)
app.include_router(chat.router)


@app.get("/")
def root():
    return {
        "message": "AI ERP Assistant backend is running"
    }