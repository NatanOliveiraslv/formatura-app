from django.db import models

class Presentes(models.Model):
    
    title = models.CharField("Título", max_length=100, blank=False, null=False)
    value = models.FloatField('Valor', null=False, blank=False, default=0.0)
    image = models.FileField('Imagem', upload_to="images/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Presente'
        verbose_name_plural = 'Presentes'
