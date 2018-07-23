class Entry:
    def __init__(self, title, date, entryBody, entry_id):
        self.title = title
        self.entryBody = entryBody
        self.date = date


    def __repr__(self):
        return repr(self.__dict__)

entries = []