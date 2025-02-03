# Generated by Django 5.1.5 on 2025-02-01 14:07

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category', verbose_name='زیردسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['-status'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('thumbnail', models.ImageField(upload_to='menu', verbose_name='تصویر')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000)], verbose_name='قیمت')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.category', verbose_name='دسته بن دیها')),
            ],
            options={
                'verbose_name': 'آیتم غذا',
                'verbose_name_plural': 'آیتم های غذا',
                'ordering': ['-status'],
            },
        ),
    ]
