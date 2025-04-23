class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.organizers = []
        self.participants = []
        self.activities = []

    def add_organizer(self, organizer):
        self.organizers.append(organizer)

    def register_participant(self, participant):
        self.participants.append(participant)

    def add_activity(self, activity):
        self.activities.append(activity)

    def event_details(self):
        return f"Event: {self.name}\nDate: {self.date}\nLocation: {self.location}\nTotal Participants: {len(self.participants)}\nTotal Activities: {len(self.activities)}"


class Organizer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def organize_event(self, event):
        event.add_organizer(self)

    def organizer_details(self):
        return f"Organizer: {self.name}, Contact: {self.contact}"


class Participant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def register_for_event(self, event):
        event.register_participant(self)

    def participant_details(self):
        return f"Participant: {self.name}, Age: {self.age}"


class Activity:
    def __init__(self, name, time, coordinator):
        self.name = name
        self.time = time
        self.coordinator = coordinator

    def activity_details(self):
        return f"Activity: {self.name}\nTime: {self.time}\nCoordinator: {self.coordinator}"


# Example Usage
#event = Event("College Fest", "2025-03-15", "Main Auditorium")

organizer1 = Organizer("John Doe", "123-456-7890")
organizer1.organize_event(event)

participant1 = Participant("Alice", 20)
participant2 = Participant("Bob", 22)
participant1.register_for_event(event)
participant2.register_for_event(event)

activity1 = Activity("Music Competition", "10:00 AM", "Prof. Smith")
event.add_activity(activity1)

# Displaying Event Details
print(event.event_details())
