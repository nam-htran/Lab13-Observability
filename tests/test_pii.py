from app.pii import scrub_text


def test_scrub_email() -> None:
    out = scrub_text("Email me at student@vinuni.edu.vn")
    assert "student@" not in out
    assert "REDACTED_EMAIL" in out


def test_scrub_common_sensitive_fields() -> None:
    out = scrub_text(
        "Phone 0987654321, card 4111 1111 1111 1111, passport A12345678, "
        "Dia chi: 123 Duong Le Loi, Quan 1"
    )

    assert "0987654321" not in out
    assert "4111" not in out
    assert "A12345678" not in out
    assert "Le Loi" not in out
    assert "REDACTED_PHONE_VN" in out
    assert "REDACTED_CREDIT_CARD" in out
    assert "REDACTED_PASSPORT" in out
    assert "REDACTED_ADDRESS_VN" in out
