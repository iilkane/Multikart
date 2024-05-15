from django.utils.deprecation import MiddlewareMixin
from products.models import BlockedIps


class GetUserIpAddress(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if request.user.is_authenticated:
            if not request.user.ips:
                request.user.ips = []
            if ip not in request.user.ips:
                request.user.ips.append(ip)
                request.user.save()



class BlockUserIpAddress(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        x = BlockedIps.objects.filter(ip_address = ip)
        if x:
            raise PermissionError