import crcmod
import qrcode
import os
from django.conf import settings

def Payload(nome, chavepix, valor, cidade, txtId, fileNameQrcode):
    nome = nome
    chavepix = chavepix
    valor = valor.replace(',', '.')
    cidade = cidade
    txtId = txtId

    nome_tam = len(nome)
    chavepix_tam = len(chavepix)
    valor_tam = len(valor)
    cidade_tam = len(cidade)
    txtId_tam = len(txtId)

    merchantAccount_tam = f'0014BR.GOV.BCB.PIX01{chavepix_tam:02}{chavepix}'
    transactionAmount_tam = f'{valor_tam:02}{float(valor):.2f}'

    addDataField_tam = f'05{txtId_tam:02}{txtId}'

    nome_tam = f'{nome_tam:02}'

    cidade_tam = f'{cidade_tam:02}'

    payloadFormat = '000201'
    merchantAccount = f'26{len(merchantAccount_tam):02}{merchantAccount_tam}'
    merchantCategCode = '52040000'
    transactionCurrency = '5303986'
    transactionAmount = f'54{transactionAmount_tam}'
    countryCode = '5802BR'
    merchantName = '59{:02}{}'.format(int(nome_tam), nome)
    merchantCity = '60{:02}{}'.format(int(cidade_tam), cidade)
    addDataField = '62{:02}{}'.format(len(addDataField_tam), addDataField_tam)
    crc16 = '6304'
    
    payload = gerarPayload(payloadFormat, merchantAccount, merchantCategCode, transactionCurrency, transactionAmount, countryCode, merchantName, merchantCity, addDataField, crc16)

    save_path = os.path.join(settings.MEDIA_ROOT, "pagamentos/qrcode_pix", fileNameQrcode)
    imgQrcode = qrcode.make(payload)
    imgQrcode.save(save_path)
    
    return payload
  
def gerarPayload(payloadFormat, merchantAccount, merchantCategCode, transactionCurrency, transactionAmount, countryCode, merchantName, merchantCity, addDataField, crc16):
    payload = f'{payloadFormat}{merchantAccount}{merchantCategCode}{transactionCurrency}{transactionAmount}{countryCode}{merchantName}{merchantCity}{addDataField}{crc16}'

    return gerarCrc16(crc16, payload)
    
def gerarCrc16(crc16Code, payload):
    crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)

    crc16Code = hex(crc16(str(payload).encode('utf-8')))

    crc16Code_formatado = str(crc16Code).replace('0x', '').upper().zfill(4)

    payload_completa = f'{payload}{crc16Code_formatado}'
        
    return payload_completa
