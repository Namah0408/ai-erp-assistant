import json

from langchain_core.tools import tool
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Employee, LeaveRecord


@tool
def search_employees(department: str = "") -> str:
    """
    Search employees by department.
    If department is empty, return all employees.
    """

    db: Session = SessionLocal()

    try:
        query = db.query(Employee)

        if department:
            query = query.filter(
                Employee.department.ilike(f"%{department}%")
            )

        employees = query.all()

        results = []

        for employee in employees:
            results.append({
                "id": employee.id,
                "employee_code": employee.employee_code,
                "name": employee.name,
                "department": employee.department,
                "designation": employee.designation,
                "email": employee.email,
                "salary": employee.salary
            })

        return json.dumps(results)

    finally:
        db.close()


@tool
def get_employee_details(employee_id: int) -> str:
    """
    Get complete details of an employee using their employee ID.
    """

    db: Session = SessionLocal()

    try:
        employee = (
            db.query(Employee)
            .filter(Employee.id == employee_id)
            .first()
        )

        if not employee:
            return json.dumps({
                "error": "Employee not found"
            })

        return json.dumps({
            "id": employee.id,
            "employee_code": employee.employee_code,
            "name": employee.name,
            "department": employee.department,
            "designation": employee.designation,
            "email": employee.email,
            "salary": employee.salary
        })

    finally:
        db.close()


@tool
def get_employee_leaves(employee_id: int) -> str:
    """
    Get leave records for a specific employee.
    """

    db: Session = SessionLocal()

    try:
        leaves = (
            db.query(LeaveRecord)
            .filter(LeaveRecord.employee_id == employee_id)
            .all()
        )

        results = []

        for leave in leaves:
            results.append({
                "leave_type": leave.leave_type,
                "start_date": str(leave.start_date),
                "end_date": str(leave.end_date),
                "status": leave.status
            })

        return json.dumps(results)

    finally:
        db.close()