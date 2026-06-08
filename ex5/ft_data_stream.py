import random
from typing import Generator


Event = tuple[str, str]
EventStream = Generator[Event, None, None]


def gen_event() -> EventStream:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list[Event]) -> EventStream:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def build_event_list(event_stream: EventStream) -> list[Event]:
    events: list[Event] = []
    for _ in range(10):
        events.append(next(event_stream))
    return events


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_stream = gen_event()

    for index in range(1000):
        name, action = next(event_stream)
        print(f"Event {index}: Player {name} did action {action}")

    event_list = build_event_list(event_stream)
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
