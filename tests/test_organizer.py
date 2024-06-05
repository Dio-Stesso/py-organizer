import unittest
from datetime import datetime, timedelta
from organizer import Organizer
from organizer_event import OrganizerEvent


class TestOrganizer(unittest.TestCase):
    def setUp(self):
        self.organizer = Organizer()
        self.organizer.create_calendar("Work")
        now = datetime.now()
        self.event1 = OrganizerEvent("Meeting", now + timedelta(days=1), now + timedelta(days=1), "Work")
        self.event2 = OrganizerEvent("Conference", now + timedelta(days=5), now + timedelta(days=5), "Work")
        self.organizer.get_calendar("Work").add_event(self.event1)
        self.organizer.get_calendar("Work").add_event(self.event2)

    def test_create_calendar(self):
        self.assertIn("Work", self.organizer.calendars)

    def test_delete_calendar(self):
        self.organizer.delete_calendar("Work")
        self.assertNotIn("Work", self.organizer.calendars)

    def test_get_calendar(self):
        calendar = self.organizer.get_calendar("Work")
        self.assertIsNotNone(calendar)

    def test_get_upcoming_events(self):
        upcoming_events = self.organizer.get_upcoming_events(days=10)
        print(f"Upcoming events: {upcoming_events}")  # Debugging statement
        self.assertIn(self.event1, upcoming_events)
        self.assertIn(self.event2, upcoming_events)


if __name__ == "__main__":
    unittest.main()
