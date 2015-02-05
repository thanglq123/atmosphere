from core.models.identity import Identity
from rest_framework import serializers


class IdentityRelatedField(serializers.RelatedField):

    def to_native(self, identity):
        return self.to_representation(identity)

    def to_representation(self, identity):
        quota_dict = identity.get_quota_dict()
        return {
            "id": identity.uuid,
            "provider": identity.provider.location,
            "provider_id": identity.provider.uuid,
            "quota": quota_dict,
        }

    def to_internal_value(self, data, files, field_name, into):
        value = data.get(field_name)
        if value is None:
            return
        try:
            into[field_name] = Identity.objects.get(uuid=value)
        except Identity.DoesNotExist:
            into[field_name] = None
