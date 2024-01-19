from pydantic import BaseModel
from datetime import datetime

class BaseReprt(BaseModel):
    ip_address: str

class ReadReport(BaseReprt):
    id: int
    report_count: int
    last_reported: datetime

    class config:
        orm_mode: True


class CreateReport(BaseReprt):
    pass
