from http import HTTPStatus

from flask import Blueprint
from flask import request

from src.common.decorators import handle_exceptions
from src.common.decorators import is_authenticated
from src.services.black_list_mail_services import create_black_email
from src.services.black_list_mail_services import is_mail_in_black_list

blueprint = Blueprint("blacklist_api", __name__, url_prefix="/blacklists")


@blueprint.route("", methods=["POST"])
@handle_exceptions
@is_authenticated
def create_black_list():
    return create_black_email(request), HTTPStatus.CREATED


@blueprint.route("/<string:email>", methods=["GET"])
@handle_exceptions
@is_authenticated
def get_mail_in_black_list(email):
    return is_mail_in_black_list(email), HTTPStatus.OK


@blueprint.route("/health", methods=["GET"])
def health():
    return "healthy", HTTPStatus.OK
