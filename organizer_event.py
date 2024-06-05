from calendar_event import CalendarEvent
from datetime import datetime


class OrganizerEvent(CalendarEvent):
    def __init__(self, title, start_date, end_date, category, periodicity=None):
        super().__init__(title, start_date, end_date, category, periodicity)
        self.reminders = []

    def add_reminder(self, reminder_time):
        self.reminders.append(reminder_time)

    def get_upcoming_reminders(self):
        now = datetime.now()
        return [reminder for reminder in self.reminders if reminder > now]

    def __repr__(self):
        return (f"OrganizerEvent(title={self.title}, start_date={self.start_date}, end_date={self.end_date}, "
                f"category={self.category}, periodicity={self.periodicity}, reminders={self.reminders})")
