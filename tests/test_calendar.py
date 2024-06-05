import unittest
from datetime import datetime
from calendar import Calendar
from organizer_event import OrganizerEvent


class TestCalendar(unittest.TestCase):
    def setUp(self):
        self.calendar = Calendar()
        self.event1 = OrganizerEvent("Meeting", datetime(2023, 6, 5), datetime(2023, 6, 5), "Work")
        self.event2 = OrganizerEvent("Conference", datetime(2023, 6, 10), datetime(2023, 6, 10), "Work")
        self.calendar.add_event(self.event1)
        self.calendar.add_event(self.event2)

    def test_add_event(self):
        self.assertIn(self.event1, self.calendar.events)
        self.assertIn(self.event2, self.calendar.events)

    def test_remove_event(self):
        self.calendar.remove_event(self.event1)
        self.assertNotIn(self.event1, self.calendar.events)

    def test_update_event(self):
        new_event = OrganizerEvent("New Meeting", datetime(2023, 6, 6), datetime(2023, 6, 6), "Work")
        self.calendar.update_event(self.event1, new_event)
        self.assertIn(new_event, self.calendar.events)
        self.assertNotIn(self.event1, self.calendar.events)

    def test_find_events_by_date(self):
        events = self.calendar.find_events_by_date(datetime(2023, 6, 5))
        self.assertIn(self.event1, events)
        self.assertNotIn(self.event2, events)

    def test_find_events_by_date_range(self):
        events = self.calendar.find_events_by_date_range(datetime(2023, 6, 5), datetime(2023, 6, 10))
        self.assertIn(self.event1, events)
        self.assertIn(self.event2, events)

    def test_sort_events_by_date(self):
        sorted_events = self.calendar.sort_events_by_date()
        self.assertEqual(sorted_events, [self.event1, self.event2])

    def test_sort_events_by_category(self):
        sorted_events = self.calendar.sort_events_by_category()
        self.assertEqual(sorted_events, [self.event1, self.event2])


if __name__ == "__main__":
    unittest.main()
