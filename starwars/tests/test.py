from app.api_read import read_api
import requests


def test_read_from_api():
    assert read_api()["status code"] == 200