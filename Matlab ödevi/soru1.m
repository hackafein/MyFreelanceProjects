clc; 
clear all;



ineksayisi=input('�neklerin say�s�n� giriniz=')
tavuksayisi=input('Tavuklar�n sayisini giriniz=')
masraf=input('Ayl�k masraflar� giriniz=')


yillik_yumurta=(tavuksayisi*180*12)*97/100;

yillik_sut=ineksayisi*9*300;

toplam_satis=yillik_sut*1.7+yillik_yumurta*0.50;

yillik_masraf=12*masraf;

yillik_net_kazanc=toplam_satis-yillik_masraf;

fprintf('Y�ll�k yumurta say�s� =%d Yumurta \n',yillik_yumurta)
fprintf('Y�ll�k Toplam S�t =%d Litre \n',yillik_sut)
fprintf('Toplam Sat�� =%d TL \n',toplam_satis)
fprintf('Toplam Masraf =%d Tl \n',yillik_masraf)
fprintf('---------------------------------------')
fprintf('Y�ll�k Net Kazan� =%d TL \n',yillik_net_kazanc)
fprintf('---------------------------------------')
if yillik_net_kazanc<0
    fprintf('Masraf toplam sat��dan fazlad�r: Sat�� fiyat�n� art�r!')
end