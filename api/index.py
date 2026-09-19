import sys
import os

# Ensure the project root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

class VercelMiddleware:
    """WSGI Middleware to restore original request path on Vercel rewrites."""
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # Vercel sends the client request path in HTTP_X_MATCHED_PATH or REQUEST_URI
        matched = environ.get('HTTP_X_MATCHED_PATH') or environ.get('REQUEST_URI')
        if matched:
            environ['PATH_INFO'] = matched.split('?')[0]
        else:
            pi = environ.get('PATH_INFO', '')
            for prefix in ['/api/index.py', '/api/index', '/api']:
                if pi.startswith(prefix):
                    pi = pi[len(prefix):]
                    break
            environ['PATH_INFO'] = pi if pi else '/'

        return self.wsgi_app(environ, start_response)

# Vercel serverless WSGI entrypoint
app = VercelMiddleware(app)
