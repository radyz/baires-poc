from django.utils.translation import gettext as _

from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from ipware import get_client_ip

from reviews.models import Review, Company


class CompanyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name',)


class ReviewModelSerializer(WritableNestedModelSerializer):

    company = CompanyModelSerializer()

    class Meta:
        model = Review
        fields = (
            'id',
            'rating',
            'title',
            'summary',
            'ip_address',
            'submission_date',
            'company',
        )
        read_only_fields = ('ip_address', 'submission_date',)

    def validate(self, data):
        client_ip, is_routable = get_client_ip(self.context.get('request'))

        if not client_ip:
            raise serializers.ValidationError(_('Client ip not available'))

        data['ip_address'] = client_ip
        return data
