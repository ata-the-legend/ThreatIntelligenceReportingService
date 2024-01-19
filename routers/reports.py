from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import reports as schemas
from dependencies import get_db, get_current_user
from repository import reports as repo
from schemas.users import ReadUser
from utils import validate_ip_address

router = APIRouter(
    prefix='/report',
    tags=['Report']
)

@router.post('/report-ip', response_model=schemas.ReadReport)
def create_report(
    request: schemas.CreateReport, 
    current_user: ReadUser= Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not validate_ip_address(request.ip_address):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid IP address'
        )
    return repo.create_report(db=db, reported_ip=request.ip_address)

@router.get('/query-ip', response_model=schemas.ReadReport)
def query_ip(
    ip_address: str, 
    current_user: ReadUser= Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not validate_ip_address(ip_address):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid IP address'
        )
    report =  repo.get_report(db=db, ip_address=ip_address)
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='This ip address has not been reported.'
        )
    return report
