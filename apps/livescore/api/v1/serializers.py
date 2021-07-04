from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin
from apps.livescore.models import (
    Result,
)


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = (
            'id',
            'tour',
            'match_date',
            'match_time',
            'place',
            'home_team_title',
            'away_team_title',
            'home_team_id',
            'away_team_id',
            'home_team_score_ft',
            'away_team_score_ft',
        )

    def validate(self, data):
        return data