# Unused and not currently working, API requires PATCH for bulk operations
import json

class BulkApiMiddleware(object):
    def process_request(self, request):
        # Consider just testing the first character is speed becomes an issue
        try:
            obj = json.loads(request.body)
            if type(obj) is list and request.method == 'POST':
                # Add header to incoming requests to get tastypie to handle bulk
                # POST requests
                request['X-HTTP-Method-Override'] = 'PATCH'
                return None
        except ValueError:
            return None
