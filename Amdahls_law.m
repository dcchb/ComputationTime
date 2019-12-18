%Amdahls law
%
%Equation and info from:
%See paper: Mark D., and Michael R. Marty. "Amdahl's law in the multicore era." Computer 41.7 (2008): 33-38.
% https://research.cs.wisc.edu/multifacet/papers/ieeecomputer08_amdahl_multicore.pdf
%
%Code written by David Harris-Birtill on 29/11/2019
%

%The law:
number_of_cores = 1:100;

fraction_of_parallel_time_95 = 0.95;
Speedup_95 = 1./((1-fraction_of_parallel_time_95)+(fraction_of_parallel_time_95./number_of_cores));

fraction_of_parallel_time_75 = 0.75;
Speedup_75 = 1./((1-fraction_of_parallel_time_75)+(fraction_of_parallel_time_75./number_of_cores));

fraction_of_parallel_time_50 = 0.50;
Speedup_50 = 1./((1-fraction_of_parallel_time_50)+(fraction_of_parallel_time_50./number_of_cores));

figure
plot(number_of_cores,Speedup_95,'LineWidth',4,'LineStyle','-','Color','r');
hold on
plot(number_of_cores,Speedup_75,'LineWidth',4,'LineStyle','--','Color','b');
hold on
plot(number_of_cores,Speedup_50,'LineWidth',4,'LineStyle','-.','Color','k');
set(gca,'fontsize', 16);
xlim([1 100])
ylim([1 18])
xlabel('Number of Cores');
ylabel('Speedup Factor');
legend({'95%','75%','50%'},'Location','northwest')
print(gcf,'Amdahls_law_plot.png','-dpng','-r300'); %produces higher resolution image than saveas


