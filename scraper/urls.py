from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # Main scraping page
    path('scrape/', views.home, name='scrape'),           # Alternative route
    path('export-excel/', views.export_excel, name='export_excel'),
    
    # Optional: View all saved candidates
    path('candidates/', views.candidate_list, name='candidate_list'),
    
    # Optional: Delete all candidates (use carefully)
    path('clear-data/', views.clear_data, name='clear_data'),
]