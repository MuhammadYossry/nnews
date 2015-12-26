from .models import News
from rest_framework import serializers

class NewsSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = News
		fields = ('title', 'url', 'source')