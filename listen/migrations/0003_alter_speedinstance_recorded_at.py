# Generated by Django 5.0.6 on 2024-06-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listen', '0002_speedinstance_delete_choice_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedinstance',
            name='recorded_at',
            field=models.CharField(max_length=32),
        ),
    ]
