
from celery import shared_task
from apps.orders.models import Order

def send_order_confirmation_email(order_id):
    """
    Dummy function to simulate sending an order confirmation email.
    Replace with real email logic in production.
    """
    order = Order.objects.get(id=order_id)
    print(f"Order confirmation sent for order {order.id}")

@shared_task
def async_send_order_confirmation(order_id):
    """
    Celery task to send order confirmation asynchronously.
    """
    send_order_confirmation_email(order_id)
