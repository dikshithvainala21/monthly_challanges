from calendar import month

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def index(request):
#     return HttpResponse("<h1>Monthly Challenges</h1>" "<h2>DIKSHITH VAINALA</h2>" )

#----------------------Using Dictionary to store the monthly challenges-----------------------------#
monthly_challenges = {
    "january": "January is the first month of the year. It is generally cold in many parts of India, especially in the mornings and at night. People celebrate New Year on January 1 and Makar Sankranti or Pongal around January 14–15. Special days: New Year's Day, Republic Day (January 26).",
    "february": "February often brings pleasant weather, with temperatures beginning to rise in many regions. Flowers bloom, and the days gradually become warmer. Valentine's Day is celebrated on February 14.\nSpecial days: Valentine's Day, National Science Day (February 28).",
    "march": "March is a transitional month, with the arrival of spring in many parts of India. The weather becomes more comfortable, and people enjoy outdoor activities. Holi, the festival of colors, is celebrated in March.\nSpecial days: Holi, International Women's Day (March 8).",
    "april": "April is a month of new beginnings, with the full bloom of spring. The weather is generally warm and pleasant. People celebrate various festivals, including Baisakhi and Good Friday.\nSpecial days: Baisakhi, Good Friday.",
    "may": "May is a month of transition from spring to summer. The weather becomes hotter, and people often seek ways to stay cool. Many schools and colleges have their summer vacations during this time.\nSpecial days: Labor Day (May 1), Mother's Day.",
    "june": "June is the first month of summer in the Northern Hemisphere. The weather is generally warm, and people enjoy outdoor activities. Children often have their summer vacations during this time.\nSpecial days: World Environment Day (June 5), Father's Day.",
    "july": "July is a month of mid-summer, with hot and humid weather in many regions. People often take vacations to escape the heat. Independence Day is celebrated on July 4 in the United States.\nSpecial days: Independence Day (July 4), World Population Day (July 11).",
    "august": "August is a month of late summer, with warm weather continuing in many areas. People enjoy outdoor activities and vacations. Independence Day is celebrated on August 15 in India.\nSpecial days: Independence Day (August 15), Raksha Bandhan.",
    "september": "September is a month of transition from summer to autumn. The weather begins to cool down, and people prepare for the upcoming fall season. Teachers' Day is celebrated on September 5 in India.\nSpecial days: Teachers' Day (September 5), International Day of Peace (September 21).",
    "october": "October is a month of transition from autumn to winter. The weather becomes cooler, and people prepare for the upcoming winter season. Halloween is celebrated on October 31.\nSpecial days: Halloween (October 31), World Thrift Day (October 29).",
    "november": "November is a month of transition from autumn to winter. The weather becomes colder, and people prepare for the upcoming winter season. Thanksgiving is celebrated on November 26 in the United States.\nSpecial days: Thanksgiving (November 26), World AIDS Day (November 30).",
    "december": "December is the last month of the year. It is generally cold in many parts of India, especially in the mornings and at night. People celebrate Christmas on December 25 and New Year on December 31.\nSpecial days: Christmas (December 25), New Year's Eve (December 31)."
}
 #******************************Different ways to write the same function*********************************#

# def monthly_challanges(request , month):
#     if month in monthly_challenges:
#         return HttpResponse(monthly_challenges[month])
#     else:
#         return HttpResponseNotFound("Bad request month is not supported.")

#*******************************Different ways to write the same function*********************************#

def monthly_challanges(request,month):
    try:
        challanges_text = monthly_challenges[month]
        return HttpResponse(challanges_text)
    except:
        return HttpResponseNotFound("Bad request month is not supported.")

#************************************************************************************************************

#********************************Loading the html template using render_to_string() method***************************************
def monthly_challanges(request,month):
    try:
        challanges_text = monthly_challenges[month]
        return render(request,"challanges/challange.html",{
            "month_name": month,
            "challanges_text": challanges_text})
        # html_content = render_to_string("challanges/challange.html")
        # return HttpResponse(html_content)
    except:
        return HttpResponseNotFound("<h1>Bad request</h1><p>Month is not supported.</p>")
    
# def march(request):
#     return HttpResponse("March is a transitional month, with the arrival of spring in many parts of India. The weather becomes more comfortable, and people enjoy outdoor activities. Holi, the festival of colors, is celebrated in March.\nSpecial days: Holi, International Women's Day (March 8).")

