from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "O. Vanshika Reddy" 
    system_username = os.getenv("USER") 
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    top= subprocess.getoutput('top -bn1 | head -10')


    return f"""
    <html>
    <body>
        <p><b>Name:</b> {name}</p>
        <p><b>Username:</b> {system_username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>Top Command Output:</h2>
        <pre>{top}</pre>
    </body>
    </html>
    """

if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000, debug=True)