# Generated by Django 3.1 on 2020-08-08 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='valid_form',
            new_name='valid_from',
        ),
    ]
