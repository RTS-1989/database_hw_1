# Generated by Django 2.2.10 on 2020-09-26 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('image', models.TextField()),
                ('price', models.TextField()),
                ('release_date', models.TextField()),
                ('lte_exists', models.TextField()),
            ],
        ),
    ]
