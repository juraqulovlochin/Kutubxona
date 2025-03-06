from django.urls import path
from .views import (
    BookView,
    CreatBookView,
    BookDetail,
    UpdateBookView,
    DeletBookView,
    SearchView
)

urlpatterns=[
    path('qidirish',SearchView.as_view(),name='search'),
    path('book/<int:pk>/Uchirish',DeletBookView.as_view(),name='delet'),
    path('book/<int:pk>/yangilash',UpdateBookView.as_view(),name='update'),
    path('',BookView.as_view(),name='home'),
    path('yangi/kitob',CreatBookView.as_view(),name='cret'),
    path('book/<int:pk>/',BookDetail.as_view(),name='detal')
]