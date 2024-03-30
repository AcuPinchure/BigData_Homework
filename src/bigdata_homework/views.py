from django.shortcuts import render


def notFound(request):
    return render(request, 'post_management/not_found.html', status=404)