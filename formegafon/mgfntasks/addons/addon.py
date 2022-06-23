import cryptocode

from django.core.files.storage import FileSystemStorage
from django.conf import settings


def overpayment(form_data: dict) -> float:
    month = form_data['years'] * 12
    monthly_percent = form_data['interest_rate'] / 12 / 100
    annuity_ratio = (monthly_percent*((1+monthly_percent))**month) / (((1+monthly_percent)**month)-1)
    annuity_payment = annuity_ratio * form_data['loan_summ']
    debt_including_overpayment = annuity_payment * month
    overpayment_summ = debt_including_overpayment - form_data['loan_summ']
    return {
        'annuity_payment': round(annuity_payment, 2),
        'debt_including_overpayment': round(debt_including_overpayment, 2),
        'overpayment_summ': round(overpayment_summ, 2)
    }

def define_word(num: int) -> str:
    if num > 9:
        last_two = int(str(num)[-2:])
        if  9 < last_two < 20:
            return 'товаров'
        else:
            last_one = int(str(num)[-1:])
            if last_one == 1:
                return 'товар'
            elif 1 < last_one < 5:
                return 'товара'
            else:
                return 'товаров'
    else:
        if num == 1:
            return 'товар'
        elif 1 < num < 5:
            return 'товара'
        else:
            return 'товаров'
        
def calculate(size: int) -> int:
    summ = 1
    for num in range(3, size+2, 2):
        summ += num**2 + (num**2 - (num - 1)) + (num**2 - 2 * (num - 1)) + (num**2 - 3 * (num - 1))
    return summ

def encode_decode(form_data: dict) -> str:
    file_text = form_data['target_file'].read().decode('utf-8')
    secret_key = "not such a secret"
    fs = FileSystemStorage()
    
    if form_data['encryptdecrypt'] == 'encrypt':
        encoded_text = cryptocode.encrypt(file_text, secret_key)
        filename = fs.save('text_encrypted.txt', form_data['target_file'])
        with open(f'{settings.MEDIA_ROOT}/{filename}', 'w') as encr_file:
            encr_file.write(encoded_text)
    else:
        decoded_text = cryptocode.decrypt(file_text, secret_key)
        filename = fs.save('text_decrypted.txt.txt', form_data['target_file'])
        with open(f'{settings.MEDIA_ROOT}/{filename}', 'w') as decr_file:
            decr_file.write(decoded_text)
            
    uploaded_file_url = fs.url(filename)
    return uploaded_file_url
    