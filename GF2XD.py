import pandas as pd
file = input('File name?')
profileNum=input('Profile num?')
data = pd.read_csv(file, sep='	')
data['y[m]'] = data['y[m]'].astype(int)
cols = ['y[m]', 'Cond.1[mS/m]', 'Cond.2[mS/m]', 'Cond.3[mS/m]']
soundings = data[cols].set_index(cols[0])
df = pd.DataFrame(soundings)
soundingNums=df.shape[0]
def getSoundings(datafile):
    for i in range(soundingNums):
        filename='kp{}_{}'.format(profileNum, i)
        S = datafile.loc[i]
        sample = open(filename + '.TEM', 'w') 
        print('     {}            309.000               0.0000       0.0000\n                                                       \n                                                  \n                                                                      \n           0.000     0.000     0.000     0.000     0.000    0   58 F F\n   No.      TIME (msec)     nV/m**2\n    1   3.0000E+04   {}\n    2   3.0000E+04   {}\n    3   3.0000E+04   {}'.format(filename,S[0],S[1],S[2]), file =sample)
        sample.close() 
getSoundings(df)