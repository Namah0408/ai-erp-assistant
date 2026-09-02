import json

from langchain_core.tools import tool
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Product


@tool
def search_products(search_term: str = "") -> str:
    """
    Search ERP inventory products by product name, code, category, or supplier.
    If search_term is empty, return all products.
    """

    db: Session = SessionLocal()

    try:
        query = db.query(Product)

        if search_term:
            query = query.filter(
                (Product.name.ilike(f"%{search_term}%")) |
                (Product.product_code.ilike(f"%{search_term}%")) |
                (Product.category.ilike(f"%{search_term}%")) |
                (Product.supplier.ilike(f"%{search_term}%"))
            )

        products = query.all()

        results = []

        for product in products:
            results.append({
                "id": product.id,
                "product_code": product.product_code,
                "name": product.name,
                "category": product.category,
                "supplier": product.supplier,
                "price": product.price,
                "stock_quantity": product.stock_quantity,
                "reorder_level": product.reorder_level
            })

        return json.dumps(results)

    finally:
        db.close()


@tool
def get_low_stock_products() -> str:
    """
    Find all products whose stock quantity is at or below their reorder level.
    """

    db: Session = SessionLocal()

    try:
        products = (
            db.query(Product)
            .filter(
                Product.stock_quantity <= Product.reorder_level
            )
            .all()
        )

        results = []

        for product in products:
            results.append({
                "product_code": product.product_code,
                "name": product.name,
                "stock_quantity": product.stock_quantity,
                "reorder_level": product.reorder_level,
                "supplier": product.supplier
            })

        return json.dumps(results)

    finally:
        db.close()


@tool
def get_product_stock(product_id: int) -> str:
    """
    Get the current stock information for a specific product.
    """

    db: Session = SessionLocal()

    try:
        product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not product:
            return json.dumps({
                "error": "Product not found"
            })

        return json.dumps({
            "product_code": product.product_code,
            "name": product.name,
            "stock_quantity": product.stock_quantity,
            "reorder_level": product.reorder_level,
            "supplier": product.supplier
        })

    finally:
        db.close()