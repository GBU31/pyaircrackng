from subprocess import check_output

class airodump:
    def __init__(self, c):
        self.c = c

    def run(self):
        c = 'sudo airodump-ng' + ' ' + self.c
        l = [i for i in c.split()]
        return check_output(l)
