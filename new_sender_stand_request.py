import configuration
import requests


def get_logs():
    return (requests.get(configuration.URL_SERVICE + configuration.api_logs_main, params={"count":20}))


request = get_logs()
print(request.status_code)
print(request.headers)
