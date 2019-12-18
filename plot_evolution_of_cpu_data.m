%Written by Dr David Harris-Birtill on 18/12/2019
%Uses data from http://cpudb.stanford.edu/download (accessed 28/10/2019)
%
%Note that the data used is the processor.csv file which was then sorted by
%date and then read in here
%
%The data sorted by date used here can be downloaded from https://github.com/dcchb/ComputationTime/blob/master/processor_sorted_by_date.csv

clear all
%Load data:
data = importdata("processor_sorted_by_date.csv", ',',1);

%date data finishes at line 1389 and starts at line 2
%date is column 13 in data.textdata
date_cell = data.textdata(2:1389,13);
date = datetime(date_cell, 'InputFormat', 'dd/MM/yyyy');

%clock speed is column 14 in data.textdata
clock_speed_cells = data.textdata(2:1389,14);
clock_speed=zeros(size(clock_speed_cells,1),size(clock_speed_cells,2));
clock_speed=str2double(clock_speed_cells);%in MHz

%number of cores is column 17 in data.textdata
numcores_cells = data.textdata(2:1389,17);
%numcores = cell2mat(numcores_cells);
numcores=zeros(size(numcores_cells,1),size(numcores_cells,2));
numcores=str2double(numcores_cells);

%number of transistors is column 2 of data.data
number_of_transistors = data.data(1:1388,2)*1000;%now in number of thoushands (rather than in number of millions)

figure
trans_f = semilogy(date, number_of_transistors, 'rx');
set(gca,'fontsize', 16);
xlabel('Year');
hold on
clock_speed_f = semilogy(date, clock_speed, 'bo');
hold on
cores_f = semilogy(date, numcores, 'k+');
xlabel('Year');
legend([trans_f, clock_speed_f, cores_f],'Num transistors (1000s)','Clock Speed (MHz)','Number of cores','Location','NorthWest')
xlim([datetime('1970-01-01') datetime('2015-01-01')]);
saveas(gcf,'Num_transistors_num_cores_and_clock_speed_over_time','png');
