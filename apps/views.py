from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import App, Review
from django.db.models import Q


# Home page – simple search box
def home(request):
    return render(request, "apps/home.html")


# AJAX suggestion endpoint (first 3 chars typed)
def suggest_apps(request):
    query = request.GET.get("q", "").strip()
    suggestions = []
    if len(query) >= 3:
        apps = App.objects.filter(name__icontains=query)[:10]
        suggestions = [app.name for app in apps]
    return JsonResponse({"results": suggestions})


# Search results page
def search_results(request):
    query = request.GET.get("q", "").strip()
    results = []
    if query:
        results = App.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )
    return render(request, "apps/search_results.html", {"results": results, "query": query})


# App detail page with reviews
def app_detail(request, app_id):
    print('Entered  app detail')
    app = get_object_or_404(App, id=app_id)
    print('appp')
    reviews = Review.objects.filter(app=app)
    print('***************************')
    print(reviews)
    print('******************')
    # reviews = Review.objects.filter(app=app, approved=True)

    return render(request, "apps/app_detail.html", {"app": app, "reviews": reviews})


# Add a new review (requires login)
@login_required
def add_review(request, app_id):
    app = get_object_or_404(App, id=app_id)
    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if text:
            Review.objects.create(
                app=app,
                user=request.user,
                content=text,
                approved=False,  # supervisor must approve
            )
            return redirect("apps:app_detail", app_id=app.id)
    return render(request, "apps/add_review.html", {"app": app})
