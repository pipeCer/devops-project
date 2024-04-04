from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models.mail_black_list import MailBlackList


class MailBlackCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MailBlackList

    id = fields.String()
    email = fields.String()
    app_id = fields.String()
    blocked_reason = fields.String()
    client_ip = fields.String()
    created_at = fields.DateTime()
