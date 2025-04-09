from main.models import *


def categories_processor(request):
    return {'categories': Category.objects.all()}

def genre_processor(request):
    return {'genres': Genre.objects.all()}