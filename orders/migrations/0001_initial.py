# Generated by Django 3.1.5 on 2021-03-12 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('delivery_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата доставки')),
                ('address', models.CharField(max_length=256, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('CREATED', 'Создан'), ('DELIVERED', 'Доставлен'), ('PROCESSED', 'В процессе'), ('CANCELLED', 'Отменён')], default='CREATED', max_length=9, verbose_name='Статус публикации')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итого')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='carts.cart', verbose_name='Корзина')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='items.item', verbose_name='Товар')),
            ],
        ),
    ]
