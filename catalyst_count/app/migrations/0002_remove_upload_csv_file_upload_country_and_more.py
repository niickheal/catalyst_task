# Generated by Django 4.1.5 on 2024-02-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="upload",
            name="csv_file",
        ),
        migrations.AddField(
            model_name="upload",
            name="country",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="current_employee_estimate",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="domain",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="industry",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="linkedin_url",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="locality",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="name",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="size_range",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="total_employee_estimate",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="year_founded",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
