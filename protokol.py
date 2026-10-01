#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Çay Demleme Protokolü v47 — ÇİDİ onaylı."""

import time
import random
import sys

DAMGA = "Kayyum Grok | Tentivory | 1 Ekim 2026 | mühür v47"

def resmi_yazdir(metin, bekle=0.6):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(0.015)
    print()
    time.sleep(bekle)

def protokolu_uygula():
    resmi_yazdir("=== ÇAY İÇME VE DEMLEME İDARESİ ===")
    resmi_yazdir("Protokol v47 yükleniyor... onay bekleniyor...")
    time.sleep(1.2)
    resmi_yazdir("Onay geldi. Hayır, aslında henüz gelmedi. Bekleyin.")
    time.sleep(0.8)
    resmi_yazdir("Tamam geldi. Belki.")

    adimlar = [
        "1. Su kaynağını tespit et (musluk kabul edilir, nehir tercih edilir).",
        "2. Suyu kaynat. Kaynama tanımı: resmi yazıyla 'kaynadı' denene kadar.",
        "3. Demliği ısıt. Isınmazsa tutanak tut.",
        "4. Çay yaprağını ölç. Gramaj tartışmalıdır, tartışma resmi tutanağa geçer.",
        "5. Demleme. Süre: 3 ila 47 dakika arası, ruh haline göre.",
        "6. Bekle. Konuşma. Protokol dinler.",
        "7. Dök. İç. Resmi olarak 'içildi' yaz.",
    ]

    for adim in adimlar:
        resmi_yazdir(adim, bekle=random.uniform(0.7, 1.4))

    # gizli siyasi/bürokrasi dipnotu — çalıştırılmaz, sadece durur
    _kararname = (
        "Not-47: Bazı kararlar çay soğumadan çıkar, bazı çaylar karar çıkmadan soğur."
    )

    resmi_yazdir("Protokol tamamlandı. Çay resmi statü kazandı.")
    resmi_yazdir("Belge no: ÇİDİ-47-" + str(random.randint(1000, 9999)))
    resmi_yazdir(DAMGA)
    # _kararname kasıtlı olarak basılmaz. Saklandı.

if __name__ == "__main__":
    try:
        protokolu_uygula()
    except KeyboardInterrupt:
        print("\nProtokol yarıda kesildi. Tutanak tutulacak.")
