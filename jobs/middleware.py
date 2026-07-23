from datetime import datetime

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Format current timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        
        # Log request information to terminal console
        print("---------------------------------")
        print(f"Time : {current_time}")
        print(f"Method : {request.method}")
        print(f"Path : {request.path}")
        print("---------------------------------")

        response = self.get_response(request)
        return response