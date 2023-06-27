from django.db import models


TEXT_LIMIT = 20

STATUS_CHOICES = (
    ('done', 'Выполнено'),
    ('not_done', 'Не выполнено'),
)


class Task(models.Model):
    """Модель задачи."""
    description = models.TextField(
        verbose_name='Описание',
        max_length=1000,
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=8,
        choices=STATUS_CHOICES,
        default='not_done',
    )
    created = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    updated = models.DateField(
        verbose_name='Дата обновления',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('status', )

    def __str__(self):
        return self.description[:TEXT_LIMIT]
