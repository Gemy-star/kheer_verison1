from django.urls import path
from . import views

urlpatterns = [
    path('create/contact', views.create_contact, name='create-contact'),
    path('add/needy-case', views.add_needycase, name='add-needycase'),
    path('payment/<int:pk>', views.payment_page, name='payment'),
    path('volunteer', views.volunteer_page, name='volunteer-page'),
    path('heba-kheer', views.heba_kheer, name='heba-kheer'),
    path('add-tamkeen', views.add_tamkeen, name='add-tamkeen'),
    path('volunteer-list', views.volunteer_list, name='volunteer-list'),
    path('all', views.new_show_case, name='show-all-cases'),
    path('technical-support', views.add_technical, name='technical-support'),
    path('technical-list', views.technical_list, name='technical-list'),

]
