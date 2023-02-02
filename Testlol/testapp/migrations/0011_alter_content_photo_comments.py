# Generated by Django 4.1.5 on 2023-01-19 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0010_alter_content_author_alter_content_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='photo',
            field=models.ImageField(upload_to='photos/%d/'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comment', models.TextField(blank=True, help_text='Распишите вашу тему')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.content')),
            ],
        ),
    ]