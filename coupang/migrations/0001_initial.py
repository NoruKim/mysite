# Generated by Django 3.2.7 on 2021-09-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('address_num', models.CharField(max_length=10)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.TextField()),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('product_name', models.TextField()),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('product_desc', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
    ]
