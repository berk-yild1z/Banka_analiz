# Banka Analiz Projesi
## Giriş
Bu proje seçilmiş bankaların finansal tablolarında ve bilançolarında yer almış bazı kalemlere ve bu bankaların hisse değerlerindeki değişime odaklanmıştır. Projede Akbank, Halkbank, İş Yatırım, QNB Finansbank ve Yapı Kredi'ye ait veriler kullanılmıştır. İlgili veriler farklı kaynaklardan elde edilmiştir. Bilanço verilerine erişmek için İş Yatırım, finansal tablo verilerine erişmek için Halk Yatırım ve ilgili hisse senedi verileri için isyatirimhisse kütüphanesi kullanılmıştır. Proje python kullanılarak yapılmıştır. Matplotlib, Pandas ve verileri ilgili sitelerden çekilebilmesi için BeautifulSoup kütüphanelerinden yararlanılmıştır.

Bankaların bilanço ve finansal tablolarında birçok farklı kalem yer almaktadır. Analizin karmaşıklığını artırmamak amacıyla bankanın ekonomik durumunu önemli şekilde etkileyen kalemler hesaba katılmıştır. Bu yüzden finansal tablodan "Net Kar" ile "Sermaye Yeterlilik Oranı" sütunları dikkate alınmıştır. Bilançolardan ise "Net Faiz Geliri/Gideri","Net Ücret ve Komisyon Gelirleri/Giderleri","Mevduat","Kredilerden Alınan Faizler" ve "Özkaynaklar" dikkate alınmıştır.

## Analiz
Yukarıda bahsedilmiş olan tüm kalemler ve ilgili bankaların bu kalemlere ilişkin analizleri bu kısımda yer alacaktır.Bu kalemlerin neden seçildiği ve bu kalemlerin ne anlam ifade ettiği aşağıda açıklanmıştır.

- Net Kar: Net kâr bankanın belirli bir dönem sonunda elde ettiği toplam gelirden (faiz gelirleri, ücretler, komisyonlar, yatırım gelirleri vb.) tüm giderler (faiz giderleri, operasyonel masraflar, vergi giderleri, zarar karşılıkları vb.) düşüldükten sonra kalan miktarı ifade eder. Net kâr, bankanın faaliyetlerinin kârlılığını ve finansal sağlığını gösteren en önemli göstergelerden biridir.
- Sermaye Yeterlilik Oranı: Sermaye Yeterlilik Oranı  bir bankanın finansal sağlığını ve risklere karşı dayanıklılığını değerlendiren kritik bir finansal göstergedir. Bu oran, bankanın sahip olduğu sermaye miktarının, üstlendiği risklerle karşılaştırılmasını sağlar. Sermaye Yeterlilik oranı, bir bankanın kredi, piyasa ve operasyonel riskler gibi risklere karşı ne kadar güvenli bir sermaye tamponuna sahip olduğunu gösterir.

Bilanço verilerinden çekilmiş bu 2 kalem hem bankanın faaliyetlerinin karlılığı, finansal sağlığı ve risklere karşı dayanaklılığı belirttiği için analize eklenmiştir.

![Bankaların Net Kar ve Sermaye Yeterlilik Oranı](assets/finansal_tablo.png)

Yukarıda verilmiş olan grafikler sol kısımda Net Kar, sağ kısımda ise Sermaye Yeterlilik Oranı yer almaktadır. Veriler 2020 Temmuz ile 2024 Temmuz arasındaki aralığa aittir. Akbank verisine bakıldığında 2022 yıllarına kadar net kar değerlerinde stabil bir artış görülmektedir. Ondan sonraki süreçlerde ise grafik stabil değildir. 2023 yılında sert bir düşüş yaşansa da sonraki dönemlerde artışa geçmiştir ancak 2023'ün son aylarıyla beraber Akbank'ın Net Kar'ı düşüşe geçmiştir.Sermaye yeterlilik oranı grafiğine bakıldığında ise daha dalgalı bir grafik olduğu gözlemlenmektedir.2022 Temmuz ayına kadar dalgalı bir görünüme sahip olan grafik, bu tarihten sonra yükselişe geçmiştir. Ancak 2024 yılı başından itibaren Sermaye Yeterlilik Oranı istikrarlı olarak düşmektedir. İki grafiği karşılaştırdığımızda, 2023 yılı sonundan itibaren hem Net Kar hem de Sermaye Yeterlilik Oranı'nda düşüşler görünmektedir. Bu durum da Akbank'ı riskler karşısında daha zayıf hale getirmiş ve Akbank bu dönemlerde yapmış olduğu faaliyetlerden daha az kar etmiştir.

