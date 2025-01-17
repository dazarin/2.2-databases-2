# Generated by Django 5.1 on 2024-10-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main', 'tag__name']},
        ),
        migrations.AddConstraint(
            model_name='scope',
            constraint=models.UniqueConstraint(condition=models.Q(('is_main', True)), fields=('article', 'is_main'), name='only_one_main_tag'),
        ),
    ]
