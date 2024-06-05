import unittest
from datetime import datetime, timedelta
from organizer_event import OrganizerEvent


class TestOrganizerEvent(unittest.TestCase):
    def test_add_reminder(self):
        event = OrganizerEvent("Meeting", datetime(2023, 6, 5), datetime(2023, 6, 5), "Work")
        reminder_time = datetime.now() + timedelta(hours=1)
        event.add_reminder(reminder_time)
        self.assertIn(reminder_time, event.reminders)

    def test_get_upcoming_reminders(self):
        event = OrganizerEvent("Meeting", datetime(2023, 6, 5), datetime(2023, 6, 5), "Work")
        reminder_time = datetime.now() + timedelta(hours=1)
        event.add_reminder(reminder_time)
        upcoming_reminders = event.get_upcoming_reminders()
        self.assertIn(reminder_time, upcoming_reminders)


if __name__ == "__main__":
    unittest.main()
