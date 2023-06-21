from django.urls import path
# Импортируем созданное нами представление
from .views import PostList
from .views import PostDetail

from .views import PostSearchList
from .views import PostCreate
from .views import PostUpdate
from .views import PostDelete
from .views import CategoryList
from .views import subscribe

from django.views.decorators.cache import cache_page

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   path('', PostList.as_view()),
   path('', cache_page(60*10)(PostList.as_view()), name='news_list'),
   path('<int:pk>', PostDetail.as_view()),
   path('search', PostSearchList.as_view(), name='news_search'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update', PostUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete', PostDelete.as_view(), name='news_delete'),
   path('article/create/', PostCreate.as_view(), name='article_create'),
   path('article/<int:pk>/update', PostUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete', PostDelete.as_view(), name='article_delete'),

   path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]