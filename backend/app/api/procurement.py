from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.connection import get_db
from app.database.models import PurchaseOrder


router = APIRouter(
    prefix="/purchase-orders",
    tags=["Procurement"]
)


class PurchaseOrderCreate(BaseModel):
    supplier: str
    product_name: str
    quantity: int
    total_amount: float


@router.get("/")
def get_purchase_orders(db: Session = Depends(get_db)):
    purchase_orders = db.query(PurchaseOrder).all()

    return purchase_orders


@router.get("/pending")
def get_pending_purchase_orders(db: Session = Depends(get_db)):
    purchase_orders = (
        db.query(PurchaseOrder)
        .filter(PurchaseOrder.status == "Pending")
        .all()
    )

    return purchase_orders


@router.get("/{purchase_order_id}")
def get_purchase_order(
    purchase_order_id: int,
    db: Session = Depends(get_db)
):
    purchase_order = (
        db.query(PurchaseOrder)
        .filter(PurchaseOrder.id == purchase_order_id)
        .first()
    )

    if not purchase_order:
        raise HTTPException(
            status_code=404,
            detail="Purchase order not found"
        )

    return purchase_order


@router.post("/")
def create_purchase_order(
    order: PurchaseOrderCreate,
    db: Session = Depends(get_db)
):
    order_count = db.query(PurchaseOrder).count()

    new_order = PurchaseOrder(
        po_number=f"PO{5001 + order_count}",
        supplier=order.supplier,
        product_name=order.product_name,
        quantity=order.quantity,
        total_amount=order.total_amount,
        order_date="2026-08-31",
        status="Pending"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order