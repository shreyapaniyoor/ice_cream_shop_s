# Generated by Django 4.2.15 on 2024-08-22 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0008_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='enquiries', to=settings.AUTH_USER_MODEL),
        ),
    ]
