from django.urls import path

from . import views

urlpatterns = [path("", views.contacts_list, name="contacts_list"),
               path("create/", views.contact_create, name="contact_create"),
               path("<int:contact_id>/", views.contact_details, name="contact_details"),
               path('<int:contact_id>/update/', views.contact_update, name='contact_update'),
               path('<int:contact_id>/delete/', views.contact_delete, name='contact_delete')
              ]