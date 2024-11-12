from django.urls import path
from django.contrib.auth import views as auth_views
from api.views import index, mail, ticket, login_view, parcels, archive
from api.views import list
from api.views import couriers


urlpatterns = [
        path('', index, name='index'),
        path('stuff_list', list, name="list"),
        path('couriers', couriers, name="couriers"),
        path('mails', mail, name="couriers"),
        path('create_ticket', ticket, name="create_question"),
        path('login/', login_view, name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('parcels/', parcels, name="parcels"),
        path('archive/', archive, name="archive")

]
