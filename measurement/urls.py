from django.urls import path
from measurement.views import SensorView, SensorDetail, MeasureDetail, MeasureView
urlpatterns = [ 
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorDetail.as_view()),
    path('measurements/', MeasureView.as_view()),
    path('measurements/<pk>/', MeasureDetail.as_view()),
]
