import time
import logging
audit_logger = logging.getLogger("audit")

class ReadAuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        ms = int((time.time() - start) * 1000)

        if request.method in ("GET", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"):
            if request.path.startswith("/static/"):
                return response

            actor = request.user.pk if hasattr(request, "user") and request.user.is_authenticated else None
            audit_logger.info(
                "request method=%s path=%s status=%s ms=%s actor=%s",
                request.method, request.path, response.status_code, ms, actor
            )
        return response
