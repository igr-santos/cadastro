# Generated by Django 4.2.1 on 2023-11-28 14:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0024_remove_volunteerstatushistory_volunteer_status_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="volunteer",
            old_name="ocuppation",
            new_name="occupation",
        ),
    ]
