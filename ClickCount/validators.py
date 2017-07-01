from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def imageNameValidator(name):
    if not name:
        raise ValidationError('name is necessary')


def imageUrlValidator(url):
    validator = URLValidator()
    if not url:
        raise ValidationError('url is necessary')
    else:
        try:
            validator(url)
        except ValidationError:
            raise ValidationError('url isn\'t correct')


def urlValidator(url):
    if not url:
        raise ValidationError('url and url are necessary')
    else:
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError:
            raise ValidationError('url isn\'t correct')


def buttonNameValidator(name):
    if not name:
        raise ValidationError('name is necessary')
