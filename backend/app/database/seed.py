from sqlalchemy.orm import Session

from .connection import Base, engine, SessionLocal
from .models import (
    Employee,
    LeaveRecord,
    Product,
    Invoice,
    PurchaseOrder
)


def seed_database():
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    try:
        # Prevent duplicate seed data
        if db.query(Employee).first():
            print("Database already contains data.")
            return

        employees = [
            Employee(
                employee_code="EMP001",
                name="Aarav Sharma",
                department="IT",
                designation="Software Engineer",
                email="aarav@novatech.com",
                salary=75000
            ),
            Employee(
                employee_code="EMP002",
                name="Priya Mehta",
                department="Finance",
                designation="Financial Analyst",
                email="priya@novatech.com",
                salary=68000
            ),
            Employee(
                employee_code="EMP003",
                name="Rahul Verma",
                department="HR",
                designation="HR Executive",
                email="rahul@novatech.com",
                salary=55000
            ),
            Employee(
                employee_code="EMP004",
                name="Sneha Kapoor",
                department="Procurement",
                designation="Procurement Manager",
                email="sneha@novatech.com",
                salary=82000
            ),
            Employee(
                employee_code="EMP005",
                name="Vikram Singh",
                department="Sales",
                designation="Sales Executive",
                email="vikram@novatech.com",
                salary=60000
            )
        ]

        db.add_all(employees)
        db.commit()

        # Refresh employees to get their IDs
        for employee in employees:
            db.refresh(employee)

        leave_records = [
            LeaveRecord(
                employee_id=employees[0].id,
                leave_type="Casual Leave",
                start_date="2026-08-10",
                end_date="2026-08-11",
                status="Approved"
            ),
            LeaveRecord(
                employee_id=employees[2].id,
                leave_type="Sick Leave",
                start_date="2026-08-20",
                end_date="2026-08-22",
                status="Approved"
            ),
            LeaveRecord(
                employee_id=employees[4].id,
                leave_type="Casual Leave",
                start_date="2026-08-25",
                end_date="2026-08-26",
                status="Pending"
            )
        ]

        db.add_all(leave_records)

        products = [
            Product(
                product_code="PROD001",
                name="Laptop",
                category="Electronics",
                supplier="TechSupply Ltd",
                price=65000,
                stock_quantity=25,
                reorder_level=10
            ),
            Product(
                product_code="PROD002",
                name="Wireless Mouse",
                category="Accessories",
                supplier="TechSupply Ltd",
                price=1200,
                stock_quantity=75,
                reorder_level=20
            ),
            Product(
                product_code="PROD003",
                name="Keyboard",
                category="Accessories",
                supplier="OfficeMart",
                price=1800,
                stock_quantity=8,
                reorder_level=15
            ),
            Product(
                product_code="PROD004",
                name="Office Chair",
                category="Furniture",
                supplier="OfficeMart",
                price=8500,
                stock_quantity=12,
                reorder_level=5
            ),
            Product(
                product_code="PROD005",
                name="Monitor",
                category="Electronics",
                supplier="DisplayTech",
                price=22000,
                stock_quantity=6,
                reorder_level=10
            )
        ]

        db.add_all(products)

        invoices = [
            Invoice(
                invoice_number="INV1001",
                customer_name="Alpha Solutions",
                amount=250000,
                invoice_date="2026-08-01",
                due_date="2026-08-15",
                status="Paid"
            ),
            Invoice(
                invoice_number="INV1002",
                customer_name="Beta Industries",
                amount=175000,
                invoice_date="2026-08-05",
                due_date="2026-08-20",
                status="Unpaid"
            ),
            Invoice(
                invoice_number="INV1003",
                customer_name="Gamma Technologies",
                amount=85000,
                invoice_date="2026-08-10",
                due_date="2026-08-25",
                status="Unpaid"
            ),
            Invoice(
                invoice_number="INV1004",
                customer_name="Delta Corp",
                amount=320000,
                invoice_date="2026-08-12",
                due_date="2026-08-27",
                status="Overdue"
            )
        ]

        db.add_all(invoices)

        purchase_orders = [
            PurchaseOrder(
                po_number="PO5001",
                supplier="TechSupply Ltd",
                product_name="Laptop",
                quantity=20,
                total_amount=1300000,
                order_date="2026-08-05",
                status="Approved"
            ),
            PurchaseOrder(
                po_number="PO5002",
                supplier="OfficeMart",
                product_name="Keyboard",
                quantity=50,
                total_amount=90000,
                order_date="2026-08-15",
                status="Pending"
            ),
            PurchaseOrder(
                po_number="PO5003",
                supplier="DisplayTech",
                product_name="Monitor",
                quantity=15,
                total_amount=330000,
                order_date="2026-08-20",
                status="Pending"
            )
        ]

        db.add_all(purchase_orders)

        db.commit()

        print("Database seeded successfully!")

    except Exception as error:
        db.rollback()
        print(f"Error while seeding database: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()