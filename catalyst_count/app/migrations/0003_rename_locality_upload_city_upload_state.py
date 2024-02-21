# Generated by Django 4.1.5 on 2024-02-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_remove_upload_csv_file_upload_country_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="upload",
            old_name="locality",
            new_name="city",
        ),
        migrations.AddField(
            model_name="upload",
            name="state",
            field=models.TextField(blank=True, null=True),
        ),
    ]