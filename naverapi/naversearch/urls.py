from django.conf.urls import url

from naversearch import views as naversearch_view

urlpatterns = [
	url(r'^naversearch/', naversearch_view.naverBookSearchApi, name='booksearch'),
    url(r'^search/', naversearch_view.naverBookTemplate,name='booksearchtpl')
]
