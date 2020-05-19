import smtplib
from _pydecimal import Context

import app as app
from django.conf import settings
from django.core.mail import send_mail
from django.template import Engine
from django.template.loader import render_to_string


def render_template(template, context):
    engine = Engine.get_default()
    tmpl = engine.get_template(template)
    return tmpl.render(Context(context))


# @app.task
# def send_email_task(subject, from_email, to_email, template, args):
#     server = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
#     server.starttls()
#     server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
#     html = render_to_string(template, args)
#     send_mail(
#         subject=subject,
#         message='',
#         from_email=from_email,
#         recipient_list=[to_email],
#         html_message=html
#     )