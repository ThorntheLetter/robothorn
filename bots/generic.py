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

        self.commands = {}

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
        modulen = function.rsplit('.', 1)[0]
        __import__(modulen)

        f = globals()[modulen]
        for name in function.split('.')[1:]:
            f = getattr(f, name)
        self.commands[name] = f

        self.defn[name] = function

    def del_cmd(self, command):
        del self.commands[command]
        del self.defn[name]

    def run_cmd(self, command, text):
        ret = self.commands['command'](text, self.args)
        for cmd in ret:
            c, t = cmd.split(' ', 1)
            run_cmd(c, t, args)

    def parse_message(self, text):
        text2 = ""
        for prefix in self.prefixes:
            if(text.startswith(prefix):
                text2 = text[len(prefix):]
                break

        cmd, txt = text2.split(' ', 1)
        self.run_cmd(cmd, txt)

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
