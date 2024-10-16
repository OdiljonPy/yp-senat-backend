import re

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException


def phone_number_validation(value):
    if not re.match('^+998\d{9}$', value):
        raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT, message='Phone number is invalid.')
