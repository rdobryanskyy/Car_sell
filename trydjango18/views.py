from django.shortcuts import render


# Create your views here.
def about(request):	
	return(render(request, "about.html", {}))

def default(request):	
	return(render(request, "default.html", {}))