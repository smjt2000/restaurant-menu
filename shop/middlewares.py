class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)

        response = self.get_response(request)

        self.process_response(request, response)

        return response

    def process_request(self, request):
        print(f"Processing request for: {request.path}")

        request.custom_header = "Custom Value"

        pass

    def process_response(self, request, response):
        print(f"Response status code: {response.status_code}")

        response['X-Custom-Header'] = "Custom Value"

        return response
