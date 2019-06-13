from flask import Blueprint, request
from app.sample_code import sample_service
from app.utils.basic_utils import *

sample_api = Blueprint('sample_api', __name__)


@sample_api.route("/project/sample", methods=['POST'])
def sample_handler():
    try:
        if request.is_json:
            response = sample_service.sample_services(request.get_json())
            return jsonify(response)
        else:
            return jsonify(BAD_INPUT)

    except Exception as ex:
        exception_response(ex)
        return "exception occured", 400
