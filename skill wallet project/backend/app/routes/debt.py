from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.models import Loan
from app.schemas import LoanCreate

router = APIRouter(prefix="/debts", tags=["Debts"])


@router.get("/{user_id}")
def get_loans(
    user_id: int,
    db: Session = Depends(get_db)
):
    loans = (
        db.query(Loan)
        .filter(Loan.user_id == user_id)
        .all()
    )

    return loans


@router.post("/{user_id}")
def add_loan(
    user_id: int,
    loan_data: LoanCreate,
    db: Session = Depends(get_db)
):
    loan = Loan(
        user_id=user_id,
        lender_name=loan_data.lender_name,
        outstanding_amount=loan_data.outstanding_amount,
        interest_rate=loan_data.interest_rate,
        emi=loan_data.emi,
        overdue_months=loan_data.overdue_months,
        loan_type=loan_data.loan_type
    )

    db.add(loan)
    db.commit()
    db.refresh(loan)

    return {
        "message": "Loan added successfully",
        "loan": loan
    }


@router.delete("/{loan_id}")
def delete_loan(
    loan_id: int,
    db: Session = Depends(get_db)
):
    loan = (
        db.query(Loan)
        .filter(Loan.id == loan_id)
        .first()
    )

    if not loan:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    db.delete(loan)
    db.commit()

    return {
        "message": "Loan deleted successfully"
    }