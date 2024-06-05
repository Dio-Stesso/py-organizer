from event import Event
from datetime import datetime, timedelta

class CalendarEvent(Event):
    def __init__(self, title, start_date, end_date, category, periodicity=None):
        super().__init__(title, start_date, end_date, category)
        self.periodicity = periodicity

    def occurs_on(self, date):
        if self.periodicity is None:
            return self.start_date <= date <= self.end_date
        else:
            return self._occurs_periodically(date)

    def _occurs_periodically(self, date):
        if self.periodicity == 'daily':
            delta = (date - self.start_date).days
            return delta >= 0 and (date <= self.end_date) and delta % 1 == 0
        elif self.periodicity == 'weekly':
            delta = (date - self.start_date).days
            return delta >= 0 and (date <= self.end_date) and delta % 7 == 0
        elif self.periodicity == 'monthly':
            if date < self.start_date or date > self.end_date:
                return False
            if self.start_date.day != date.day:
                return False
            month_diff = (date.year - self.start_date.year) * 12 + date.month - self.start_date.month
            return month_diff % 1 == 0
        elif self.periodicity == 'yearly':
            if date < self.start_date or date > self.end_date:
                return False
            return self.start_date.month == date.month and self.start_date.day == date.day
        return False

    def __repr__(self):
        return f"CalendarEvent(title={self.title}, start_date={self.start_date}, end_date={self.end_date}, category={self.category}, periodicity={self.periodicity})"
