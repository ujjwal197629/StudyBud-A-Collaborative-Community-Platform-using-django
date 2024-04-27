#python object lai json object ma change garna ko lagi
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        #yesle chai k vaniraxa vanda room model lai lera tesko sabai fields lai chai seralize garni json format ma, return all the fields and turn that into json object