from isyatirimhisse import StockData, Financials
stock_data = StockData()

df = stock_data.get_data(
    symbols='THYAO',
    start_date='02-01-2023'
)
print(df)
# Örnek 2: Birden fazla hisse senedine ait başlangıç tarihi belli ve son işlem gününe kadar olan haftalık ortalama kapanış fiyatlarını TL bazında al.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['AKBNK','HALKB',"ISYAT","QNBFB","YKBNK"],
    start_date = '02-01-2023',
    exchange='0',
    frequency='1w',
    observation='mean'
)
print(df)

# Haftalık frekansta veriler Pazar günleri başlangıç kabul edilerek ayarlanmaktadır.
# Örnek 3: Birden fazla hisse senedine ait başlangıç ve bitiş tarihleri belli aylık USD fiyatları üzerinden logaritmik getirileri al.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date='01-01-2023',
    end_date='29-09-2023',
    exchange='1',
    frequency='1mo',
    return_type='1'
)
print(df)
stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date='01-01-2023',
    end_date='29-09-2023',
    exchange='1',
    frequency='3mo',
    return_type='2'
)
print(df)
# Örnek 5: Birden fazla hisse senedine ait başlangıç ve bitiş tarihleri belli yıllık ortalama USD fiyatlarını al. Sonucu excel dosyasına kaydet.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','EUPWR'],
    start_date='01-01-2012',
    end_date='06-10-2023',
    exchange='1',
    frequency='1y',
    return_type='1',
    save_to_excel=True
)
print(df)

# Not: Örnekte bulunan EUPWR hisse senedinin 2023 yılı öncesi verileri olmadığı için çıktıda görünmeyecektir.
# Örnek 1: Tek bir hisse senedi için finansal tabloları istenilen başlangıç yılından itibaren çek.

financials = Financials()

df = financials.get_data(
    symbols='THYAO',
    start_year='2020'
)
print(df)
# Örnek 2: Birden fazla hisse senedi için finansal tabloları istenilen başlangıç ve bitiş yılı aralığında çek.
# Sözlük tipinde saklanan verilerden istenen şirket aşağıdaki gibi çekilebilir.

financials = Financials()

df = financials.get_data(
    symbols=['THYAO','PGSUS'],
    start_year='2019',
    end_year='2023',
    exchange='TRY',
    financial_group='1',
    save_to_excel=True
)

import pandas as pd

df_thyao = pd.DataFrame(df['THYAO'])
# Örnek 3: Birden fazla hisse senedi için finansal tabloları istenilen başlangıç ve bitiş yılı aralığında çek.

financials = Financials()

df = financials.get_data(
    symbols=['THYAO','AKBNK'],
    start_year='2019',
    end_year='2023',
    exchange='TRY',
    financial_group='1',
    save_to_excel=True
)


# Not: Örnekte bulunan AKBNK hisse senedi Seri XI NO:29'a uymadığı için (UFRS kullanılmalı) çıktıda görünmeyecektir.
