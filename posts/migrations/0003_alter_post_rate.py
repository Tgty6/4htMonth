# Generated by Django 5.1.6 on 2025-02-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
