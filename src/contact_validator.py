def validate_email(email):
    """Return True if email has basic valid format."""
    return "@" in email and "." in email.split("@")[-1]


def mask_email(email):
    """Mask part of the email username."""
    local, domain = email.split("@")

    if len(local) <= 2:
        masked_local = local[0] + "*" * (len(local) - 1)
    else:
        masked_local = local[:2] + "*" * (len(local) - 2)

    return f"{masked_local}@{domain}"


def normalize_phone(phone):
    """Remove dashes and validate phone number length."""
    cleaned = phone.replace("-", "")

    if len(cleaned) != 10 or not cleaned.isdigit():
        raise ValueError("Invalid phone number")

    return cleaned