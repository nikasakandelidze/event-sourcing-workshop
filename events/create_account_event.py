from events.domain_event import DomainEvent
from domain.account import Account


class CreateAccountEvent(DomainEvent):
    def __init__(self, account: Account) -> None:
        self.account = account
        super().__init__('create_account_event')
