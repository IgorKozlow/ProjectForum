# Generated by Django 4.1.5 on 2023-01-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_alter_content_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(help_text='Введите заголовок Темы', max_length=255, verbose_name='Content'),
        ),
    ]