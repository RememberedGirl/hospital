from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.http import Http404


class MyPermissionMixin(PermissionRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('error_access')
        return super().dispatch(request, *args, **kwargs)


class DoctorPermissionMixin(PermissionRequiredMixin):
    def has_permission(self):
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise redirect('error_access')
        return super().dispatch(request, *args, **kwargs)
