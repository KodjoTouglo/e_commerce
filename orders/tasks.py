from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Commande n° {order.id}'
    message = f'Cher {order.first_name},\n\n' \
              f'Vous avez commandé avec succès.' \
              f'Votre commande d\'identification est {order.id}.' 
    mail_sent = send_mail(subject, message, 'admin@e_commerce.com', [order.email])
    return mail_sent