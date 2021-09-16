from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import requests
from .models import DiseaseCase
from django.conf import settings
from geonode.geoserver.helpers import ogc_server_settings
import os
import logging
from .send_notification import notify_daard_user
from geonode.people.models import Profile
from .geoserver_wfs_template import wfs_insert_tpl, wfs_update_tpl, wfs_delete_tpl
from .helpers import count_bones, get_bone_names, format_bone_relations, get_technics, get_svgids
logger = logging.getLogger("geonode")

geoserver_local_url = "http://geoserver:8080/geoserver/ows"
geoserver_settings_url = settings.GEOSERVER_WEB_UI_LOCATION
geoserver_user = settings.OGC_SERVER_DEFAULT_USER
geoserver_user_password = settings.OGC_SERVER_DEFAULT_PASSWORD
layername = os.getenv('DAARD_LAYERNAME',"geonode:daard_database_dev")

if ("localhost" in geoserver_settings_url):
    geoserver_url = geoserver_local_url
else:
    geoserver_url = f"{geoserver_settings_url}ows"


def http_client(geoserver_payload):
    try:
        # logger.info(geoserver_payload)
        geoserver_response = requests.post(geoserver_url, data=geoserver_payload.encode('utf-8'), auth=(
            geoserver_user, geoserver_user_password))
        if not geoserver_response.ok:
            logger.error(geoserver_response.content)

        #print(geoserver_payload)
        #print("-------------------------")
        #print(geoserver_response.content)
        #print("-------------------------")

        return geoserver_response.content
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

@receiver(post_save, sender=DiseaseCase)
def add_or_edit_map_feature(sender, instance, created, **kwargs):

    payload_template = wfs_insert_tpl if created else wfs_update_tpl
    instance.layername = layername

    # add calculated fields
    instance.c_no_o_bones = count_bones(instance)
    instance.c_bones = get_bone_names(instance)
    instance.c_b_t_bc_rel = format_bone_relations(instance)
    instance.c_technic = get_technics(instance)
    instance.disease_name = str(instance.disease)
    instance.svgid = get_svgids(instance)
    instance.position = str(instance.position.longitude)+" "+str(instance.position.latitude)
    owner_email = [instance.owner.email, ]

    # Update geoserver
    geoserver_payload = payload_template.format(**instance.__dict__)
    geoserver_response = http_client(geoserver_payload=geoserver_payload)

    # Email notification
    if created:
        daard_all_editor__profiles = Profile.objects.filter(groups__name="daard_editors")
        editor_recipients = list(i for i in daard_all_editor__profiles.values_list('email', flat=True) if bool(i))
        notify_daard_user(receiver=editor_recipients,
                          template='./email/admin_notice_created.txt',
                          instance=instance,
                          title='A new entry has been created')

        notify_daard_user(receiver=owner_email,
                          template='./email/user_notice_created.txt',
                          instance=instance,
                          title='Your DAARD Database entry')
    else:
        if instance.is_approved:
            notify_daard_user(receiver=owner_email,
                              template='./email/user_resource_published.txt',
                              instance=instance,
                              title='Your entry has changed')



@receiver(post_delete, sender=DiseaseCase)
def delete_map_feature(sender,instance,**kwargs):
        # Update Map
        geoserver_payload = wfs_delete_tpl.format(
            layerName=layername,
            uuid=instance.uuid
        )
        geoserver_response = http_client(geoserver_payload=geoserver_payload)

        # Email notification
        receivers = [instance.owner.email, ]
        notify_daard_user(receiver=receivers,
                          template='./email/user_resource_deleted.txt',
                          instance=instance,
                          title='Your entry has been deleted')
