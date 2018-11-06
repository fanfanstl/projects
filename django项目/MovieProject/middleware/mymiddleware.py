from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print(request.path)