# def april(request):
#     return HttpResponse("April is a month of new beginnings, with the full bloom of spring. The weather is generally warm and pleasant. People celebrate various festivals, including Baisakhi and Good Friday.\nSpecial days: Baisakhi, Good Friday.")

# def may(request):
#     return HttpResponse("May is a month of transition from spring to summer. The weather becomes hotter, and people often seek ways to stay cool. Many schools and colleges have their summer vacations during this time.\nSpecial days: Labor Day (May 1), Mother's Day.")

# def june(request):
#     return HttpResponse("June is the first month of summer in the Northern Hemisphere. The weather is generally warm, and people enjoy outdoor activities. Children often have their summer vacations during this time.\nSpecial days: World Environment Day (June 5), Father's Day.")

# def july(request):
#     return HttpResponse("July is a month of mid-summer, with hot and humid weather in many regions. People often take vacations to escape the heat. Independence Day is celebrated on July 4 in the United States.\nSpecial days: Independence Day (July 4), World Population Day (July 11).")

# def august(request):
#     return HttpResponse("August is a month of late summer, with warm weather continuing in many areas. People enjoy outdoor activities and vacations. Independence Day is celebrated on August 15 in India.\nSpecial days: Independence Day (August 15), Raksha Bandhan.")  

# def september(request):
#     return HttpResponse("September is a month of transition from summer to autumn. The weather begins to cool down, and people prepare for the upcoming fall season. Teachers' Day is celebrated on September 5 in India.\nSpecial days: Teachers' Day (September 5), International Day of Peace (September 21).")  

# def october(request):
#     return HttpResponse("October is a month of autumn, with cooler temperatures and the changing colors of leaves. People celebrate various festivals, including Diwali and Halloween.\nSpecial days: Diwali, Halloween (October 31).") 

# def november(request):
#     return HttpResponse("November is a month of late autumn, with cooler weather and shorter days. People prepare for the upcoming winter season. Children's Day is celebrated on November 14 in India.\nSpecial days: Children's Day (November 14), Thanksgiving (fourth Thursday of November).")

# def december(request):
#     return HttpResponse("December is a month of winter, with cold weather in many regions. People celebrate various festivals, including Christmas and New Year's Eve.\nSpecial days: Christmas (December 25), New Year's Eve (December 31).")

#   ----------------------------DYNAMIC PATH SEGMENT-----------------------------

# def monthly_challanges(request, month):
#     challanges_text = None
#     if month=="january":
#         challanges_text = "January is the first month of the year. It is generally cold in many parts of India, especially in the mornings and at night. People celebrate New Year on January 1 and Makar Sankranti or Pongal around January 14–15. Special days: New Year's Day, Republic Day (January 26)."

#     elif month == "february":
#         challanges_text = "February often brings pleasant weather, with temperatures beginning to rise in many regions. Flowers bloom, and the days gradually become warmer. Valentine's Day is celebrated on February 14.\nSpecial days: Valentine's Day, National Science Day (February 28)."

#     elif month == "march":
#         challanges_text = "March is a transitional month, with the arrival of spring in many parts of India. The weather becomes more comfortable, and people enjoy outdoor activities. Holi, the festival of colors, is celebrated in March.\nSpecial days: Holi, International Women's Day (March 8)."

#     elif month == "april":
#         challanges_text = "April is a month of spring, with mild weather and blooming flowers. People enjoy outdoor activities and festivals. Dr. Ambedkar's birthday is celebrated on April 14.\nSpecial days: Dr. Ambedkar's Birthday (April 14), World Health Day (April 7)."

#     elif month == "may":
#         challanges_text = "May is a month of warm weather, with the onset of summer in many regions. People celebrate various festivals and events. May Day is celebrated on May 1.\nSpecial days:My Birthday (May 13), May Day (May 1), World Athletics Day (May 20)."

#     elif month == "june":
#         challanges_text = "June is a month of summer, with hot weather in many regions. People celebrate various festivals and events. World Environment Day is celebrated on June 5.\nSpecial days: World Environment Day (June 5), World Ozone Day (June 16)."
#     else:
#         return HttpResponseNotFound("Bad request month is not supported.")
#     return HttpResponse(challanges_text) 


def monthly_challanges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Bad request Invalid month number.")
    redirect_month = months[month-1]
    return HttpResponseRedirect(f"/challanges/{redirect_month}")

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challanges", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

