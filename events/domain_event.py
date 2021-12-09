from uuid import uuid1
from datetime import datetime


class DomainEvent():
    def __init__(self, event_name) -> None:
        self.event_id = str(uuid1())
        self.created_time = str(datetime.now())
        self.event_name = event_name

    def process(self) -> None:
        pass
