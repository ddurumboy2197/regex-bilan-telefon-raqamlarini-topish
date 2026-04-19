import re

def top TelefonRaqamlar(matn):
    telefonRaqamlari = re.findall(r'\+998 \d{2} \d{3} \d{2} \d{2}', matn)
    return telefonRaqamlari

matn = "Menim telefon raqamim +998 90 123 45 67. Sizning telefon raqamingiz +998 91 234 56 78."
print(top TelefonRaqamlar(matn))
```

Kodni ishlatish uchun, matn o'ziga telefon raqamlarini o'z ichiga olgan string bo'lishi kerak. Kodda `re.findall` funksiyasi matn o'z ichiga telefon raqamlarini topish uchun ishlatiladi. `r'\+998 \d{2} \d{3} \d{2} \d{2}'` - bu telefon raqamlarini topish uchun ishlatiladigan regular expression.
