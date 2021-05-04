
from rest_framework import serializers
from .models import *
from django_filters import rest_framework as filters
from slugify import slugify

# All Disease



class NewMedicineSerializer(serializers.ModelSerializer):
    #name = serializers.CharField( read_only=True)
    class Meta:
        model = Bone
        fields = '__all__'


class BoneChangeBoneProxySerializer(serializers.ModelSerializer):
    #disease_library = serializers.CharField(source='disease_library.name', read_only=True)
    technic = serializers.CharField(source='technic.name', read_only=True)
    bone_change = serializers.CharField(source='bone_change.name', read_only=True)
    bone = NewMedicineSerializer( read_only=True, many=True)

    class Meta:
        model = BoneChangeBoneProxy
        fields = ['technic','bone_change','bone',]


class DiseaseSerializer(serializers.ModelSerializer):
    anomalies = BoneChangeBoneProxySerializer(many=True, read_only=True)

    class Meta:
        model = DiseaseLibrary
        fields = ['id','adults','subadults','name','anomalies']
        depth = 3

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DiseaseSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)



# Disease Case

class DiseaseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseCase
        #fields = '__all__'
        filter_fields = ['name',]
        search_fields = ['name', ]
        exclude = ['is_approved', 'geoserver_id',]
        filter_backends = (filters.DjangoFilterBackend)
        title = "XXX"

# All Bones nested with children

class ChildrenBoneSerializer(serializers.ModelSerializer):

    value = serializers.SerializerMethodField()

    class Meta:
        model = Bone
        #exclude = ['lft', 'rght', 'id']
        fields = ['name', 'value',]

    @classmethod
    def get_value(self, object):
        """getter method to add field retrieved_time"""
        return slugify(object.name)

class BoneSerializer(serializers.ModelSerializer):
    options = ChildrenBoneSerializer(many=True)
    label = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    @classmethod
    def get_label(self, object):
        """getter method to add field retrieved_time"""
        return object.name

    @classmethod
    def get_name(self, object):
        """getter method to add field retrieved_time"""
        return slugify(object.name)


    class Meta:
        model = Bone
        #exclude = ['lft','rght',]
        fields = ['name','label','options','section',]



# BONE PROXY
class CustomBoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bone
        fields = ('id','name')

class BoneChangeBoneProxySerializer(serializers.ModelSerializer):
    bone = CustomBoneSerializer(many=True)
    class Meta:
        model = BoneChangeBoneProxy
        depth = 1
        #exclude = ('bone_change__id', )
        fields = '__all__'

