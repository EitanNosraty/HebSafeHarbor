from hebsafeharbor import HebSafeHarbor

hsh = HebSafeHarbor()

text = """שרון לוי התאשפזה ב02.02.2012 וגרה בארלוזרוב 16 רמת גן"""
doc = {"text": text}

output = hsh([doc])

print(output[0].anonymized_text.text)

# > <שם_> התאשפזה ב<יום_>.02.2012 וגרה <מיקום_> 16 רמת גן

text = """איתן נוסרתי עובד בחברת אמן המייל שלי הוא eitanno@taxes.gov.il  תעודת הזהות שלי היא 200630465"""
doc = {"text": text}

output = hsh([doc])

print(output[0].anonymized_text.text)

# > <שם_> התאשפזה ב<יום_>.02.2012 וגרה <מיקום_> 16 רמת גן
