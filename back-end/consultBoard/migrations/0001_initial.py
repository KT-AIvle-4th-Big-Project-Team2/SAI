# Generated by Django 4.2 on 2024-01-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BoardConsult",
            fields=[
                ("board_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=75)),
                ("contents", models.TextField()),
                ("creationdate", models.DateTimeField()),
            ],
            options={
                "db_table": "board_consult",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CommentsConsult",
            fields=[
                ("comment_id", models.AutoField(primary_key=True, serialize=False)),
                ("contents", models.TextField()),
                ("creationdate", models.DateTimeField()),
            ],
            options={
                "db_table": "comments_consult",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=75, unique=True)),
                ("password", models.CharField(max_length=75)),
                ("email", models.CharField(max_length=254)),
                ("phonenumber", models.CharField(max_length=11)),
                ("age", models.PositiveIntegerField()),
                ("gender", models.CharField(max_length=1)),
            ],
            options={
                "db_table": "user",
                "managed": False,
            },
        ),
    ]
