from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.utils import timezone
from django.db.models import Q

# Create your views here.

def in_theaters(request):
	queryset = Movie.objects.filter(release_date__lte=timezone.now())
	query = request.GET.get("q")
	if query:
		queryset = Movie.objects.all()
		queryset = queryset.filter(
				Q(name__icontains=query)|
				Q(tagline__icontains=query)
				).distinct()
	context = {
		"object_list" : queryset,
	}
	return render(request, "movies_list.html", context)

def coming_soon(request):
	queryset = Movie.objects.filter(release_date__gt=timezone.now())
	query = request.GET.get("q")
	if query:
		queryset = Movie.objects.all()
		queryset = queryset.filter(
				Q(name__icontains=query)|
				Q(tagline__icontains=query)
				).distinct()
	context = {
		"object_list" : queryset,
	}
	return render(request, "movies_list.html", context)

def movies_genre(request, genre=None):
	queryset = Movie.objects.filter(genre=genre)
	query = request.GET.get("q")
	if query:
		queryset = Movie.objects.all()
		queryset = queryset.filter(
				Q(name__icontains=query)|
				Q(tagline__icontains=query)
				).distinct()
	context = {
	"object_list" : queryset,
	}
	return render(request, "movies_list.html", context)

def movies_list(request):
	queryset = Movie.objects.all()
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
				Q(name__icontains=query)|
				Q(tagline__icontains=query)
				).distinct()
	context = {
		"object_list" : queryset,
	}
	return render(request, "movies_list.html", context)


def movies_detail(request, slug=None):
	instance = get_object_or_404(Movie, slug=slug)
	query = request.GET.get("q")
	if query:
		queryset = Movie.objects.all()
		queryset = queryset.filter(
				Q(name__icontains=query)|
				Q(tagline__icontains=query)
				).distinct()
		context = {
		"object_list" : queryset,
		}
		return render(request, "movies_list.html", context)
	context = {
	"instance" : instance,
	}
	return render(request, "movies_detail.html", context)