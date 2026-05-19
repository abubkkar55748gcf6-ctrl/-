from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

browser_process = None

HTML_FILE = os.path.expanduser('~/Desktop/zubair.html')

@app.route('/cmd', methods=['POST'])
def cmd():
    global browser_process

    data = request.form.get('command')

    if data == 'open':
        if os.path.exists(HTML_FILE):
            browser_process = subprocess.Popen([
                'xdg-open',
                HTML_FILE
            ])
            return 'HTML Opened'
        else:
            return 'File Not Found'

    elif data == 'close':
        os.system('pkill firefox')
        os.system('pkill chrome')
        os.system('pkill chromium')
        return 'Browser Closed'

    return 'Unknown Command'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
