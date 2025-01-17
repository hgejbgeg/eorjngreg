import os
import json
from google.cloud import translate_v2 as translate

# Google Translate API'yi başlat (JSON Key dosyasının yolunu doğru şekilde ekle)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\0bora\Desktop\lingify-58867-1b117fdb8f4c.json'
translate_client = translate.Client()

# JSON dosyasını masaüstünden oku
input_file_path = r'C:\Users\0bora\Desktop\oxford3000a1.json'

with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Çeviri fonksiyonu (İngilizceden İspanyolcaya çevirir)
def translate_text(text, target_language='es'):
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

# Her kelimenin 'meaning' ve 'sentence translation' kısmını çevir ve yeni bir JSON oluştur
for item in data:
    for meaning_item in item['meaning list']:
        meaning_item['meaning_spanish'] = translate_text(meaning_item['meaning'])  # 'meaning' çevirisi
        meaning_item['sentence_translation_spanish'] = translate_text(meaning_item['sentence translation'])  # 'sentence translation' çevirisi

# Yeni JSON dosyasını masaüstüne kaydet
output_file_path = r'C:\Users\0bora\Desktop\oxford3000a1_spanish.json'

with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print(f"Çeviri işlemi tamamlandı ve yeni dosya kaydedildi: {output_file_path}")
