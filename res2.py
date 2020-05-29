from csv import reader
import math 


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def column_readFile(file_name,col):
    '''
        read the file and return the column with number "col"
        for example if col == 2 then it will return the 2th column of the file
    '''
    arr_res = []
    with open(file_name, "r") as csv_file:
        csv_reader = reader(csv_file)
        for lines in csv_reader:
            arr_res.append(lines[col])
    return arr_res

def columnedFile(file_name):
    '''
        this function will read the file column by column and return all the columns in a 2d array
    '''
    counter =0
    file_col = []
    while(counter <4):
        temp_row = column_readFile(file_name,counter)
        
        file_col.append(temp_row)
        print(temp_row)

        counter +=1

    file_col = strTofloat(file_col)

    return file_col


def strTofloat(Arr2D):
    '''
        this function will change type of a 2d STRING array to a 2d FLOAT array
    '''
    csv_int_arr = []
    for arr_el in Arr2D:
        arr_el = [float(i) for i in arr_el] 
        
        csv_int_arr.append(arr_el)

    return csv_int_arr

def ploter(columned_file):
    '''
        this function will plot 4D dots
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = columned_file[0]
    y = columned_file[1]
    z = columned_file[2]
    c = columned_file[3]

    img = ax.scatter(x, y, z, c=c, cmap=plt.magma())
    fig.colorbar(img)
    plt.show()
   
ploter(columnedFile("result2.csv"))