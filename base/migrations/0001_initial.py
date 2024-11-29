# Generated by Django 5.1.3 on 2024-11-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your name', max_length=100)),
                ('email', models.EmailField(help_text='Your email address', max_length=254)),
                ('subject', models.CharField(help_text='Subject of your message', max_length=255)),
                ('message', models.TextField(help_text='Your message')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time of submission')),
            ],
        ),
    ]