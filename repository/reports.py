from sqlalchemy.orm import Session
import models

def create_report(db: Session, reported_ip:str):
    report = db.query(models.SuspiciousIP).filter(models.SuspiciousIP.ip_address == reported_ip)
    data = report.first()
    if data:
        report_count = data.report_count + 1
        report.update({'report_count': report_count})
        db.commit()
        db.refresh(data)
        return data
    report = models.SuspiciousIP(ip_address= reported_ip)
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

def get_report(db: Session, ip_address:str) -> models.SuspiciousIP | None:
    report = db.query(models.SuspiciousIP).filter(models.SuspiciousIP.ip_address == ip_address).first()
    return report