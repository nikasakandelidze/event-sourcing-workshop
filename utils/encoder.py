from json import JSONEncoder


class AccountEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class EventEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
