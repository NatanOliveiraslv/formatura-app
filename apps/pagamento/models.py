from django.db import models
from django.utils import timezone

# Create your models here.

class Pagamentos(models.Model):

    PAYMENT_STATUS = [
        ('PAGO','Pago'),
        ('PENDENTE','Pendente'),
        ]
    
    status = models.CharField('Status', max_length=100, choices=PAYMENT_STATUS, default='')
    nome = models.CharField("nome", max_length=100, blank=False, null=False)
    email = models.EmailField('E-mail', blank=False, null=False)
    value = models.FloatField('Valor', null=False, blank=False, default=0.0)
    message = models.TextField('Mensagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', default=timezone.now)
    # qrcode = models.FileField('qrcode', upload_to="qrcode_pix/", blank=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'