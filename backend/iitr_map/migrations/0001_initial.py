# Generated by Django 4.1.3 on 2022-11-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vertex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('is_prominent', models.BooleanField()),
                ('neighbors', models.ManyToManyField(blank=True, to='iitr_map.vertex')),
            ],
        ),
    ]