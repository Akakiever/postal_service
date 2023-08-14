from django.db import models


class Order(models.Model):

    class OrderStatus(models.TextChoices):
        NEW = 'new', 'New'
        DELIVERED = 'delivered', 'Delivered'
        RECEIVED = 'received', 'Received',
        REJECTED = 'rejected', 'Rejected'

    foreign_id = models.IntegerField(unique=True)
    location_from = models.CharField(max_length=255)
    location_to = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=OrderStatus.choices, default=OrderStatus.NEW.value)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_changed = models.DateTimeField(auto_now=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        created = False
        if not self.pk:
            created = True
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        if created:
            from app.tasks import change_order_status_delivered
            change_order_status_delivered.apply_async(args=[self.pk], countdown=180)
