from .profile_selector import ProfileSelector


class ProfileEngine:

    def __init__(self):
        self.selector = ProfileSelector()

    def activate(self, profile):
        return self.selector.activate(profile)
