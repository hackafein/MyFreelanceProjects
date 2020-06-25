clc
clear all
subplot(2,1,1)

t= [-15:0.05:15];
y= power(t,2)
plot(t,y,'--b'), xlabel('t'), ylabel('t^2'), title('y=t^2'),
grid on


subplot(2,1,2)
t = [-15:0.05:15];
y = cos(pi*t);
plot(t, y,'.r'), xlabel('t'), ylabel('cos(pi t)'), title('y=cos(pi t)'),
grid on