# Generated by Django 3.0.3 on 2020-02-19 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StreetCardServices', '0014_remove_incomeandsources_personalid'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomeandsources',
            name='PersonalId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='IncomeAndSources_PersonalId', to='StreetCardServices.Homeless'),
        ),
    ]