from django.db import models

CHOICES = (
    ('started', 'запущен'),
    ('blocked', 'заблокирован'),
    ('stopped', 'остановлен')
)

class VPS(models.Model):
    uid = models.UUIDField('UUID', primary_key=True)
    cpu = models.IntegerField('Количество процессорных ядер')
    ram = models.IntegerField('Объем оперативной памяти')
    hdd = models.IntegerField('Объем дискового пространства')
    status = models.CharField(
        'Статус',
        max_length=32,
        choices=CHOICES
        )
    
    def __str__(self):
        return self.uid