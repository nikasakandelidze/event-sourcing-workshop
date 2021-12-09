from aggregator.state import main as state
from aggregator.storage import main as storage


def handle_event(event):
    if event.event_name == 'create_account_event':
        account_id = event.account.id
        state.account_states[account_id] = event.account
    elif event.event_name == 'withdraw_event':
        account_id = event.account_id
        state.account_states[account_id].withdraw_money(event.amount)
    elif event.event_name == 'deposit_event':
        account_id = event.account_id
        state.account_states[account_id].deposit_money(event.amount)
    storage.persist_event(event)


def get_inmemory_state():
    return state


def get_persistent_state():
    return storage.get_persistent_state()
