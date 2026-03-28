from django.db import models
from django.utils import timezone

# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    purchase_date = models.DateField(
        verbose_name="Date d'achat",
        help_text="Date d'acquisition de l'équipement",
        default=timezone.now
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Disponible'),
            ('in_use', 'En utilisation'),
            ('maintenance', 'En maintenance'),
        ],
        default='available'
    )

    class Meta:
        verbose_name = "Équipement"
        verbose_name_plural = "Équipements"
        ordering = ['-purchase_date']  # Trier par date récente d'abord

    def __str__(self):
        return self.name
