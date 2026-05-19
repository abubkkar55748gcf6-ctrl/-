import requests

KALI_IP = '192.168.1.5'
PORT = '5000'

while True:
    cmd = input('Enter command (open/close): ')

    try:
        r = requests.post(
            f'http://{KALI_IP}:{PORT}/cmd',
            data={'command': cmd}
        )

        print('Server:', r.text)

    except Exception as e:
        print('Error:', e)
