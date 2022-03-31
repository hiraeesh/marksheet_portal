# Generated by Django 3.1.2 on 2021-02-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bhai',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('programme', models.CharField(default='bscit', max_length=40)),
                ('semister', models.IntegerField(default=1, max_length=5)),
                ('coursetitleone', models.CharField(default='a', max_length=40)),
                ('coursetitletwo', models.CharField(default='a', max_length=40)),
                ('coursetitlethree', models.CharField(default='a', max_length=40)),
                ('coursetitlefour', models.CharField(default='a', max_length=40)),
                ('coursetitlefive', models.CharField(default='a', max_length=40)),
                ('coursetitlesix', models.CharField(default='a', max_length=40)),
                ('coursetitleseven', models.CharField(default='a', max_length=40)),
                ('coursetitleeight', models.CharField(default='a', max_length=40)),
                ('coursetitlenine', models.CharField(default='a', max_length=40)),
                ('coursetitleten', models.CharField(default='a', max_length=40)),
                ('coursecredits', models.IntegerField(default=2, max_length=5)),
                ('tr_or_prone', models.CharField(default='a', max_length=40)),
                ('tr_or_prtwo', models.CharField(default='a', max_length=40)),
                ('tr_or_prthree', models.CharField(default='a', max_length=40)),
                ('tr_or_prfour', models.CharField(default='a', max_length=40)),
                ('tr_or_prfive', models.CharField(default='a', max_length=40)),
                ('tr_or_prsix', models.CharField(default='a', max_length=40)),
                ('tr_or_prseven', models.CharField(default='a', max_length=40)),
                ('tr_or_preight', models.CharField(default='a', max_length=40)),
                ('tr_or_prnine', models.CharField(default='a', max_length=40)),
                ('tr_or_prten', models.CharField(default='a', max_length=40)),
                ('iaone', models.CharField(default='a', max_length=40)),
                ('iatwo', models.CharField(default='a', max_length=40)),
                ('iathree', models.CharField(default='a', max_length=40)),
                ('iafour', models.CharField(default='a', max_length=40)),
                ('iafive', models.CharField(default='a', max_length=40)),
                ('iasix', models.CharField(default='a', max_length=40)),
                ('iaseven', models.CharField(default='a', max_length=40)),
                ('iaeight', models.CharField(default='a', max_length=40)),
                ('ianine', models.CharField(default='a', max_length=40)),
                ('iaten', models.CharField(default='a', max_length=40)),
                ('overallone', models.CharField(default='a', max_length=40)),
                ('overalltwo', models.CharField(default='a', max_length=40)),
                ('overallthree', models.CharField(default='a', max_length=40)),
                ('overallfour', models.CharField(default='a', max_length=40)),
                ('overallfive', models.CharField(default='a', max_length=40)),
                ('overallsix', models.CharField(default='a', max_length=40)),
                ('overallseven', models.CharField(default='a', max_length=40)),
                ('overalleight', models.CharField(default='a', max_length=40)),
                ('overallnine', models.CharField(default='a', max_length=40)),
                ('overallten', models.CharField(default='a', max_length=40)),
                ('credits_earnedone', models.IntegerField(default=0, max_length=40)),
                ('credits_earnedtwo', models.IntegerField(default=0, max_length=40)),
                ('credits_earnedthree', models.IntegerField(default=0, max_length=40)),
                ('credits_earnedfour', models.IntegerField(default=0, max_length=40)),
                ('credits_earnedfive', models.IntegerField(default=0, max_length=40)),
                ('credits_earnedsix', models.IntegerField(default=0, max_length=40)),
                ('credits_earnedseven', models.IntegerField(default=0, max_length=40)),
                ('credits_earnedeight', models.IntegerField(default=0, max_length=40)),
                ('credits_earnednine', models.IntegerField(default=0, max_length=40)),
                ('credits_earnedten', models.IntegerField(default=0, max_length=40)),
                ('grade_pointsone', models.IntegerField(default=0, max_length=40)),
                ('grade_pointstwo', models.IntegerField(default=0, max_length=40)),
                ('grade_pointsthree', models.IntegerField(default=0, max_length=40)),
                ('grade_pointsfour', models.IntegerField(default=0, max_length=40)),
                ('grade_pointsfive', models.IntegerField(default=0, max_length=40)),
                ('grade_pointssix', models.IntegerField(default=0, max_length=40)),
                ('grade_pointsseven', models.IntegerField(default=0, max_length=40)),
                ('grade_pointseight', models.IntegerField(default=0, max_length=40)),
                ('grade_pointsnine', models.IntegerField(default=0, max_length=40)),
                ('grade_pointsten', models.IntegerField(default=0, max_length=40)),
                ('csone', models.IntegerField(default=0, max_length=40)),
                ('cstwo', models.IntegerField(default=0, max_length=40)),
                ('csthree', models.IntegerField(default=0, max_length=40)),
                ('csfour', models.IntegerField(default=0, max_length=40)),
                ('csfive', models.IntegerField(default=0, max_length=40)),
                ('cssix', models.IntegerField(default=0, max_length=40)),
                ('csseven', models.IntegerField(default=0, max_length=40)),
                ('cseight', models.IntegerField(default=0, max_length=40)),
                ('csnine', models.IntegerField(default=0, max_length=40)),
                ('csten', models.IntegerField(default=0, max_length=40)),
                ('sgpi', models.IntegerField(default=0, max_length=40)),
                ('remark', models.CharField(default='a', max_length=30)),
            ],
        ),
    ]
