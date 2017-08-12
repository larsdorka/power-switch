import requests


class SwitchRequestor:
    """"""

    def __init__(self):
        """"""
        self.user = ""
        self.password = ""
        self.url = ""

    def open(self, url):
        """"""
        self.url = url

    def toggle_switches(self, switch_states=list()):
        """"""
        if len(switch_states) >= 4:
            data = dict()
            for index in range(4):
                if switch_states[index]:
                    data[str(index)] = True
                else:
                    data[str(index)] = False

            session = requests.session()
            try:
                response = session.post(self.url, json=data)
                print()
                print("response: " + str(response))
                print("body: " + response.json())
            except Exception as ex:
                print("Error while sending post request: " + str(ex))
