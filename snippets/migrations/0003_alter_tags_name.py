# Generated by Django 3.2.4 on 2021-06-30 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_alter_snippet_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
