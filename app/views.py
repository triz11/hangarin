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

@login_required
def tasks_view(request):
    context = {
        'tasks': [
            {'title': 'Set up Celery asynchronous task queue', 'status': 'In Progress', 'priority': 'High', 'category': 'Backend', 'deadline': 'Oct. 3, 2026, 11:00 a.m.'},
            {'title': 'Implement Redis caching for API responses', 'status': 'Completed', 'priority': 'Medium', 'category': 'Performance', 'deadline': 'Sept. 27, 2026, 4:15 p.m.'},
            {'title': 'Draft software architecture diagram', 'status': 'Completed', 'priority': 'Low', 'category': 'Documentation', 'deadline': 'Sept. 24, 2026, 9:00 a.m.'},
            {'title': 'Configure HTTPS SSL certificates on domain', 'status': 'Pending', 'priority': 'High', 'category': 'Security', 'deadline': 'Oct. 6, 2026, 2:30 p.m.'},
            {'title': 'Build user profile photo upload functionality', 'status': 'In Progress', 'priority': 'Medium', 'category': 'UI/UX', 'deadline': 'Oct. 8, 2026, 6:00 p.m.'},
            {'title': 'Refactor database migrations for production deployment', 'status': 'Completed', 'priority': 'High', 'category': 'Database', 'deadline': 'Sept. 26, 2026, 1:00 p.m.'},
            {'title': 'Integrate Stripe payment gateway webhooks', 'status': 'Pending', 'priority': 'High', 'category': 'Finance', 'deadline': 'Oct. 12, 2026, 5:00 p.m.'},
            {'title': 'Create automated daily database backup script', 'status': 'Completed', 'priority': 'Medium', 'category': 'DevOps', 'deadline': 'Sept. 21, 2026, 8:00 a.m.'},
            {'title': 'Design dark mode color scheme for dashboard', 'status': 'Pending', 'priority': 'Optional', 'category': 'UI/UX', 'deadline': 'Oct. 15, 2026, 3:45 p.m.'},
            {'title': 'Conduct accessibility audit for WCAG compliance', 'status': 'Pending', 'priority': 'Medium', 'category': 'Testing', 'deadline': 'Oct. 18, 2026, 10:30 a.m.'},
            {'title': 'Set up Prometheus and Grafana system monitoring', 'status': 'In Progress', 'priority': 'High', 'category': 'Infrastructure', 'deadline': 'Oct. 22, 2026, 1:15 p.m.'},
            {'title': 'Write API documentation using Swagger UI', 'status': 'Pending', 'priority': 'Low', 'category': 'Documentation', 'deadline': 'Oct. 25, 2026, 4:00 p.m.'},
        ]
    }
    return render(request, 'tasks.html', context)

@login_required
def notes_view(request):
    context = {
        'notes': [
            {'task': 'Database Indexing Optimization', 'content': 'Added composite index on user_id and created_at to speed up dashboard query execution time by 40%.', 'created': 'Sep. 30, 2026, 8:45 a.m.'},
            {'task': 'GraphQL API Migration', 'content': 'Evaluated Strawberry vs Graphene packages; decided on Strawberry for modern Python type hints support.', 'created': 'Sep. 29, 2026, 3:20 p.m.'},
            {'task': 'Docker Containerization', 'content': 'Multi-stage build reduced final container image size from 1.2GB down to 180MB.', 'created': 'Sep. 28, 2026, 11:10 a.m.'},
            {'task': 'Email Notification System', 'content': 'Integrated SendGrid API for transactional emails and configured SPF and DKIM DNS records.', 'created': 'Sep. 27, 2026, 5:00 p.m.'},
            {'task': 'Two-Factor Authentication (2FA)', 'content': 'Implemented TOTP using django-two-factor-auth with automated recovery codes generation.', 'created': 'Sep. 26, 2026, 2:15 p.m.'},
            {'task': 'Frontend Internationalization (i18n)', 'content': 'Added support for English and Tagalog language translations using Django gettext framework.', 'created': 'Sep. 25, 2026, 10:30 a.m.'},
            {'task': 'Session Timeout Policy', 'content': 'Set SESSION_COOKIE_AGE to 3600 seconds and enabled SESSION_SAVE_EVERY_REQUEST.', 'created': 'Sep. 24, 2026, 4:40 p.m.'},
            {'task': 'File Upload S3 Bucket Configuration', 'content': 'Configured AWS S3 bucket policies to block public access and serve media via CloudFront CDN.', 'created': 'Sep. 23, 2026, 1:00 p.m.'},
            {'task': 'CI/CD Pipeline Setup', 'content': 'Created GitHub Actions workflow to automatically run Pytest suite and deploy to staging on push.', 'created': 'Sep. 22, 2026, 9:15 a.m.'},
            {'task': 'User Onboarding Tour', 'content': 'Added Shepherd.js walkthrough guide to introduce new users to core dashboard features.', 'created': 'Sep. 21, 2026, 6:50 p.m.'},
        ]
    }
    return render(request, 'notes.html', context)

@login_required
def subtasks_view(request):
    context = {
        'subtasks': [
            {'task': 'Server Infrastructure Migration', 'title': 'Provision EC2 compute instances on AWS', 'status': 'Completed'},
            {'task': 'Customer Support Portal', 'title': 'Design ticket submission form layout', 'status': 'In Progress'},
            {'task': 'Data Export Feature', 'title': 'Implement CSV generator background task', 'status': 'Pending'},
            {'task': 'OAuth2 Provider Integration', 'title': 'Register developer credentials on Google Cloud Console', 'status': 'Completed'},
            {'task': 'Mobile Responsiveness Overhaul', 'title': 'Fix horizontal scrolling bug on mobile viewports', 'status': 'In Progress'},
            {'task': 'Search Bar Auto-complete', 'title': 'Build debounced REST API endpoint for search queries', 'status': 'Pending'},
            {'task': 'User Permission Roles', 'title': 'Define admin, manager, and guest user group permissions', 'status': 'Completed'},
            {'task': 'Analytics Dashboard Charts', 'title': 'Integrate Chart.js for monthly active user graphs', 'status': 'In Progress'},
            {'task': 'Password Reset Workflow', 'title': 'Create password reset email template with secure token', 'status': 'Pending'},
            {'task': 'System Logging Standard', 'title': 'Configure Python logging module with JSON formatting', 'status': 'Completed'},
        ]
    }
    return render(request, 'subtasks.html', context)