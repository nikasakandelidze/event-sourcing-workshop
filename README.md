# what is event sourcing?
The Event Sourcing pattern defines an approach to handling operations on data that's driven by a sequence of events, each of which is recorded in an append-only store.

## Example in code
Main idea for the implementation in this repo, is we have Accounts ( like we have in bank )
We can create, deposit and withdraw from the account. Instead of regular programming model where we  simply mutate the state of let's say
account object ( created from some class ) now everything is an event. So for every action we have an according event, like: createAccountEvent, depositEvent, withdrawEvent.
Whenever we want to do some aciton we create an according event and sent it to aggregator, which is some kind of an event handler which know what to do with each event.

Event handler upon recieving event does 2 main conceptual steps: updates current in memory state, so that application logic can continute to use updated data. It also
persists this event with a timestamp into a persistent storage ( in our example file system ). the idea is that at every point in time, we should be able to audit the history
of the state changes of any point in time.
