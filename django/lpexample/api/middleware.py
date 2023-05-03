
# from datetime import datetime


# import datetime
# from django.core.cache import cache
# from django.conf import settings
# from django.utils.deprecation import MiddlewareMixin

# class SimpleMiddleware(MiddlewareMixin):
#        def process_view(self,request, view_func, view_args, view_kwargs):
#               if request.user.is_authenticated:
#                 #      login_time=datetime.now()
#                 #      print(login_time)
#                      request.user.last_login = datetime.datetime.now()
#                      request.user.save()


# class SimpleMiddleware:

#     def process_request(self, request):
#         current_user = request.user
#         if request.user.is_authenticated:
#             now = datetime.datetime.now()
#             print("time:     ",now)
#             cache.set('seen_%s' % (current_user.username), now, 
#                            settings.USER_LASTSEEN_TIMEOUT)


# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request):
#         if request.user.is_authenticated:
#                      request.user.last_login = datetime.now()
#                      request.user.save()

#         response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        # return response