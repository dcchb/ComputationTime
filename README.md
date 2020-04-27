# ComputationTime
Code and data that goes with the Computation Time paper by D. Harris-Birtill and R. Harris-Birtill:

D Harris-Birtill and R Harris-Birtill, "Understanding computation time: A critical discussion of time as a computational performance metric", Time in Variance (The Study of Time XVII), Brill.

If you use this code, please cite our paper.

Below are details of the files:

Amdahls_law.m is a Matlab script to create a plot of Amdahl's law (shown as Figure 4 in the paper). Showing the increase in speed as a function of the number of cores in three different scenarios, where the execution time for the part of the code that can be run in parallel is 50\%, 75\%, and 95\% of the total time to run.

plot_evolution_of_cpu_data.m is a Matlab script to plot the evolution of CPUs (shown as Figure 2 in the paper). This plot shows, on a log scale, the number of transistors (crosses), the clock speed (circles), and the number of physical cores (plus signs) in different processors over time. The figure has been made using data from the Stanford CPU Database, using the details of 1,388 processors in which information of the release dates was published. The database was originally discussed in [1] and the database has since been updated and can be downloaded from \url{http://cpudb.stanford.edu/download} (accessed 28 October 2019)). Note that sometimes not all three parts (clock speed, number of transistors, and number of cores) for some processors are in the database, and therefore only the known parts are plotted here.
[1] Danowitz, Andrew, Kyle Kelley, James Mao, John P. Stevenson, and Mark Horowitz. 2012. “CPU DB:recording microprocessor history.” Communications of the ACM55 (4): 55–63.

processor_sorted_by_date.csv is the data used from [1] which can be read in from the plot_evolution_of_cpu_data.m file.

Computation_time_reporter.py is a python script to automatically generate the text for reporting time, automatically retrieving the hardware details (such as CPU clock speed, number of physical cores, number of virtual cores, RAM and Operating system). When you run this file using the command "python Computation_time_reporter.py" then the file "Computation_time_text.txt" will be produced in the same directory which contains the text.

Computation_time_reporter.exe is a Windows executable which creates an executable for the above Computation_time_reporter.py script. This means that Windows users should be able to just run the exe file (by double clicking on it) to generate the text file in the same directory that the exe is in (reducing the need to open a command window or install dependencies). Note that this was generated in a Windows 10.0.18362 operating system.

Computation_time_reporter_generate_exe.py is a python script which generates the above exe file.
