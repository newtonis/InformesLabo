 hold off
s=tf('s');
 h=(s*7.05*10^-6)/((s*7.05*10^-6)+1)
 wrange=logspace(3,7,10000);
 %bode(h
[mag, pha , w] = bode(h,wrange);
mag = squeeze(mag);
% xlabel('frec (1/s)');
% ylabel('|H(s)| (db)');
 %hold on
 
 Vr=[0.025 0.025 0.04 0.033 0.034 0.038 0.04 0.045 0.0613 0.038 0.125 0.175 0.22 0.248 0.325 0.4 0.481 0.625 0.769 0.869 0.988 1.075 1.131 1.15 1.188 1.213 1.263 1.275 1.3 1.306 1.331 1.356 1.369 1.394 1.444 1.506 1.55 1.78 1.8 1.86 1.86 1.86 1.84 1.8]
 V1=[2.03 2.3 1.97 1.97 1.97 2.02 1.97 1.97 1.97 1.97 1.97 1.97 1.97 1.97 1.97 2.16 2.02 2.02 1.95 2.2 1.95 2 1.97 1.97 2 2 2 2 2 2 2.05 2 1.97 1.95 1.98 1.98 2 2.02 2.03 2.03 2.03 1.95 2.03 1.98]
 frec=[220 240 260 280 300 340 380 420 620 1020 1520 2020 2520 3020 4020 5020 6020 8020 10000 12000 14000 16000 17000 18000 19000 20000 21000 22000 22575 23000 24000 25000 26000 27000 30000 35000 40000 80000 100000 200000 400000 800000 1500000 2000000]
 j=Vr./V1
 hold off
 %plot(frec,j) 
 %hold on
 xlabel('frec (Hz)');
ylabel('|H(s)| (db)');

semilogx(w./(2*pi) , 20 * log10(mag) );
hold on
semilogx(frec,20*log10(j));
grid on