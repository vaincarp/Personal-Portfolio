from django.urls import path
from . import views

app_name = 'blog'
# if we use the above name then we need to apply blog: in the all+blogs.html
# <a href="{% url 'blog:detail' blog.id %}"><h2>{{ blog.title }}</h2></a>
# OR
# <a href="{% url 'detail' blog.id %}"><h2>{{ blog.title }}</h2></a> without app_name
# its a good practice

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]
