""" Serializers for quran_api.languages """

from rest_framework.serializers import ModelSerializer

from quran_api.languages.models import Language


# Create your serializers here.
class LanguageSerializer(ModelSerializer):
    """Language Serializer"""

    class Meta:
        """Meta data"""

        model = Language
        fields = ["id", "url", "name", "code", "created_at", "updated_at"]
