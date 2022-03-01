from subprocess import check_output


class aireplay:
    def __init__(self, c):
        self.c = c

    def run(self):
        c = 'sudo aireplay-ng' + ' ' + self.c
        l = [i for i in c.split()]
        return check_output(l)
        
