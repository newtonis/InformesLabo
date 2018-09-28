
s= tf ('s');
R=120;
C=10*10^-9;
L=1000*10^-6;

h1= (s*C*R)/(s^2*L*C+s*R*C+1);
h2= (s^2*L*C+1)/(s^2*L*C+s*R*C+1);
h3= (s^2*L*C)/(s^2*L*C+s*R*C+1);

% step1=h1/s;
% step2=h2/s;
% step3=h3/s;

plot (second1, Volt1)
hold on
% opt = stepDataOptions('InputOffset',-0.25,'StepAmplitude', 0.5);
% step(h1,opt,'r')

%bode 
[mag, pha, w] = bode(H);
mag = squeeze (mag);
pha = squeeze (pha);

%phase
semilogx ( w./(2*pi), pha);

%mag
semilogx( w./(2*pi), 20*log10(mag));


grid on