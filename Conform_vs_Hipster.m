clear all;
mult = 0;
rand_num = 1;
S = 50;
C = 50; % number of conformists
H = 50; % number of hipsters
N = 500;
stub = rand(S,1) + rand(S,1)*1i;
stub = stub./abs(stub);
con = rand(C,1) + rand(C,1)*1i;
con = con./abs(con);
hip = rand(H,1) + rand(H,1)*1i;
hip = hip./abs(hip);
% Initializiation of the fashion choises of conformists and hipsters

for i =1:4
stub1(i) = sum(real(stub).^2);
stub2(i) = sum(imag(stub).^2);
con1(i) = sum(real(con).^2);
con2(i) = sum(imag(con).^2);
hip1(i) = sum(real(hip).^2);
hip2(i) = sum(imag(hip).^2);
p1 = (con1(i) + hip1(i) + stub1(i))/(C + H + S);
p2 = (con2(i) + hip2(i) + stub2(i))/(C + H + S);
con = real(con)*(p1 + mult*rand_num) + imag(con)*(p2 + mult*rand_num)*1i;
hip = real(hip)*(p2 + mult*rand_num) + imag(hip)*(p1 + mult*rand_num)*1i;
stub = real(stub)*(1 + mult*rand_num) + imag(stub)*(1 + mult*rand_num)*1i;
con = con./abs(con);
hip = hip./abs(hip);
stub = stub./abs(stub);
end

for i=5:N
stub1(i) = sum(real(stub).^2);
stub2(i) = sum(imag(stub).^2);
con1(i) = sum(real(con).^2);
con2(i) = sum(imag(con).^2);
hip1(i) = sum(real(hip).^2);
hip2(i) = sum(imag(hip).^2);
p1curr = (con1(i-4) + hip1(i-4) + stub1(i-4))/(C + H + S);
p2curr = (con2(i-4) + hip2(i-4) + stub2(i-4))/(C + H + S);
p1prev = (con1(i-2) + hip1(i-2) + stub1(i-2))/(C + H + S);
p2prev = (con2(i-2) + hip2(i-2) + stub2(i-2))/(C + H + S);
p1 = (p1curr + p1prev)/2;
p2 = (p2curr + p2prev)/2;
con = real(con)*(p1 + mult*rand_num) + imag(con)*(p2 + mult*rand_num)*1i;
hip = real(hip)*(p2 + mult*rand_num) + imag(hip)*(p1 + mult*rand_num)*1i;
stub = real(stub)*(1 + mult*rand_num) + imag(stub)*(1 + mult*rand_num)*1i;
con = con./abs(con);
hip = hip./abs(hip);
stub = stub./abs(stub);
end


t = 1:N;
plot(t,con1,t,con2,t,hip1,t,hip2,t,stub1,t,stub2);
legend('Conformists with Style 1','Conformists with Style 2','Hipsters with Style 1','Hipsters with Style 2','Stubborn with Style 1','Stubborn with Style 2');
