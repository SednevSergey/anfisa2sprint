from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(
        default=100, verbose_name='Порядок отображения')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField('Название', max_length=256,
                             help_text='Уникальное название обёртки, не более 256 символов')

    class Meta:
        verbose_name = 'объект «Обёртка»'
        verbose_name_plural = 'Обёртки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория',
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топинг')
    is_on_main = models.BooleanField('На главную', default=False)
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title
