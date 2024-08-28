# Banka Analiz Projesi
## Giriş
Bu proje seçilmiş bankaların finansal tablolarında ve bilançolarında yer almış bazı kalemlere ve bu bankaların hisse değerlerindeki değişime odaklanmıştır. Projede Akbank, Halkbank, İş Yatırım, QNB Finansbank ve Yapı Kredi'ye ait veriler kullanılmıştır. İlgili veriler farklı kaynaklardan elde edilmiştir. Bilanço verilerine erişmek için İş Yatırım, finansal tablo verilerine erişmek için Halk Yatırım ve ilgili hisse senedi verileri için isyatirimhisse kütüphanesi kullanılmıştır. Proje python kullanılarak yapılmıştır. Matplotlib, Pandas ve verileri ilgili sitelerden çekilebilmesi için BeautifulSoup kütüphanelerinden yararlanılmıştır.

Bankaların bilanço ve finansal tablolarında birçok farklı kalem yer almaktadır. Analizin karmaşıklığını artırmamak amacıyla bankanın ekonomik durumunu önemli şekilde etkileyen kalemler hesaba katılmıştır. Bu yüzden finansal tablodan "Net Kar" ile "Sermaye Yeterlilik Oranı" sütunları dikkate alınmıştır. Bilançolardan ise "Net Faiz Geliri/Gideri","Net Ücret ve Komisyon Gelirleri/Giderleri","Mevduat","Kredilerden Alınan Faizler" ve "Özkaynaklar" dikkate alınmıştır.

## Analiz
Yukarıda bahsedilmiş olan tüm kalemler ve ilgili bankaların bu kalemlere ilişkin analizleri bu kısımda yer alacaktır.Bu kalemlerin neden seçildiği ve bu kalemlerin ne anlam ifade ettiği aşağıda açıklanmıştır.

- Net Kar: Net kâr bankanın belirli bir dönem sonunda elde ettiği toplam gelirden (faiz gelirleri, ücretler, komisyonlar, yatırım gelirleri vb.) tüm giderler (faiz giderleri, operasyonel masraflar, vergi giderleri, zarar karşılıkları vb.) düşüldükten sonra kalan miktarı ifade eder. Net kâr, bankanın faaliyetlerinin kârlılığını ve finansal sağlığını gösteren en önemli göstergelerden biridir.
- Sermaye Yeterlilik Oranı: Sermaye Yeterlilik Oranı  bir bankanın finansal sağlığını ve risklere karşı dayanıklılığını değerlendiren kritik bir finansal göstergedir. Bu oran, bankanın sahip olduğu sermaye miktarının, üstlendiği risklerle karşılaştırılmasını sağlar. Sermaye Yeterlilik oranı, bir bankanın kredi, piyasa ve operasyonel riskler gibi risklere karşı ne kadar güvenli bir sermaye tamponuna sahip olduğunu gösterir.

Bilanço verilerinden çekilmiş bu 2 kalem hem bankanın faaliyetlerinin karlılığı, finansal sağlığı ve risklere karşı dayanaklılığı belirttiği için analize eklenmiştir.

![Bankaların Net Kar ve Sermaye Yeterlilik Oranı](assets\finansal_tablo.png)
