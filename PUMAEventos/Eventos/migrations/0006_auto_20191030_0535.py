# Generated by Django 2.2.5 on 2019-10-30 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0005_auto_20191026_2249'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='regevento',
            unique_together={('id_Evento', 'email_Usuario')},
        ),
    ]
