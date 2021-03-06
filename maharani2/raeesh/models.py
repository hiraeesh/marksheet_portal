from django.db import models
# Create your models here.
class Bhai(models.Model):
      name=models.CharField(max_length=50)
      roll=models.IntegerField(primary_key=True ,default=0)
      programme=models.CharField(max_length=40,default="bscit")
      semister=models.IntegerField(max_length=5,default=1)
      coursetitleone=models.CharField(max_length=40,default='PYTHON')
      coursetitletwo=models.CharField(max_length=40,default='EMBEDED SYSTEM')
      coursetitlethree=models.CharField(max_length=40,default='SOFTWARE ENGEENIAR')
      coursetitlefour=models.CharField(max_length=40,default='MATHEMATICS')
      coursetitlefive=models.CharField(max_length=40,default='GRAPHICS')
      coursetitlesix=models.CharField(max_length=40,default="PYTHON PRACTICAL")
      coursetitleseven=models.CharField(max_length=40,default='EMBEDED SYSTEM PRACTICAL')
      coursetitleeight=models.CharField(max_length=40,default='SOFTWARE ENGEENIAR PRACTICAL')
      coursetitlenine=models.CharField(max_length=40,default='MATHEMATICS PRACTICAL')
      coursetitleten=models.CharField(max_length=40,default='GRAPHICS PRACTICAL')

      coursecredits=models.IntegerField(max_length=5,default=2)
      
      tr_or_prone=models.CharField(max_length=40,default='a')
      tr_or_prtwo=models.CharField(max_length=40,default='a')
      tr_or_prthree=models.CharField(max_length=40,default='a')
      tr_or_prfour=models.CharField(max_length=40,default='a')
      tr_or_prfive=models.CharField(max_length=40,default='a')
      tr_or_prsix=models.CharField(max_length=40,default="a")
      tr_or_prseven=models.CharField(max_length=40,default='a')
      tr_or_preight=models.CharField(max_length=40,default='a')
      tr_or_prnine=models.CharField(max_length=40,default='a')
      tr_or_prten=models.CharField(max_length=40,default='a')

      
      iaone=models.CharField(max_length=40,default='a')
      iatwo=models.CharField(max_length=40,default='a')
      iathree=models.CharField(max_length=40,default='a')
      iafour=models.CharField(max_length=40,default='a')
      iafive=models.CharField(max_length=40,default='a')
      iasix=models.CharField(max_length=40,default="a")
      iaseven=models.CharField(max_length=40,default='a')
      iaeight=models.CharField(max_length=40,default='a')
      ianine=models.CharField(max_length=40,default='a')
      iaten=models.CharField(max_length=40,default='a')

      overallone=models.CharField(max_length=40,default='a')
      overalltwo=models.CharField(max_length=40,default='a')
      overallthree=models.CharField(max_length=40,default='a')
      overallfour=models.CharField(max_length=40,default='a')
      overallfive=models.CharField(max_length=40,default='a')
      overallsix=models.CharField(max_length=40,default="a")
      overallseven=models.CharField(max_length=40,default='a')
      overalleight=models.CharField(max_length=40,default='a')
      overallnine=models.CharField(max_length=40,default='a')
      overallten=models.CharField(max_length=40,default='a')

      credits_earnedone=models.IntegerField(max_length=40,default=0)
      credits_earnedtwo=models.IntegerField(max_length=40,default=0)
      credits_earnedthree=models.IntegerField(max_length=40,default=0)
      credits_earnedfour=models.IntegerField(max_length=40,default=0)
      credits_earnedfive=models.IntegerField(max_length=40,default=0)
      credits_earnedsix=models.IntegerField(max_length=40,default=0)
      credits_earnedseven=models.IntegerField(max_length=40,default=0)
      credits_earnedeight=models.IntegerField(max_length=40,default=0)
      credits_earnednine=models.IntegerField(max_length=40,default=0)
      credits_earnedten=models.IntegerField(max_length=40,default=0)

      grade_pointsone=models.IntegerField(max_length=40,default=0)
      grade_pointstwo=models.IntegerField(max_length=40,default=0)
      grade_pointsthree=models.IntegerField(max_length=40,default=0)
      grade_pointsfour=models.IntegerField(max_length=40,default=0)
      grade_pointsfive=models.IntegerField(max_length=40,default=0)
      grade_pointssix=models.IntegerField(max_length=40,default=0)
      grade_pointsseven=models.IntegerField(max_length=40,default=0)
      grade_pointseight=models.IntegerField(max_length=40,default=0)
      grade_pointsnine=models.IntegerField(max_length=40,default=0)
      grade_pointsten=models.IntegerField(max_length=40,default=0)

      csone=models.IntegerField(max_length=40,default=0)
      cstwo=models.IntegerField(max_length=40,default=0)
      csthree=models.IntegerField(max_length=40,default=0)
      csfour=models.IntegerField(max_length=40,default=0)
      csfive=models.IntegerField(max_length=40,default=0)
      cssix=models.IntegerField(max_length=40,default=0)
      csseven=models.IntegerField(max_length=40,default=0)
      cseight=models.IntegerField(max_length=40,default=0)
      csnine=models.IntegerField(max_length=40,default=0)
      csten=models.IntegerField(max_length=40,default=0)

      sgpi=models.IntegerField(max_length=40,default=0)
      remark=models.CharField(max_length=30,default='a')


 



