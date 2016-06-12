from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpUnauthorized
from transactionapi.models import Transaction
from django.contrib.auth.models import User

class TransactionResource(ModelResource):
    class Meta:
        queryset = Transaction.objects.all()
        resource_name = 'transactions'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True

    # In aid of per-user resources i.e. only retrieve Transactions for the
    # user making the request, code taken from TastyPie cookbook:
    # http://django-tastypie.readthedocs.org/en/latest/cookbook.html#creating-per-user-resources
    def obj_create(self, bundle, **kwargs):
        return super(TransactionResource, self).obj_create(
                bundle, user=bundle.request.user)

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)

    def authorized_create_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)

    def authorized_update_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)

    def authorized_delete_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)

    def authorized_read_detail(self, object_detail, bundle):
        if bundle.obj.user != bundle.request.user:
            raise ImmediateHttpResponse(response=HttpUnauthorized())
        return True

    # Shouldn't need auth when the object hasn't been created yet
    def authorized_create_detail(self, object_detail, bundle):
        pass

    def authorized_update_detail(self, object_detail, bundle):
        if bundle.obj.user != bundle.request.user:
            raise ImmediateHttpResponse(response=HttpUnauthorized())
        return object_detail.filter(user=bundle.request.user)

    def authorized_delete_detail(self, object_detail, bundle):
        if bundle.obj.user != bundle.request.user:
            raise ImmediateHttpResponse(response=HttpUnauthorized())
        return object_detail.filter(user=bundle.request.user)
