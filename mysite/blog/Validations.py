from django.core.exceptions import ValidationError
import re
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain


def validation_for_profile(value):
    if  not value:
        raise ValidationError("Please provide Profile pic of the User")
    return value
    
def validation_for_address(value):
    if  value=='':
        raise ValidationError("Adreess can't be none or empty")
    return value
def validation_for_username(value):
    if  value=='':
        raise ValidationError("Username can't be none or Empty")
    return value
def validation_for_email(email):
    if  not re.fullmatch(email_re, email):
      raise ValidationError("Please provoid valid email")
    return email
def validation_for_first_name(value):
    if  value=='':
        raise ValidationError("first_name can't be none or Empty")
    return value
def validation_for_last_name(value):
    if  value=='':
        raise ValidationError("last_name can't be none or Empty")
    return value
def validation_for_password(val1,val2):
    if val1=='' :
            raise ValidationError("Password can't be empty")    
    elif val1!=val2:
        raise ValidationError("Password and Confirm password not matches")
    return val1
def validation_for_password1(val1):
    if val1=='' :
            raise ValidationError("Password can't be empty")    
    return val1

