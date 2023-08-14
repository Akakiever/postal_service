import random

from celery import shared_task

from app.models import Order


@shared_task
def change_order_status_delivered(order_id):
    print('test')
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return
    order.status = Order.OrderStatus.DELIVERED.value
    order.save()
    change_order_status_random.apply_async(args=[order_id], countdown=180)


@shared_task
def change_order_status_random(order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return
    new_status = random.choice((
        Order.OrderStatus.RECEIVED.value,
        Order.OrderStatus.REJECTED.value,
    ))
    order.status = new_status
    order.save()

