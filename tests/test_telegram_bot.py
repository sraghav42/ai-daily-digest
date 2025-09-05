import requests
from notifier.telegram_bot import send_to_telegram

def test_send_message_success(monkeypatch):
    class FakeResponse:
        status_code = 200
        text = "OK"

    monkeypatch.setattr(requests, "post", lambda url, data: FakeResponse())
    # No exception should be raised
    result = send_to_telegram("Hello World")
    assert result is None  # since your function doesn't return anything

def test_send_message_failure(monkeypatch):
    class FakeResponse:
        status_code = 400
        text = "Bad Request"

    monkeypatch.setattr(requests, "post", lambda url, data: FakeResponse())
    result = send_to_telegram("Hello World")
    assert result is None  # Function only prints errors