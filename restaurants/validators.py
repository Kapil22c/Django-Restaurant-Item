from django.core.exceptions import ValidationError
#from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

# def clean_email(value):
#     email= value
#     if ".edu" in email:
#         raise ValidationError("Not a valid email edu is not correct")

def validate_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError("Not a valid email edu is not correct")

# continue with this...
CATEGORIES = ['Mexican', 'Chinese', 'game e', 'indian', 'japanese']

def validate_category(value):
    cat = value.capitalize();
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f'{value} is not a valid category')