Halkbank grafiğine bakıldığında ise 2023 yılının başına kadar Net Kar artışa geçmiştir ancak Akbank'da olduğu gibi bu dönemden sonra düşüşe geçmiştir. Akbank'tan farklı olarak Halkbank düşüşten sonra hızlı bir toparlanma sürecine girmiş olup bu süreç 2024 yılının ortalarına kadar devam etmiştir.Sermaye Yeterlilik Oranına bakıldığında ise 2022 yılında zirve noktasına ulaşan bu oran zamanla ciddi oranda azalarak %13 seviyelerine yaklaşmıştır.
İş Yatırım için 2 farklı kalem kullanılmıştır. Bunlar Net İşletme Sermayesi ve Özkaynaklardır. Net İşletme Sermayesi bir bankanın kısa vadeli varlıkları ile kısa vadeli borçları arasındaki farkı ifade eder. Bankalar için net işletme sermayesi, günlük faaliyetlerini sürdürmek için gereken likiditeyi ve finansal esnekliği sağlar. Bankanın kısa vadeli yükümlülüklerini karşılayabilmesi ve operasyonlarını sorunsuz bir şekilde devam ettirebilmesi için yeterli işletme sermayesine sahip olması kritik öneme sahiptir. Net işletme Sermayesi grafiğine bakıldığında 2023 yılına kadar dalgalı bir şekilde değişim göstermiştir.2023 yılında ise ciddi bir düşüş yaşanmıştır. 2023 yılından sonra ise Net İşletme Sermayesi'nde anlamlı bir değişiklik gözlenmemiştir. 

Özkaynaklar, bir banka için temel finansal göstergelerden biridir ve bankanın mali sağlığını, dayanıklılığını ve kârlılığını değerlendirmede kritik bir rol oynar. Özkaynaklar, bankanın sahiplerinin şirkete yatırdığı sermaye ve bankanın faaliyetlerinden elde ettiği kârların birikimi ile oluşur. Bu sermaye, bankanın borçlanma kapasitesini artırırken, finansal krizler ve beklenmedik kayıplar karşısında bir tampon görevi görür. İş Yatırım'ın Özkaynaklar grafiği incelendiğinde 2022 yılının Ağustos ayına kadar ciddi bir değişim yaşanmamıştır ancak bu tarihten 2022 yılının sonlarına kadar ciddi bir oranda yükselmiştir. Diğer bankalarda gördüğümüz gibi 2023 yılının başında ciddi bir düşüş yaşansa da ileriki dönemlerde İş Yatırım Özkaynaklar açısından toparlamıştır.

QNB Finansbak grafikleri incelendiğinde Net Kar açısından istikrarlı bir grafik gözlenmektedir. Diğer bankalarda gözüken sert düşüşler veya yükselişler yaşanmamıştır. Zaman içinde istisnalar olsa da yükselen Net Kar 2024 yılında düşüşe geçmiştir. Sermaye Yeterlilik Oranı ise Net Kar grafiği ile karşılaştırıldığında oldukça farklı bir grafiktir. Düzenli olarak düşüşte olan bu oran 2023'ün ilk aylarında en düşük seviyesini görmüştür. Daha sonraki dönemlerde net bir yükselişe sahip olsa da 2023'ün son aylarından itibaren tekrar düşüşe geçmiştir.

Yapı Kredi Net Kar olarak zaman içinde hep yükselişte olmuştur. Ancak 2023'ün sonlarından itibaren ciddi bir düşüşe geçmiştir.Sermaye Yeterlilik Oranı ise zaman içinde dalgalı bir şekilde değişmiştir. 2023'ün son aylarında keskin bir düşüş yaşayarak 2024 Haziran'da en düşük seviyesi olan %15' ulaşmıştır.

![Akbank Bilanço](assets/akbank_bilanço.png)




