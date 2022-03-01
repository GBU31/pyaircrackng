from subprocess import check_output


class aircrack:
    def __init__(self, c):
        self.c = c

    def run(self):
        c = 'sudo aircrack-ng' + ' ' + self.c
        l = [i for i in c.split()]
        return check_output(l)
        
