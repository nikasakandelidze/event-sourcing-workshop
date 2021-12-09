from json import dumps, load
from utils.encoder import EventEncoder

DATA_FILE = "aggregator/storage/data.txt"


def get_persistent_state():
    with open(DATA_FILE, "r") as data_file:
        json_data = load(data_file)
        return json_data


def persist_event(event):
    # event_date = event.created_time
    # event_id = event.event_id
    # event_name = event.event_name
    # account_id = event.account.id
    # if event.event_name == 'create_account_event':
    #     account = event.account
    # elif event.event_name == 'withdraw_event':
    #     amount = event.amount
    # elif event.event_name == 'deposit_event':
    #     amount = event.amount
    data = dumps(event, indent=4, cls=EventEncoder)
    with open(DATA_FILE, "a") as data_file:
        data_file.write(data)
        data_file.flush()
