from django.urls import path
from . import views

app_name = 'ag360l_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('ag360l_app/rev/<int:num>', views.rev, name='rev'),
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
     'mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
 ),
]

