"""
Responsible for defining how the data will be presented to the user.
"""
import json
import typing


class View:
    pass


class TerminalJsonView(View):
    def __init__(self, data: dict, is_successful: bool) -> None:
        self.data = data
        self.is_successful = is_successful

    @property
    def _message(self) -> str:
        if self.is_successful:
            HEADERCRED = "\033[42m"
            HEADER = "    SUCCESS"
            BODYCRED = "\033[92m"
        else:
            HEADERCRED = "\033[41m"
            HEADER = "    FAILURE"
            BODYCRED = "\033[91m"

        json_data = json.dumps(self.data, indent=2)

        CEND = "\033[0m"

        header = f"{HEADERCRED}{HEADER}{CEND}"
        body = f"{BODYCRED}{json_data}{CEND}"

        return f"{header}\n{body}"

    def __str__(self) -> str:
        return self._message

    def __repr__(self) -> str:
        return self._message


class HttpView(View):

    def __init__(self,
                 status_code: int,
                 headers: typing.List[typing.Tuple[str, str]] = ([]),
                 body: str = "",
                 ) -> None:
        self.status_code = status_code
        self.headers = headers
        self.body = body
