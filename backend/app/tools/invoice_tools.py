import json

from langchain_core.tools import tool
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Invoice


@tool
def search_invoices(search_term: str = "") -> str:
    """
    Search invoices by invoice number or customer name.
    If search_term is empty, return all invoices.
    """

    db: Session = SessionLocal()

    try:
        query = db.query(Invoice)

        if search_term:
            query = query.filter(
                (Invoice.invoice_number.ilike(f"%{search_term}%")) |
                (Invoice.customer_name.ilike(f"%{search_term}%"))
            )

        invoices = query.all()

        results = []

        for invoice in invoices:
            results.append({
                "id": invoice.id,
                "invoice_number": invoice.invoice_number,
                "customer_name": invoice.customer_name,
                "amount": invoice.amount,
                "invoice_date": str(invoice.invoice_date),
                "due_date": str(invoice.due_date),
                "status": invoice.status
            })

        return json.dumps(results)

    finally:
        db.close()


@tool
def get_unpaid_invoices() -> str:
    """
    Get all invoices that are currently unpaid.
    """

    db: Session = SessionLocal()

    try:
        invoices = (
            db.query(Invoice)
            .filter(
                Invoice.status.ilike("unpaid")
            )
            .all()
        )

        results = []

        for invoice in invoices:
            results.append({
                "invoice_number": invoice.invoice_number,
                "customer_name": invoice.customer_name,
                "amount": invoice.amount,
                "due_date": str(invoice.due_date),
                "status": invoice.status
            })

        return json.dumps(results)

    finally:
        db.close()


@tool
def get_overdue_invoices() -> str:
    """
    Get all invoices that are overdue.
    """

    db: Session = SessionLocal()

    try:
        invoices = (
            db.query(Invoice)
            .filter(
                Invoice.status.ilike("overdue")
            )
            .all()
        )

        results = []

        for invoice in invoices:
            results.append({
                "invoice_number": invoice.invoice_number,
                "customer_name": invoice.customer_name,
                "amount": invoice.amount,
                "due_date": str(invoice.due_date),
                "status": invoice.status
            })

        return json.dumps(results)

    finally:
        db.close()