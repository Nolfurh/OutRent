# Generated by Django 3.2.4 on 2023-05-12 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dwelling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('card_description', models.CharField(max_length=500)),
                ('full_description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dwelling_type', models.CharField(choices=[('RM', 'Room'), ('HS', 'House'), ('AP', 'Apartment'), ('GH', 'Guesthouse')], max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dwelling_post_status', models.CharField(choices=[('DF', 'Draft'), ('PT', 'Posted')], default='DF', max_length=2)),
                ('dwelling_ban_status', models.CharField(choices=[('AC', 'Active'), ('BN', 'Banned')], default='AC', max_length=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dwellings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='DwellingRentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_in', models.DateTimeField()),
                ('date_out', models.DateTimeField()),
                ('rent_status', models.CharField(choices=[('A', 'Active'), ('C', 'Completed'), ('B', 'Booked')], default='B', max_length=1)),
                ('dwelling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_status', to='main_app.dwelling')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renters_reviews', to=settings.AUTH_USER_MODEL)),
                ('dwelling_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_review', to='main_app.dwellingrentstatus')),
            ],
            options={
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='ReviewDwelling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dwellings_reviews', to=settings.AUTH_USER_MODEL)),
                ('dwelling_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renter_review', to='main_app.dwellingrentstatus')),
            ],
            options={
                'ordering': ['-posted'],
            },
        ),
        migrations.AddIndex(
            model_name='reviewrenter',
            index=models.Index(fields=['-posted'], name='main_app_re_posted_757fa3_idx'),
        ),
        migrations.AddIndex(
            model_name='reviewdwelling',
            index=models.Index(fields=['-posted'], name='main_app_re_posted_a946fc_idx'),
        ),
        migrations.AddIndex(
            model_name='dwelling',
            index=models.Index(fields=['-posted'], name='main_app_dw_posted_2e8425_idx'),
        ),
    ]
