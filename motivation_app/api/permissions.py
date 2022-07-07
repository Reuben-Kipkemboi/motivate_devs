from rest_framework.permissions import BasePermission



class IsStaffUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_staff)
    
class IsStudentUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_student)