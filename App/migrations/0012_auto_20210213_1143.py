# Generated by Django 3.1.1 on 2021-02-13 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20210211_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='item_id',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='App.items'),
            preserve_default=False,
        ),
    ]
