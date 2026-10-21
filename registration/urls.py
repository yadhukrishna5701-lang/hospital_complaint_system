from django.urls import path
from registration.views import SingUpview
from registration.views import ComplaintListCreateViews,ComplaintRetrieveUpdateDeleteViews
from registration.views import SummaryView,totalView,Group_by,Priority
urlpatterns=[

    path("signup/",SingUpview.as_view()),
    path("complaint/",ComplaintListCreateViews.as_view()),
    path("complaint/<int:pk>/",ComplaintRetrieveUpdateDeleteViews.as_view()),
    path("summary/",SummaryView.as_view()),
    path("total/",totalView.as_view()),
    path("count/",Group_by.as_view()),
    path("priority/",Priority.as_view()),
]