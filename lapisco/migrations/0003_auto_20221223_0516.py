# Generated by Django 2.2 on 2022-12-23 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lapisco', '0002_auto_20221222_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='laptopdata',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapisco.brand'),
        ),
    ]