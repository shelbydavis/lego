import csv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__' :
    time = []
    light_1 = []
    light_2 = []
    motor_b = []
    motor_c = []
    with open('log.csv', 'rU') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data :
            time.append(float(row[0]))
            light_1.append(int(row[1]))
            light_2.append(int(row[2]))
            motor_b.append(int(row[3]))
            motor_c.append(int(row[4]))
    
    fig, axs = plt.subplots(2,1)
    axs[0].plot(time, light_1, time, light_2)
    axs[0].set_xlabel('time')
    axs[0].set_ylabel('reflected light')

    time_ = []
    light_1_ = []
    light_2_ = []
    motor_b_ = []
    motor_c_ = []
    for (t,l1,l2,mb,mc) in zip(time, light_1, light_2, motor_b, motor_c) :
        if len(time_) == 0 or abs(mb - motor_b_[-1]) >= 5:
            time_.append(t)
            light_1_.append(l1)
            light_2_.append(l2)
            motor_b_.append(mb)
            motor_c_.append(mc)
            
    weights = [-0.5,-0.2,0,0.2,0.2]
    c_data_1 = np.convolve(light_1_,weights,mode='same')
    c_data_2 = np.convolve(light_2_,weights,mode='same')
    
    axs[1].plot(time_, c_data_1, time_, c_data_2)
    axs[1].set_xlabel('time')
    axs[1].set_ylabel('convolution_value')
    fig.tight_layout()
    plt.show()
