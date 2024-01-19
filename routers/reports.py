from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import reports as schemas
from dependencies import get_db
from repository import reports as repo

router = APIRouter(
    prefix='/report',
    tags=['Report']
)

@router.post('/report-ip', response_model=schemas.ReadReport)
def create_report(request: schemas.CreateReport, db: Session = Depends(get_db)):
    return repo.create_report(db=db, reported_ip=request.ip_address)

@router.get('/query-ip', response_model=schemas.ReadReport)
def query_ip(ip_address: str, db: Session = Depends(get_db)):
    report =  repo.get_report(db=db, ip_address=ip_address)
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='This ip address has not been reported.'
        )
    return report
