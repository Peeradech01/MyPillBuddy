# Generated by Django 4.2.16 on 2024-10-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_medicationreminder_reminder_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='drugtype',
            field=models.CharField(choices=[('ยาเม็ด', 'ยาเม็ด'), ('ยาน้ำ', 'ยาน้ำ')], default=None, max_length=100),
        ),
    ]
