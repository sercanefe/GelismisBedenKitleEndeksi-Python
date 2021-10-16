print("""
Beden Kitle Endeksi Hesaplayıcı
      """)

boy = float(input("Boyunuzu giriniz (örn: 1.86): "))
kilo = float(input("Kilonuzu giriniz (örn: 75): "))

bki = kilo / (boy**2)

print("Beden kitle endeksiniz {}.".format(bki))

if (bki < 18.5):
    print("Zayıfsınız.")
    print("Biraz bi' şeyler atıştırmaya ne dersiniz?")
elif (bki >= 18.5 and bki < 25):
    print("Normalsiniz")
    print("Formunuzu korumaya çalışın:)")
elif (bki >= 25 and bki < 30):
    print("Fazla kilolusunuz")
    print("Yarım saat koşu yapabilirsiniz:)")
else:
    print("Obezsiniz.")
    print("Diyetisyene gitmeyi düşünebilirsiniz:)")
