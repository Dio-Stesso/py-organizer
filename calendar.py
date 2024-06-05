from organizer_event import OrganizerEvent
from datetime import datetime


class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event: OrganizerEvent):
        self.events.append(event)

    def remove_event(self, event: OrganizerEvent):
        self.events.remove(event)

    def update_event(self, old_event: OrganizerEvent, new_event: OrganizerEvent):
        index = self.events.index(old_event)
        self.events[index] = new_event

    def find_events_by_date(self, date: datetime):
        return [event for event in self.events if event.occurs_on(date)]

    def find_events_by_date_range(self, start_date: datetime, end_date: datetime):
        return [event for event in self.events if event.start_date <= end_date and event.end_date >= start_date]

    def sort_events_by_date(self):
        return sorted(self.events, key=lambda event: event.start_date)

    def sort_events_by_category(self):
        return sorted(self.events, key=lambda event: event.category)
