import unittest
from datetime import datetime
from event import Event


class TestEvent(unittest.TestCase):
    def test_event_creation(self):
        event = Event("Meeting", datetime(2023, 6, 5), datetime(2023, 6, 5), "Work")
        self.assertEqual(event.title, "Meeting")
        self.assertEqual(event.start_date, datetime(2023, 6, 5))
        self.assertEqual(event.end_date, datetime(2023, 6, 5))
        self.assertEqual(event.category, "Work")


if __name__ == "__main__":
    unittest.main()
