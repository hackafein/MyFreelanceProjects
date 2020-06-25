clc; 
clear all;



ineksayisi=input('Ýneklerin sayýsýný giriniz=')
tavuksayisi=input('Tavuklarýn sayisini giriniz=')
masraf=input('Aylýk masraflarý giriniz=')


yillik_yumurta=(tavuksayisi*180*12)*97/100;

yillik_sut=ineksayisi*9*300;

toplam_satis=yillik_sut*1.7+yillik_yumurta*0.50;

yillik_masraf=12*masraf;

yillik_net_kazanc=toplam_satis-yillik_masraf;

fprintf('Yýllýk yumurta sayýsý =%d Yumurta \n',yillik_yumurta)
fprintf('Yýllýk Toplam Süt =%d Litre \n',yillik_sut)
fprintf('Toplam Satýþ =%d TL \n',toplam_satis)
fprintf('Toplam Masraf =%d Tl \n',yillik_masraf)
fprintf('---------------------------------------')
fprintf('Yýllýk Net Kazanç =%d TL \n',yillik_net_kazanc)
fprintf('---------------------------------------')
if yillik_net_kazanc<0
    fprintf('Masraf toplam satýþdan fazladýr: Satýþ fiyatýný artýr!')
end