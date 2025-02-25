from django.shortcuts import render  # Import Django's render function to render templates
from django.core.paginator import Paginator  # Import Django's Paginator class for pagination
from .models import Song  # Import the Song model from the current app


# Create your views here.
def index(request):
    # Fixed version:
    paginator = Paginator(Song.objects.all(), 1)  # Retrieves all Song objects and paginates them, displaying 1 song per page.
    
    page_number = request.GET.get('page')  # Gets the current page number from the request (e.g., ?page=2)
    
    page_obj = paginator.get_page(page_number)  # Fetches the requested page, handling out-of-range cases automatically.

    context = {"page_obj": page_obj}  # Stores the page object in a dictionary to pass to the template.

    return render(request, "index.html", context)  # Renders the "index.html" template with the paginated song data.
