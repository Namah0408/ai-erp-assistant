from fastapi import FastAPI

from app.database.connection import Base, engine

from app.api import (
    employees,
    inventory,
    invoices,
    procurement,
    chat
)


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI ERP Assistant",
    description="Backend API for an AI-powered ERP Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AI ERP Assistant backend is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(employees.router)
app.include_router(inventory.router)
app.include_router(invoices.router)
app.include_router(procurement.router)
app.include_router(chat.router)