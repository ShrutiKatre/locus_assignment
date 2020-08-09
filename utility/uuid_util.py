import uuid


def get_uuid():
    return str(uuid.uuid4())


def get_short_uuid():
    return uuid.uuid4().hex[:8].upper()


def validate_uuid(text):
    try:
        uuid.UUID(text)
        return True
    except:
        return False
