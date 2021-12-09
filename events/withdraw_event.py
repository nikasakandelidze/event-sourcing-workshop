
from events.domain_event import DomainEvent


class WithdrawEvent(DomainEvent):
    def __init__(self, amount: int, account_id: str) -> None:
        self.amount = amount
        self.account_id = account_id
        super().__init__('withdraw_event')
