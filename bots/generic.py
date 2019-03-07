import threading


class Bot(threading.Thread):
    def __init__(self, defn, gargs, o_queue, i_queue):
        self.defn = defn
        self.gargs = gargs
        self.o_queue = o_queue
        self.i_queue = i_queue
        self.closing = False

        self.name = defn["name"]
        self.platform = defn["platform"]
        self.prefixes = defn["prefixes"]

    def run(self):
        self.startup()
        while not self.closing:
            self.loop()
        self.end()

    def shutdown(self):
        """Shutdown gracefully."""
        self.closing = True

    def restart(self):
        self.shutdown()
        self.send('restart')

    def save(self):
        self.send('save')

    def send(self, message):
        m = self.name + ' ' + self.service + ' ' + message
        self.iqueue.put(m)

    def add_cmd(self, name, function):
        pass

    def del_cmd(self, command):
        pass

    def run_cmd(self, command, args):
        pass

   # def check_perms(self):
   #     # checks black / whitelists, can be overridden for other services
   #     pass

    def startup(self):
        raise NotImplementedError("Method startup() is not implemented.")

    def loop(self):
        raise NotImplementedError("Method loop() is not implemented.")

    def end(self):
        raise NotImplementedError("Method startup() is not implemented.")

    def say(self):
        raise NotImplementedError("Method say() is not implemented.")
