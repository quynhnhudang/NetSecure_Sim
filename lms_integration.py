import requests

# Send user progress to LMS
progress_data = {'user_id': 1, 'scenario_id': 2, 'score': 85}
response = requests.post('https://lms.example.com/progress', json=progress_data)
print(response.status_code)
