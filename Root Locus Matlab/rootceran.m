function [asimtot,acilar,centr,breakingpoint] = rootceran(fonksiyon,K)


kapalidongu=feedback(fonksiyon,K);

kutup=pole(fonksiyon);
sifir=pole(fonksiyon^(-1));
m=length(kutup);
n=length(sifir);
asimtot=m-n;
acilar=zeros(m-n-1,0);
for i = 1:m-n-1
    acilar(i)=(2*i+1/(asimtot))*180;
    
end


centr=(sum(kutup)+sum(sifir))/(m-n);


syms s
kapalifonksiyon=(1+(K*fonksiyon));
n=kapalifonksiyon.numerator{:};
d=kapalifonksiyon.denominator{:};

nuzunluk=length(n);
ns=0;
for i=1:nuzunluk
    ns=ns+n(i)*s^(nuzunluk-i);
end
ds=0;
for i=1:nuzunluk
    ds=ds+d(i)*s^(nuzunluk-i);
end

kapalifonksiyon=ns/ds;
kapalidonguturev=diff((kapalifonksiyon));
[pay,payda]=numden(kapalidonguturev);
pay=coeffs(pay,s,'all');
payda=coeffs(payda,s,'all');
pay=double(pay);
payda=double(payda);

kapalidonguturev=tf(pay,payda);
breakingpoint=zero(kapalidonguturev);


rlocus(fonksiyon)




end

