from . import views
from django.urls import path



urlpatterns = [
    #-------------------------Manual path segment------------------------------------#
    path("Index",views.index),
  # path("January",views.january),
  # path("February",views.february),
  # path("March",views.march),
  # path("April",views.april),
  # path("May",views.may),
  # path("June",views.june),
  # path("July",views.july),
  # path("August",views.august),
  # path("September",views.september),
  # path("October",views.october),
  # path("November",views.november),
  # path("December",views.december)
# -------------------------------Dynamic path segment-------------------------------- #
  path("<int:month>",views.monthly_challanges_by_number),
  path("<str:month>",views.monthly_challanges)

]