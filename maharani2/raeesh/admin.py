from django.contrib import admin
from .models import Bhai

# Register your models here.
@admin.register(Bhai)
class Student(admin.ModelAdmin):
      list_display=['name','roll','programme','semister',

      'coursetitleone',
      'coursetitletwo',
      'coursetitlethree',
      'coursetitlefour',
      'coursetitlefive'
      ,'coursetitlesix',
      'coursetitleseven','coursetitleeight',
      'coursetitlenine',
      'coursetitleten',
      'coursecredits',

      'tr_or_prone',      
      'tr_or_prtwo',
      'tr_or_prthree',
      'tr_or_prfour',
      'tr_or_prfive',
      'tr_or_prsix',
      'tr_or_prseven',
      'tr_or_preight',
      'tr_or_prnine',
      'tr_or_prten',


      'iaone',
      'iatwo',
      'iathree',
      'iafour',
      'iafive',
      'iasix',
      'iaseven',
      'iaeight',
      'ianine',
      'iaten',
      
      'overallone',
      'overalltwo',
      'overallthree',
      'overallfour',
      'overallfive',
      'overallsix',
      'overallseven',
      'overalleight',
      'overallnine',
      'overallten',

      'credits_earnedone',
            'credits_earnedtwo',
      'credits_earnedthree',
      'credits_earnedfour',
      'credits_earnedfive',
      'credits_earnedsix',
      'credits_earnedseven',
      'credits_earnedeight',
      'credits_earnednine',
      'credits_earnedten',

      'grade_pointsone',
      'grade_pointstwo',
      'grade_pointsthree',
      'grade_pointsfour',
      'grade_pointsfive',
      'grade_pointssix',
      'grade_pointsseven',
      'grade_pointseight',
      'grade_pointsnine',
      'grade_pointsten',

      'csone',
      'cstwo',
      'csthree',
      'csfour',
      'csfive',
      'cssix',
      'csseven',
      'cseight',
      'csnine',
      'csten',
      'sgpi',
      'remark'


      ]