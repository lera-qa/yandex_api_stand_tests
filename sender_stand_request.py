import configuration
import requests


def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers={"Content-Type": "application/json"}
    )