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
            {'title': 'Complete Django OAuth authentication setup', 'status': 'Completed', 'priority': 'High', 'category': 'Development', 'deadline': 'Sept. 28, 2026, 10:00 a.m.'},
            {'title': 'Configure PythonAnywhere proxy and WSGI settings', 'status': 'Completed', 'priority': 'High', 'category': 'Deployment', 'deadline': 'Sept. 29, 2026, 2:30 p.m.'},
            {'title': 'Design Bootstrap dashboard template', 'status': 'In Progress', 'priority': 'Medium', 'category': 'UI/UX', 'deadline': 'Oct. 2, 2026, 5:00 p.m.'},
            {'title': 'Create Task and Note database models', 'status': 'Pending', 'priority': 'High', 'category': 'Backend', 'deadline': 'Oct. 5, 2026, 11:59 p.m.'},
            {'title': 'Write unit tests for custom user login flows', 'status': 'Pending', 'priority': 'Optional', 'category': 'Testing', 'deadline': 'Oct. 10, 2026, 4:00 p.m.'},
            {'title': 'Set up Celery asynchronous task queue', 'status': 'In Progress', 'priority': 'High', 'category': 'Backend', 'deadline': 'Oct. 12, 2026, 11:00 a.m.'},
            {'title': 'Implement Redis caching for API responses', 'status': 'Completed', 'priority': 'Medium', 'category': 'Performance', 'deadline': 'Sept. 27, 2026, 4:15 p.m.'},
            {'title': 'Configure HTTPS SSL certificates on domain', 'status': 'Pending', 'priority': 'High', 'category': 'Security', 'deadline': 'Oct. 14, 2026, 2:30 p.m.'},
            {'title': 'Build user profile photo upload functionality', 'status': 'In Progress', 'priority': 'Medium', 'category': 'UI/UX', 'deadline': 'Oct. 16, 2026, 6:00 p.m.'},
            {'title': 'Refactor database migrations for production', 'status': 'Completed', 'priority': 'High', 'category': 'Database', 'deadline': 'Sept. 26, 2026, 1:00 p.m.'},
            {'title': 'Integrate Stripe payment gateway webhooks', 'status': 'Pending', 'priority': 'High', 'category': 'Finance', 'deadline': 'Oct. 20, 2026, 5:00 p.m.'},
            {'title': 'Set up Prometheus and Grafana system monitoring', 'status': 'In Progress', 'priority': 'Optional', 'category': 'Infrastructure', 'deadline': 'Oct. 22, 2026, 1:15 p.m.'},
        ]
    }
    return render(request, 'tasks.html', context)

@login_required
def notes_view(request):
    context = {
        'notes': [
            {'task': 'Database Indexing', 'content': 'Added composite index on user_id and created_at to speed up query response.', 'created': 'Sep. 30, 2026, 8:45 a.m.'},
            {'task': 'GraphQL Evaluation', 'content': 'Compared Strawberry vs Graphene; selected Strawberry for modern Python type hints.', 'created': 'Sep. 29, 2026, 3:20 p.m.'},
            {'task': 'Docker Multi-stage Build', 'content': 'Multi-stage build reduced final web server container image size from 1.2GB to 180MB.', 'created': 'Sep. 28, 2026, 11:10 a.m.'},
            {'task': 'SendGrid Integration', 'content': 'Configured SPF and DKIM DNS records for transactional email verification.', 'created': 'Sep. 27, 2026, 5:00 p.m.'},
            {'task': 'TOTP 2FA Setup', 'content': 'Implemented django-two-factor-auth with automated single-use recovery code generation.', 'created': 'Sep. 26, 2026, 2:15 p.m.'},
            {'task': 'i18n Translation', 'content': 'Added initial English and Tagalog translation dictionary files using gettext.', 'created': 'Sep. 25, 2026, 10:30 a.m.'},
            {'task': 'Session Security', 'content': 'Set SESSION_COOKIE_AGE to 3600 seconds with automatic refresh on active requests.', 'created': 'Sep. 24, 2026, 4:40 p.m.'},
            {'task': 'S3 Bucket Policy', 'content': 'Enforced private ACLs on media buckets and configured signed CloudFront URLs.', 'created': 'Sep. 23, 2026, 1:00 p.m.'},
            {'task': 'CI/CD Pipeline', 'content': 'Created GitHub Actions pipeline for automated Pytest suite execution on pull requests.', 'created': 'Sep. 22, 2026, 9:15 a.m.'},
            {'task': 'Shepherd.js Walkthrough', 'content': 'Configured interactive step-by-step tour for first-time dashboard visitors.', 'created': 'Sep. 21, 2026, 6:50 p.m.'},
            {'task': 'OAuth Callback Handling', 'content': 'Handled edge cases where social login users decline email permissions.', 'created': 'Sep. 20, 2026, 4:10 p.m.'},
            {'task': 'PythonAnywhere Proxy', 'content': 'Configured FORCE_SCRIPT_NAME in settings.py for proper subpath routing.', 'created': 'Sep. 19, 2026, 2:25 p.m.'},
            {'task': 'CSRF Token Cookie', 'content': 'Set CSRF_COOKIE_HTTPONLY to True to secure sessions against XSS script access.', 'created': 'Sep. 18, 2026, 11:45 a.m.'},
            {'task': 'PostgreSQL Pooler', 'content': 'Configured PgBouncer connection pooling to avoid max database connection limits.', 'created': 'Sep. 17, 2026, 10:05 a.m.'},
            {'task': 'Gunicorn Workers', 'content': 'Set worker count formula to (2 * CPU_CORES) + 1 for optimized concurrency.', 'created': 'Sep. 16, 2026, 3:30 p.m.'},
            {'task': 'Static File Compression', 'content': 'Integrated Whitenoise with Brotli storage backend for auto-compressed static assets.', 'created': 'Sep. 15, 2026, 1:15 p.m.'},
            {'task': 'Tailwind Integration', 'content': 'Compiled custom utility classes to standalone CSS bundle for standalone templates.', 'created': 'Sep. 14, 2026, 9:00 a.m.'},
            {'task': 'Rate Limiting', 'content': 'Added django-ratelimit middleware to prevent brute-force attacks on login endpoints.', 'created': 'Sep. 13, 2026, 5:40 p.m.'},
            {'task': 'Custom Exception Handlers', 'content': 'Created unified JSON error response format for HTTP 404 and HTTP 500 status codes.', 'created': 'Sep. 12, 2026, 12:20 p.m.'},
            {'task': 'Sentry Error Capture', 'content': 'Filtered out known unhandled HTTP 404 client errors from Sentry event quota.', 'created': 'Sep. 11, 2026, 8:15 a.m.'},
            {'task': 'Redis Key Expiration', 'content': 'Set default TTL on session keys to 14 days to prevent cache store memory bloat.', 'created': 'Sep. 10, 2026, 4:30 p.m.'},
            {'task': 'Database Backup Script', 'content': 'Wrote bash script to run daily pg_dump export and sync dumps directly to S3.', 'created': 'Sep. 09, 2026, 2:10 p.m.'},
            {'task': 'User Avatar Resize', 'content': 'Integrated Pillow library to automatically compress user profile images down to 300x300px.', 'created': 'Sep. 08, 2026, 11:00 a.m.'},
            {'task': 'PWA Web Manifest', 'content': 'Created manifest.json file to enable progressive app installation on mobile screens.', 'created': 'Sep. 07, 2026, 3:45 p.m.'},
            {'task': 'Webhook Signature Check', 'content': 'Added SHA-256 HMAC signature validation to verify incoming Stripe webhook payloads.', 'created': 'Sep. 06, 2026, 1:30 p.m.'},
        ]
    }
    return render(request, 'notes.html', context)

