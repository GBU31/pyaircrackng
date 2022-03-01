from subprocess import check_output


class airmon:
    def __init__(self, i):
        self.i = i

    def start(self):
        proc = check_output(['sudo', 'airmon-ng', 'start', self.i])
        return proc
        
    def stop(self):
        proc = check_output(['sudo', 'airmon-ng', 'stop', self.i+'mon'])
        return proc

    def check(self):
        proc = check_output(['sudo', 'airmon-ng', 'check'])
        return proc

