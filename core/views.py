from django.shortcuts import render, get_object_or_404
from .models import Restaurant, SurpriseBag

def index(request):
    """
    Landing page: Displays the 6 most recent available bags.
    """
    # Fetching active bags from MySQL
    recent_bags = SurpriseBag.objects.filter(is_available=True).order_by('-created_at')[:6]
    return render(request, 'index.html', {'bags': recent_bags})

def browse(request):
    """
    Browse page: Displays all available food bags with optional filtering.
    """
    # Get all available bags
    bags = SurpriseBag.objects.filter(is_available=True)
    
    # Simple search logic for 'Estate' or 'Category'
    query = request.GET.get('q')
    if query:
        bags = bags.filter(restaurant__estate__icontains=query)
        
    return render(request, 'browse.html', {'bags': bags})

def store_detail(request, restaurant_id):
    """
    Store page: Shows a specific restaurant and its current offerings.
    """
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    # Get only the bags belonging to this specific restaurant
    store_bags = SurpriseBag.objects.filter(restaurant=restaurant, is_available=True)
    
    return render(request, 'store.html', {
        'restaurant': restaurant,
        'bags': store_bags
    })

def profile(request):
    """
    Profile page: Shows user info and order history.
    """
    # Placeholder: In a real app, you'd filter by request.user
    return render(request, 'profile.html')