# Generated by Django 4.1.3 on 2022-12-06 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestProxy",
            fields=[
                (
                    "stock_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="stock.stock",
                    ),
                ),
            ],
            bases=("stock.stock",),
        ),
        migrations.AlterField(
            model_name="stock",
            name="category",
            field=models.CharField(
                choices=[
                    ("meet", "肉"),
                    ("vegetable", "野菜"),
                    ("alcohol", "お酒"),
                    ("other", "その他"),
                ],
                max_length=100,
                verbose_name="カテゴリー名",
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
