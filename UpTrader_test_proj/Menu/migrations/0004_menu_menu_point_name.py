# Generated by Django 4.1.7 on 2023-03-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_alter_menu_point_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='menu_point',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]