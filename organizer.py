from calendar import Calendar
from datetime import datetime, timedelta


class Organizer:
    def __init__(self):
        self.calendars = {}

    def create_calendar(self, name):
        self.calendars[name] = Calendar()

    def delete_calendar(self, name):
        del self.calendars[name]

    def get_calendar(self, name):
        return self.calendars.get(name)

    def get_upcoming_events(self, days=7):
        upcoming_events = []
        now = datetime.now()
        end_date = now + timedelta(days=days)
        print(f"Finding events between {now} and {end_date}")
        for calendar in self.calendars.values():
            events = calendar.find_events_by_date_range(now, end_date)
            print(f"Events in calendar: {events}")
            upcoming_events.extend(events)
        return sorted(upcoming_events, key=lambda event: event.start_date)
