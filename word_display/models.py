from django.db import models

class word(models.Model):
    wordEntry = models.CharField(max_length=50)
    wordImage = models.CharField(max_length=1000)
    wordDef = models.CharField(max_length = 1000)

    def __str__(self):
        return self.wordEntry + ' : ' + self.wordDef

class users_def(models.Model):
    wordEntry = models.ForeignKey(word, on_delete=models.CASCADE)
    userDef = models.CharField(max_length=150)
