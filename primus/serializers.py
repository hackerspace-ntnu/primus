from rest_framework import serializers

from primus.models import Contest, Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'player', 'value', 'time')


class ContestSerializer(serializers.ModelSerializer):
    results = ResultSerializer(many=True)

    class Meta:
        model = Contest
        fields = ('id', 'name', 'lowest_best', 'results')
