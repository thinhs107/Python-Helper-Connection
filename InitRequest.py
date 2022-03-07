import requests


class CallRequest:
    def __init__(self, URL: str):
        self.URL = URL

    def Get_Requests(self):
        try:
            response = requests.get(self.URL)

            return response.json()
            response.close()
        except requests.exceptions.HTTPError as err:
            return print(SystemError(err))