@login_required
def subtasks_view(request):
    context = {
        'subtasks': [
            {'task': 'Complete Django OAuth authentication setup', 'title': 'Register app on Google Cloud Console', 'status': 'Completed'},
            {'task': 'Complete Django OAuth authentication setup', 'title': 'Store client secrets in environment variables', 'status': 'Completed'},
            {'task': 'Configure PythonAnywhere proxy and WSGI settings', 'title': 'Set virtualenv folder in wsgi.py configuration', 'status': 'Completed'},
            {'task': 'Design Bootstrap dashboard template', 'title': 'Build responsive top navigation bar', 'status': 'Completed'},
            {'task': 'Design Bootstrap dashboard template', 'title': 'Construct overview statistic card grid', 'status': 'In Progress'},
            {'task': 'Create Task and Note database models', 'title': 'Define priority and status ENUM field choices', 'status': 'Pending'},
            {'task': 'Create Task and Note database models', 'title': 'Execute makemigrations and migrate scripts', 'status': 'Pending'},
            {'task': 'Write unit tests for custom user login flows', 'title': 'Test login form with valid credentials', 'status': 'Pending'},
            {'task': 'Write unit tests for custom user login flows', 'title': 'Assert HTTP 400 response on wrong password', 'status': 'Pending'},
            {'task': 'Set up Celery asynchronous task queue', 'title': 'Configure Celery broker URL with Redis connection', 'status': 'In Progress'},
            {'task': 'Set up Celery asynchronous task queue', 'title': 'Create initial background email delivery task', 'status': 'Pending'},
            {'task': 'Implement Redis caching for API responses', 'title': 'Install django-redis dependency library', 'status': 'Completed'},
            {'task': 'Configure HTTPS SSL certificates on domain', 'title': 'Generate Let\'s Encrypt SSL certificate via Certbot', 'status': 'Pending'},
            {'task': 'Build user profile photo upload functionality', 'title': 'Create form file input field with image validation', 'status': 'In Progress'},
            {'task': 'Build user profile photo upload functionality', 'title': 'Write image cropper module using JavaScript', 'status': 'Pending'},
            {'task': 'Refactor database migrations for production', 'title': 'Squash intermediate database migration files', 'status': 'Completed'},
            {'task': 'Integrate Stripe payment gateway webhooks', 'title': 'Add webhook endpoint route in core/urls.py', 'status': 'Pending'},
            {'task': 'Integrate Stripe payment gateway webhooks', 'title': 'Test subscription renewal event handling', 'status': 'Pending'},
            {'task': 'Set up Prometheus and Grafana system monitoring', 'title': 'Install django-prometheus exporter app', 'status': 'In Progress'},
            {'task': 'Set up Prometheus and Grafana system monitoring', 'title': 'Configure dashboard panel for memory usage', 'status': 'Pending'},
            {'task': 'Set up Prometheus and Grafana system monitoring', 'title': 'Set alert trigger for response latencies above 2s', 'status': 'Pending'},
        ]
    }
    return render(request, 'subtasks.html', context)