import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID

from src.db import Base


class MailBlackList(Base):
    __tablename__ = "mail_black_list"  # noqa
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255))
    app_id = Column(UUID(as_uuid=True))
    blocked_reason = Column(String(255))
    client_ip = Column(String(255))
    created_at = Column(DateTime)
