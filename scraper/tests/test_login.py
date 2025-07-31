import pytest
import requests
from requests.cookies import RequestsCookieJar
from scraper.tests.supports.constants import TOKEN_HTML
from scraper.login import login


class FakeResponse:
    def __init__(self, text=""):
        self.text = text


class SuccessSession:
    def __init__(self):
        self.cookies = RequestsCookieJar()

    def get(self, url, params=None, **kwargs):
        return FakeResponse(TOKEN_HTML)

    def post(self, url, data=None, headers=None, **kwargs):
        if data and data.get("token") == "test-token":
            self.cookies.set("pmaAuth-1", "ok")
        return FakeResponse("OK")


class FailureSession:
    def __init__(self):
        self.cookies = RequestsCookieJar()

    def get(self, url, params=None, **kwargs):
        return FakeResponse(TOKEN_HTML)

    def post(self, url, data=None, headers=None, **kwargs):
        return FakeResponse("FAIL")


class MissingTokenSession:
    def __init__(self):
        self.cookies = RequestsCookieJar()

    def get(self, url, params=None, **kwargs):
        return FakeResponse("<html><body>No token here</body></html>")

    def post(self, url, data=None, headers=None, **kwargs):
        return FakeResponse("OK")


def test_login_success(monkeypatch):
    monkeypatch.setattr(requests, "Session", lambda: SuccessSession())
    sess = login("user", "pass")
    assert isinstance(sess, SuccessSession)
    assert any(k.startswith("pmaAuth") for k in sess.cookies.keys())


def test_login_failure_raises(monkeypatch):
    monkeypatch.setattr(requests, "Session", lambda: FailureSession())
    with pytest.raises(RuntimeError):
        login("user", "wrong-pass")


def test_login_missing_token_raises(monkeypatch):
    monkeypatch.setattr(requests, "Session", lambda: MissingTokenSession())
    with pytest.raises((KeyError, TypeError, AttributeError)):
        login("user", "pass")
