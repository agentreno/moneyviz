from django.conf.urls import url, include
from transactionapi.resources import TransactionResource
from . import views

transaction_resource = TransactionResource()

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^', include(transaction_resource.urls)),
]
