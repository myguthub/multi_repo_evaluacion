# Generated by Django 4.0.5 on 2022-06-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi', '0008_board_adminpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
