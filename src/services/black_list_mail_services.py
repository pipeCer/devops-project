import datetime

from src.common.decorators import db_session
from src.common.exceptions import InvalidParameterException
from src.common.exceptions import ResourceExistsException
from src.common.utils import email_is_valid
from src.common.utils import uuid_is_valid
from src.models.mail_black_list import MailBlackList
from src.schema.mail_black_list_schema import MailBlackCreateSchema


@db_session
def create_black_email(session, request):
    data = request.get_json()
    email = data.get("email")
    app_id = data.get("app_id")
    blocked_reason = data.get("blocked_reason")
    created_at = datetime.datetime.now()

    if not all([email, app_id]):
        raise InvalidParameterException("email and app_id are required")

    if not email_is_valid(email):
        raise InvalidParameterException("Invalid email")

    if not uuid_is_valid(app_id):
        raise InvalidParameterException("Invalid app_id")

    # check email and app_id already exists
    mail = session.query(MailBlackList).filter_by(email=email, app_id=app_id).first()
    if mail:
        raise ResourceExistsException("Email and app_id already exists")

    client_ip = request.remote_addr
    black_list = MailBlackList(email=email, app_id=app_id, blocked_reason=blocked_reason, client_ip=client_ip, created_at=created_at)
    session.add(black_list)
    session.commit()

    response = MailBlackCreateSchema().dump(black_list)
    response["message"] = "Email added to black list"

    return response


@db_session
def is_mail_in_black_list(session, email):
    mail = session.query(MailBlackList).filter_by(email=email).first()
    response = {"email": email, "is_black_listed": False}
    if mail:
        response["is_black_listed"] = True
    return response
