from django.shortcuts import render
from .models import book, Author , bookinstance, Genre

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=book.objects.all().count()
    num_instances=bookinstance.objects.all().count()
    #Available books
    num_instances_available= bookinstance.objects.filter(status__exact='a').count()
    num_authors= Author.objects.count()
    return render(
                        request,
                        'index.html',
                        context= {'num_books':num_books, 'num_instances':num_instances,
                                  'num_instances_available': num_instances_available,
                                  'num_authors': num_authors},
                    )