# Generated by Django 4.2.16 on 2024-10-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='drugtype',
            field=models.CharField(choices=[('tablet', 'ยาเม็ด'), ('liquid', 'ยาน้ำ'), ('topical', 'ยาทา'), ('inhaler', 'ยาพ่น')], default=None, max_length=100),
        ),
    ]
