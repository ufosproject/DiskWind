import numpy as np     # this loads the numpy modules. It is a very powerful package and I would recommend using numpy functions and arrays :)


def eta():         # This defines a function 
    
    data=np.loadtxt('eta.dat')    # This is function to readin txt files. You can google numpy loadtxt to see more options 
    
    test=data.reshape(17,21,25,21,19)     # reshape justs changes the shape of an array eg. a hughe 1D array can be transformed into another shape which is often more convinient.
    # The entries are temp, gas density, Ceta, plasma beta. The 19 collums are described in the info file.

    temp=test[:,0,0,0,4]   # This is a 1D array with the values of the temperature in K
    rho=test[0,:,0,0,5]    # This is a 1D array with the values of the density in g/cm^3
    Ceta=test[0,0,:,0,6]    # This is a 1D array with the values of the Ceta, the non thermal ionizaton rate  1/s
    beta=test[0,0,0,:,7]    # This is a 1D array with the values of the Plasma beta, the ratio of gas pressure and magnetic pressure 2*P/B^2


    print temp,rho,Ceta,beta
