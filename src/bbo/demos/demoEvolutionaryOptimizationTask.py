## \file demoEvolutionaryOptimizationTask.py
## \author Freek Stulp
## \brief  Visualizes results of demoEvolutionaryOptimizationTask.cpp
## 
## \ingroup Demos
## \ingroup BBO

import matplotlib.pyplot as plt
import numpy
import subprocess

# Add relative path if PYTHONPATH is not set
import os, sys
lib_path = os.path.abspath('../../../python/')
sys.path.append(lib_path)

import bbo.bbo_plotting

if __name__=='__main__':
    executable = "../../../bin/demoEvolutionaryOptimizationTask"
    
    if (not os.path.isfile(executable)):
        print ""
        print "ERROR: Executable '"+executable+"' does not exist."
        print "Please call 'make install' in the build directory first."
        print ""
        sys.exit(-1);
    
    covar_updates = ["none","decay","adaptation"]

    figure_number = 1;
    for covar_update in covar_updates:
      # Call the executable with the directory to which results should be written
      directory = "/tmp/demoEvolutionaryOptimizationTask/"+covar_update
      command = executable+" "+directory+" "+covar_update
      print command
      subprocess.call(command, shell=True)
      
      fig = plt.figure(figure_number,figsize=(12, 4))
      figure_number += 1;
      axs = [ fig.add_subplot(143), fig.add_subplot(144), fig.add_subplot(142) , fig.add_subplot(141) ]
      bbo.bbo_plotting.plotEvolutionaryOptimizationDir(directory,axs)
      fig.canvas.set_window_title("Optimization with covar_update="+covar_update) 

    plt.show()
    

