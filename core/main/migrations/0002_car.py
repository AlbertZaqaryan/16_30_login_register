# Generated by Django 4.1 on 2022-08-10 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Car name')),
                ('about', models.TextField(verbose_name='Car about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Car image')),
                ('price', models.IntegerField(verbose_name='Car price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carcateg', to='main.category')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
