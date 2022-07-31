#python3
#PyQt5
#todoist API
#C:\Users\halaz\OneDrive\Документы\GitHub\stats_todoist


from todoist_api_python.api import TodoistAPI

api = TodoistAPI('')

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)