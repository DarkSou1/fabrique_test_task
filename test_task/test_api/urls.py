from django.urls import path

from .views import (ClientDetail, ClientViewList,
                    DistributionViewList, DistributionDetail,
                    MessageViewList)


urlpatterns = [
    path('v1/client/', ClientViewList.as_view()),
    path('v1/client/<int:pk>/', ClientDetail.as_view()),
    path('v1/distribution/', DistributionViewList.as_view()),
    path('v1/distribution/<int:pk>/', DistributionDetail.as_view()),
    path('v1/message/', MessageViewList.as_view())
]
