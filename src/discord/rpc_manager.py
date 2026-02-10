import pypresence
import time

class DiscordRPCManager:
    def __init__(self, client_id):
        self.client_id = client_id
        self.p = pypresence.Presence(client_id)
        self.p.connect()

    def update_activity(self, state, details, start=None, end=None, large_image=None, small_image=None):
        self.p.update(state=state, details=details, start=start, end=end, large_image=large_image, small_image=small_image)

    def clear_activity(self):
        self.p.clear()

    def close(self):
        self.p.close()