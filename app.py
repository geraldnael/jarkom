from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def scan_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error:
        return "Unable to resolve the hostname."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    website = request.form['website']
    ip_address = scan_ip_address(website)
    return render_template('result.html', website=website, ip_address=ip_address)

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run()
