from aggregator import main as aggregator
from domain.account import Account
from events import create_account_event, deposit_event, withdraw_event

first_account = Account("0", "nika")
aggregator.handle_event(create_account_event.CreateAccountEvent(first_account))
aggregator.handle_event(deposit_event.DepositEvent(1, first_account.id))
aggregator.handle_event(deposit_event.DepositEvent(2, first_account.id))
aggregator.handle_event(withdraw_event.WithdrawEvent(3, first_account.id))
# print(aggregator.get_persistent_state)
