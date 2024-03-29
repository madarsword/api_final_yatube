# Generated by Django 3.2.16 on 2023-04-09 09:47

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230409_1144'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_name_description',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('following', django.db.models.expressions.F('user')), _negated=True), name='self_follow'),
        ),
    ]
