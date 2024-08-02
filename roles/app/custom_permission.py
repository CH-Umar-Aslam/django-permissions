from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    """
    Custom permission to allow access based on user groups and request methods.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check user group and request method
        if request.user.groups.filter(name='Employee').exists():
            return request.method == 'GET'
        if request.user.groups.filter(name='umar').exists():
            return True
        if request.user.groups.filter(name='Manager').exists():
            return request.method in ['GET', 'PUT']

        if request.user.groups.filter(name='    ').exists():
            return True

        if request.user.groups.filter(name='HR').exists():
            return request.method in ['GET','DELETE']
        if request.user.groups.filter(name='lead').exists():
            return request.method in ['GET','DELETE']

        return False
