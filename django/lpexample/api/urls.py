
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
# router.register('register',views.UserView,basename='register')
router.register('api/employee',views.EmployeeView,basename='employee')

router.register('employedetails',views.EmployeeDetailView,basename='employee-detail')



urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('register/',views.UserView.as_view()),  
    path('login/refresh/',TokenRefreshView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('logout/',views.LogoutView.as_view(), name='logout'),

    
]+router.urls
