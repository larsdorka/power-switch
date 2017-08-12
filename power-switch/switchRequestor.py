import requests


class SwitchRequestor:
    """"""

    def __init__(self, debug_log=dict()):
        """"""
        self.debug_log = debug_log
        self.debug_log['requestor_data'] = ""
        self.debug_log['requestor_response'] = ""
        self.debug_log['requestor_error'] = ""
        self.url = ""
        self.password = ""
        self.session = None

    def open(self, url, password):
        """"""
        self.url = url
        self.password = password
        self.session = requests.session()

    def login(self):
        """"""
        response = self.session.post(self.url + "/login.html", data={'pw': self.password})

    def logout(self):
        """"""
        response = self.session.get(self.url + "/login.html")

    def toggle_switches(self, switch_states=list(), outlet=0):
        """"""
        if len(switch_states) >= 4:
            data = dict()
            for index in range(4):
                if index == outlet:
                    if switch_states[index]:
                        data['cte' + str(index + 1)] = "1"
                    else:
                        data['cte' + str(index + 1)] = "0"
                else:
                    data['cte' + str(index + 1)] = ""
            self.debug_log['requestor_data'] = str(data)

            try:
                response = self.session.post(self.url, data=data)
                self.debug_log['requestor_response'] = str(response)
                self.debug_log['requestor_error'] = ""
            except Exception as ex:
                self.debug_log['requestor_error'] = str(ex)
