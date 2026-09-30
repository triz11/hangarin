from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    context = {
        'total_tasks': 12,
        'total_notes': 25,
        'total_subtasks': 21,
        'recent_tasks': [
            {'title': 'Complete Django OAuth authentication setup', 'status': 'Completed', 'priority': 'High', 'category': 'Development', 'deadline': 'Sept. 28, 2026, 10:00 a.m.'},
            {'title': 'Configure PythonAnywhere proxy and WSGI settings', 'status': 'Completed', 'priority': 'High', 'category': 'Deployment', 'deadline': 'Sept. 29, 2026, 2:30 p.m.'},
            {'title': 'Design Bootstrap dashboard template', 'status': 'In Progress', 'priority': 'Medium', 'category': 'UI/UX', 'deadline': 'Oct. 2, 2026, 5:00 p.m.'},
            {'title': 'Create Task and Note database models', 'status': 'Pending', 'priority': 'High', 'category': 'Backend', 'deadline': 'Oct. 5, 2026, 11:59 p.m.'},
            {'title': 'Write unit tests for custom user login flows', 'status': 'Pending', 'priority': 'Optional', 'category': 'Testing', 'deadline': 'Oct. 10, 2026, 4:00 p.m.'},
        ]
    }
    return render(request, 'dashboard.html', context)