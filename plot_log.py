#!/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import sys

# ==============================================================================
# Code used for logging data plotted here
# ==============================================================================

# Set up the logging ===========================================================

#  this->myfile.open (filepath);
#             myfile << "Time,Accel X,Accel Y,Accel Z,Vel X,Vel Y,Vel Z,Pose X,Pose Y,Pose Z\n";

# To be ran when adding data ===================================================

# this->myfile << timestamp<<",,,," <<
#             this->prec_linear_twist_.x<<","<<
#             this->prec_linear_twist_.y<<","<< 
#             this->prec_linear_twist_.z<<","<<
#             this->prec_pose_.x<<","<<
#             this->prec_pose_.y<<","<<
#             this->prec_pose_.z<<"\n";

# ==============================================================================

print("== Log plotter for GO2 ==")
while (True):
    
    if(len( sys.argv ) > 1):
        filename =sys.argv[1]
        
    else:
        filename = input("Name of the csv file to plot:") 

    # Load data
    data = pd.read_csv(filename)

    # Plot
    fig,(A1,A2,A3)= plt.subplots(3,1)
    
    A1.set_title("Acceleration, velocity & pose of GO2" + " [" + filename + "]")
    A1.plot(data['Time'], data['Accel X'],label='a (m/s²)',marker='.',markersize='5',linewidth=1,color='navy')
    A1.plot(data['Time'], data['Vel X'], label='v (m/s)',  marker='.',markersize='5',linewidth=1,color='royalblue')
    A1.plot(data['Time'], data['Pose X'], label='p (m)',   marker='.',markersize='5',linewidth=1,color='deepskyblue')

    A2.plot(data['Time'], data['Accel Y'],label='a (m/s²)',marker='.',markersize='5',linewidth=1,color='navy')
    A2.plot(data['Time'], data['Vel Y'], label='v (m/s)',  marker='.',markersize='5',linewidth=1,color='royalblue')
    A2.plot(data['Time'], data['Pose Y'], label='p (m)',   marker='.',markersize='5',linewidth=1,color='deepskyblue')

    A3.plot(data['Time'], data['Accel Z'],label='a (m/s²)',marker='.',markersize='5',linewidth=1,color='navy')
    A3.plot(data['Time'], data['Vel Z'], label='v (m/s)',  marker='.',markersize='5',linewidth=1,color='royalblue')
    A3.plot(data['Time'], data['Pose Z'], label='p (m)',   marker='.',markersize='5',linewidth=1,color='deepskyblue')

    A1.set_xlabel('Time (s)')
    A1.set_ylabel('X Value')

    A2.set_xlabel('Time (s)')
    A2.set_ylabel('Y Value')

    A3.set_xlabel('Time (s)')
    A3.set_ylabel('Z Value')

    A1.legend()
    A2.legend()
    A3.legend()

    A1.grid()
    A2.grid()
    A3.grid()


    plt.show()