from rest_framework import permissions

class CzyTechnik(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.rola == 'TECHNICIAN'

class CzyLicencjat(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.rola == 'BACHELOR'

class CzyMagister(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.rola == 'MASTER'
