from django.urls import path
from . import views


urlpatterns = [
    path('', views.JournalListView.as_view(), name="journal_list"),   
    path('journal/create', views.JournalCreateView.as_view(), name='journal_create'),
    path('journal/update/<pk>', views.JournalUpdateView.as_view(), name="update_journal"),
    path('journal/delete/<pk>', views.JournalDeleteView.as_view(), name="delete_journal"),
]