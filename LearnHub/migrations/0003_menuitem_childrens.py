# Generated by Django 5.1.3 on 2024-11-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnHub', '0002_menuitem_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='childrens',
            field=models.ManyToManyField(blank=True, null=True, related_name='children', to='LearnHub.menuitem'),
        ),
    ]
