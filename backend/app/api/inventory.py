from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Product


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.get("/")
def get_inventory(db: Session = Depends(get_db)):
    products = db.query(Product).all()

    return products


@router.get("/low-stock")
def get_low_stock_products(db: Session = Depends(get_db)):
    products = (
        db.query(Product)
        .filter(Product.stock_quantity <= Product.reorder_level)
        .all()
    )

    return products


@router.get("/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product