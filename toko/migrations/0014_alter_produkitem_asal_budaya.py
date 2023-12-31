# Generated by Django 4.2 on 2023-07-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0013_alter_produkitem_asal_budaya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='asal_budaya',
            field=models.CharField(choices=[('A', 'Aceh'), ('SU', 'Sumatera Utara'), ('SB', 'Sumatera Barat'), ('R', 'Riau'), ('KR', 'Kepulauan Riau'), ('J', 'Jambi'), ('SS', 'Sumatera Selatan'), ('BB', 'Bangka Belitung'), ('BE', 'Bengkulu'), ('L', 'Lampung'), ('BT', 'Banten'), ('JK', 'DKI Jakarta'), ('JB', 'Jawa Barat'), ('JT', 'Jawa Tengah'), ('YO', 'DIY Yogyakarta'), ('JT', 'Jawa Timur'), ('BA', 'Bali'), ('NB', 'Nusa Tenggara Barat (NTB)'), ('NT', 'Nusa Tenggara Timur (NTT)'), ('KB', 'Kalimantan Barat'), ('KT', 'Kalimantan Tengah'), ('KS', 'Kalimantan Selatan'), ('KI', 'Kalimantan Timur'), ('KU', 'Kalimantan Utara'), ('SU', 'Sulawesi Utara'), ('GO', 'Gorontalo'), ('ST', 'Sulawesi Tengah'), ('SA', 'Sulawesi Barat'), ('SS', 'Sulawesi Selatan'), ('SG', 'Sulawesi Tenggara'), ('MA', 'Maluku'), ('MU', 'Maluku Utara'), ('PB', 'Papua Barat'), ('P', 'Papua')], max_length=5),
        ),
    ]
