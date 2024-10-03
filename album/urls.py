from django.urls import path
from . import views
urlpatterns = [
    path('',views.add_album,name='add_album'),
    path('edit_album/<int:id>',views.edit_data,name='edit_data'),
    path('edit_musician/<int:id>',views.edit_musician,name='edit_musician'),
    path('delete_data/<int:id>',views.delete_data,name='delete_data'),
]
