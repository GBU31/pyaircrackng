from subprocess import check_output


def is_installed():
    try:
        proc = check_output(['dpkg', '-s', 'aircrack-ng'])
        return True
    except:
        return False
    
