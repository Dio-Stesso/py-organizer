import unittest
from datetime import datetime
from calendar_event import CalendarEvent


class TestCalendarEvent(unittest.TestCase):
    def test_one_time_event_occurs_on(self):
        event = CalendarEvent("Meeting", datetime(2023, 6, 5), datetime(2023, 6, 5), "Work")
        self.assertTrue(event.occurs_on(datetime(2023, 6, 5)))
        self.assertFalse(event.occurs_on(datetime(2023, 6, 6)))

    def test_periodic_event_occurs_on(self):
        event = CalendarEvent("Daily Standup", datetime(2023, 6, 1), datetime(2023, 6, 30), "Work", "daily")
        self.assertTrue(event.occurs_on(datetime(2023, 6, 5)))
        self.assertFalse(event.occurs_on(datetime(2023, 7, 1)))


if __name__ == "__main__":
    unittest.main()
