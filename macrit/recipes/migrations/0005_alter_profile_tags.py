# Generated by Django 3.2.3 on 2022-12-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_food_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tags',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
