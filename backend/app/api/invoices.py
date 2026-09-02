from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Invoice


router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)


@router.get("/")
def get_invoices(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()

    return invoices


@router.get("/unpaid")
def get_unpaid_invoices(db: Session = Depends(get_db)):
    invoices = (
        db.query(Invoice)
        .filter(Invoice.status == "Unpaid")
        .all()
    )

    return invoices


@router.get("/overdue")
def get_overdue_invoices(db: Session = Depends(get_db)):
    invoices = (
        db.query(Invoice)
        .filter(Invoice.status == "Overdue")
        .all()
    )

    return invoices


@router.get("/{invoice_id}")
def get_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):
    invoice = (
        db.query(Invoice)
        .filter(Invoice.id == invoice_id)
        .first()
    )

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )

    return invoice