# Generated by Django 4.2.16 on 2024-10-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_medication_drugtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='description',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='dosage',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='start_date',
        ),
        migrations.AddField(
            model_name='prescription',
            name='duration',
            field=models.CharField(choices=[('ก่อนอาหาร', 'ก่อนอาหาร'), ('หลังอาหาร', 'หลังอาหาร')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='medication',
            name='drugtype',
            field=models.CharField(choices=[('tablet', 'ยาเม็ด'), ('liquid', 'ยาน้ำ')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='frequency',
            field=models.CharField(max_length=155),
        ),
    ]
