class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on == False:
            self.is_on = True

    def install(self, app: str, app_memory: int):

        if self.memory >= app_memory and self.is_on == True:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"

        if self.memory >= app_memory and self.is_on == False:
            return f"Turn on your phone to install {app}"

        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

