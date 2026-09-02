from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Employee, LeaveRecord


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()

    return employees


@router.get("/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.get("/{employee_id}/leaves")
def get_employee_leaves(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    leaves = (
        db.query(LeaveRecord)
        .filter(LeaveRecord.employee_id == employee_id)
        .all()
    )

    return leaves