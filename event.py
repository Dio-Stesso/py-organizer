class Event:
    def __init__(self, title, start_date, end_date, category):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.category = category

    def __repr__(self):
        return f"Event(title={self.title}, start_date={self.start_date}, end_date={self.end_date}, category={self.category})"
