from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from smtplib import SMTPException
import logging
from django.conf import settings

logger = logging.getLogger(__name__)



def notify_daard_user(receiver=[], template='', instance='', title=''):

    #msg_html = render_to_string('./email/admin_notice_created.txt', {'instance': instance.pk})
    msg_plain = render_to_string(template, {'instance': instance})

    try:
        send_mail(
            title,
            msg_plain,
            settings.DEFAULT_FROM_EMAIL,
            receiver
        )
    except BadHeaderError:  # If mail's Subject is not properly formatted.
        logger.debug('Invalid header found.')
        print('Invalid header found.')
    except SMTPException as e:  # It will catch other errors related to SMTP.
        logger.debug('There was an error sending an email.' + e)
        print('There was an error sending an email.' + e)
    except:  # It will catch All other possible errors.
        logger.debug("Mail Sending Failed!")
        print("Mail Sending Failed!")
