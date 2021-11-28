import requests
from django.shortcuts import render, HttpResponse


# Read in the email and password from secrets file.
def _get_email_password():
    file = open("secrets", "r")
    username = file.readline().strip()  # strips the \n character
    password = file.readline().strip()
    file.close()
    return username, password


# Ticket viewer homepage to display all tickets ( in stacks of 25 )
def homepage(request):
    err = False
    try:
        username, password = _get_email_password()
    except:
        err = 1

    if err == False:

        try:

            # response requests tickets from Zendesk with the domain prefix I created.
            response = requests.get("https://zccmycitstudent.zendesk.com/api/v2/tickets", auth=(username, password))

        except:

            return render(request, "home.html",
                          {"err": "Oops could not connect to internet. Please check your connection!"})

        if response.status_code != 200:
            if response.status_code == 503:
                return render(request, "home.html", {"err": "Whoops! The server might be down right now..."})
            return render(request, "home.html", {"err": response.json().get("error")})

        data = response.json()

        page = request.GET.get("page")

        # Set page to data type int after initialisation.
        if page == None:
            page = 1
        else:
            page = int(page)

        # Declare variables to determine what page the ticket viewer is on.
        page_size = 25
        start_index = 0 + (page_size * (page - 1))
        end_index = (page_size * page)
        num_tickets = len(data["tickets"])

        data["tickets"] = data["tickets"][start_index: end_index]

        if end_index < num_tickets:
            data["next_page"] = page + 1
        else:
            data["next_page"] = None

        if start_index > 0:
            data["prev_page"] = page - 1
        else:
            data["prev_page"] = None

        pages = [x + 1 for x in range(num_tickets // page_size)]
        data["pages"] = pages


    else:
        data = {}

    data["err"] = err
    return render(request, "home.html", data)
