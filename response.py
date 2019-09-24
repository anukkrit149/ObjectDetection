import requests


API="https://inspicons.co.in/policeapi/info.php?lat=51.507351&long=-0.127758&type=car%20acccident"
r = requests.get('https://github.com/timeline.json')
r.json()