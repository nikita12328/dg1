from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
        This function is the view for the index page. It takes a request object as a parameter and returns an HTTP response with the rendered 'my_app/index.html' template.

        Parameters:
            request (HttpRequest): The request object containing information about the current request.

        Returns:
            HttpResponse: The HTTP response with the rendered 'my_app/index.html' template.
    """
    logger.info("\nIndex Page")
    context = {
        'title': 'Django Course',
    }
    return render(request, 'my_app/index.html', context)


def about(request):
    """
    Render the about page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTTP response.

    Raises:
        None
    """
    logger.info("About Page")
    context = {
        'title': 'Django Course',
    }
    return render(request, 'my_app/about.html', context)


def contact(request):
    """
    Render the contact page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered contact.html page.
    """
    logger.info("Contact Page")
    context = {
        'title': 'Django Course',
    }
    return render(request, 'my_app/contact.html', context)
