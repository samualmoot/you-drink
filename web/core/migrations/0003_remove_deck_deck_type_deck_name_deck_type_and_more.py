# Generated by Django 4.2 on 2023-07-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_deck_card_deck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='deck_type',
        ),
        migrations.AddField(
            model_name='deck',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='deck',
            name='type',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='card',
            name='drink_amount',
            field=models.IntegerField(default=1),
        ),
    ]
