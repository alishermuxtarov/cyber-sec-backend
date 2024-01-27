def cleanup_phone(phone: str) -> str:
    return '+{}'.format(phone.lstrip('+').strip())
