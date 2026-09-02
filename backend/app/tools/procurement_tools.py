import json
from datetime import date

from langchain_core.tools import tool
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import PurchaseOrder


@tool
def get_pending_purchase_orders() -> str:
    """
    Get all purchase orders that are currently pending.
    """

    db: Session = SessionLocal()

    try:
        orders = (
            db.query(PurchaseOrder)
            .filter(
                PurchaseOrder.status.ilike("pending")
            )
            .all()
        )

        results = []

        for order in orders:
            results.append({
                "id": order.id,
                "po_number": order.po_number,
                "supplier": order.supplier,
                "product_name": order.product_name,
                "quantity": order.quantity,
                "total_amount": order.total_amount,
                "order_date": str(order.order_date),
                "status": order.status
            })

        return json.dumps(results)

    finally:
        db.close()


@tool
def search_purchase_orders(search_term: str = "") -> str:
    """
    Search purchase orders by PO number, supplier, or product name.
    """

    db: Session = SessionLocal()

    try:
        query = db.query(PurchaseOrder)

        if search_term:
            query = query.filter(
                (PurchaseOrder.po_number.ilike(f"%{search_term}%")) |
                (PurchaseOrder.supplier.ilike(f"%{search_term}%")) |
                (PurchaseOrder.product_name.ilike(f"%{search_term}%"))
            )

        orders = query.all()

        results = []

        for order in orders:
            results.append({
                "id": order.id,
                "po_number": order.po_number,
                "supplier": order.supplier,
                "product_name": order.product_name,
                "quantity": order.quantity,
                "total_amount": order.total_amount,
                "order_date": str(order.order_date),
                "status": order.status
            })

        return json.dumps(results)

    finally:
        db.close()


@tool
def create_purchase_order(
    supplier: str,
    product_name: str,
    quantity: int,
    total_amount: float
) -> str:
    """
    Create a new purchase order in the ERP database.
    """

    db: Session = SessionLocal()

    try:
        latest_order = (
            db.query(PurchaseOrder)
            .order_by(PurchaseOrder.id.desc())
            .first()
        )

        if latest_order:
            next_id = latest_order.id + 1
        else:
            next_id = 1

        po_number = f"PO-{next_id:04d}"

        new_order = PurchaseOrder(
            po_number=po_number,
            supplier=supplier,
            product_name=product_name,
            quantity=quantity,
            total_amount=total_amount,
            order_date=date.today(),
            status="Pending"
        )

        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        return json.dumps({
            "message": "Purchase order created successfully",
            "po_number": new_order.po_number,
            "supplier": new_order.supplier,
            "product_name": new_order.product_name,
            "quantity": new_order.quantity,
            "total_amount": new_order.total_amount,
            "status": new_order.status
        })

    except Exception as e:
        db.rollback()

        return json.dumps({
            "error": f"Could not create purchase order: {str(e)}"
        })

    finally:
        db.close()