from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from .choices import forms
from geoposition.fields import GeopositionField
import uuid
from jsonfield import JSONField


class DiseaseLibrary(models.Model):
    name = models.CharField(max_length=255)
    subadults = models.BooleanField(default=False, blank=True)
    adults = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class Technic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BoneChange(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Bone(MPTTModel):
    sections = (('cranial_district', 'Cranial district'),
                ('axial_skeleton', 'Axial skeleton'),
                ('right_upper_limb', 'Right upper limb'),
                ('left_upper_limb', 'Left upper limb'),
                ('right_lower_limb', 'Right lower limb'),
                ('left_lower_limb', 'Left lower limb'))
    section = models.CharField(max_length=255, choices=sections)
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='options', db_index=True,
                            on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class BoneChangeBoneProxy(models.Model):
    anomalies = models.ForeignKey('DiseaseLibrary', on_delete=models.CASCADE, related_name='anomalies')
    technic = models.ForeignKey('Technic', on_delete=models.CASCADE, related_name='technic_proxy')
    bone_change = models.ForeignKey('BoneChange', blank=True, null=True, on_delete=models.CASCADE, related_name='bone_change_proxy')
    bone = TreeManyToManyField('Bone', related_name='bone_proxy')


class BoneRelation(models.Model):
    anomalies_case = models.ForeignKey('DiseaseCase', on_delete=models.CASCADE, related_name='anomalies_case')
    technic_case = models.ForeignKey('Technic', on_delete=models.CASCADE, related_name='technic_proxy_case')
    bone_change_case = models.ForeignKey('BoneChange', blank=True, null=True, on_delete=models.CASCADE, related_name='bone_change_proxy_case')
    bone_case = TreeManyToManyField('Bone', related_name='bone_proxy_case')


class DiseaseCase(models.Model):
    # commons
    is_approved = models.BooleanField(default=False)
    geoserver_id = models.UUIDField(primary_key=False, default=uuid.uuid4, blank=True)

    # step 1
    adults = models.BooleanField(default=False)
    subadults = models.BooleanField(default=False)
    disease = models.ForeignKey('DiseaseLibrary', on_delete=models.CASCADE, related_name='anomalies_case')
    age_class = models.CharField(max_length=200, choices=forms['disease']['age_class']['values'])
    age = models.CharField(max_length=200, choices=forms['disease']['age']['values'])
    age_freetext = models.CharField(max_length=200, blank=True)
    sex = models.CharField(max_length=200, choices=forms['disease']['sex']['values'])

    # step 2
    inventory = JSONField()

    # step 3
    bone_relations = JSONField()

    # step 4
    reference_images = models.CharField(max_length=600)
    origin = models.CharField(max_length=400)
    archaeological_site = models.CharField(max_length=400)
    archaeological_tombid = models.CharField(max_length=400)
    archaeological_individualid = models.CharField(max_length=400)
    archaeological_funery_context = models.CharField(max_length=400, choices=forms['site']['archaeological_funery_context']['values'])
    archaeological_burial_type = models.CharField(max_length=400, choices=forms['site']['archaeological_burial_type']['values'])
    storage_place = models.CharField(max_length=400, choices=forms['site']['storage_place']['values'])
    storage_place_freetext = models.CharField(max_length=400)
    storage_condition = models.CharField(max_length=400, choices=forms['site']['storage_condition']['values'])
    chronology = models.CharField(max_length=400)
    chronology_freetext = models.CharField(max_length=400, blank=True)

    # step 5
    dating_method = models.CharField(max_length=400, choices=forms['publication']['dating_method']['values'])
    dna_analyses = models.CharField(max_length=400, choices=forms['publication']['dna_analyses']['values'])
    dna_analyses_link = models.CharField(max_length=400)

    published = models.BooleanField(default=False)
    publication = models.CharField(max_length=400, choices=forms['publication']['publication']['objects']['publication']['values'])

    # contact
    contact_firstname = models.CharField(max_length=400)
    contact_lastname = models.CharField(max_length=400)
    contact_institut = models.CharField(max_length=400)
    contact_email = models.EmailField(max_length=400)
    position = GeopositionField(null=True, blank=True)

    def __str__(self):
        return self.disease