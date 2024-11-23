from django.db import models

class Convidados(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', blank=False, null=True)
    phone = models.CharField('Telefone', max_length=15, blank=False, null=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'
        ordering =['first_name']