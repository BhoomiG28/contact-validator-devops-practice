import pytest

from src.contact_validator import validate_email, mask_email


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