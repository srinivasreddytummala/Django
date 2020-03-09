from rest_framework import serializers

from api_1.models import Cricket

class CricketSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cricket

		fields = ('name','place')