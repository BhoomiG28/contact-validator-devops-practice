import pytest

from src.contact_validator import validate_email, mask_email, normalize_phone


def test_validate_email_valid():
    assert validate_email("priya@example.com") is True


def test_validate_email_invalid():
    assert validate_email("priya@example") is False


def test_validate_email_no_at():
    assert validate_email("priya.example.com") is False

def test_mask_email_basic():
    email = "priya@example.com"

    result = mask_email(email)

    assert result == "pr***@example.com"

def test_normalize_phone():
    phone = "555-123-4567"

    result = normalize_phone(phone)

    assert result == "5551234567"


def test_normalize_phone_invalid():
    phone = "12345"

    with pytest.raises(ValueError):
        normalize_phone(phone)