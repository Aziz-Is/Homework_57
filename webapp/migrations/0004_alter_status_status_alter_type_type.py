# Generated by Django 4.0.6 on 2022-07-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_status_type_tracker_status_tracker_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('new', 'новый'), ('in progress', 'в процессе'), ('done', 'выполнено')], default='new', max_length=20),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(choices=[('task', 'задача'), ('bug', 'ошибка'), ('enhancement', 'улучшение')], default='task', max_length=20),
        ),
    ]
