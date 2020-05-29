from csv import reader
import math 


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def rows_readFile(file_name):
    '''
        this function will read the file row by row
    '''
    
    csv_arr =[]
    with open(file_name, 'r') as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            csv_arr.append(row)
        
    
    return csv_arr

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
        temp_row = column_readFile("dataset.csv",counter)
        
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

def subtractor(arr1,arr2):

    counter = 0
    result = []
    while(counter < len(arr1)):
        result.append(arr1[counter] - arr2[counter]) 
        
        counter += 1
    return result

def euclideanCal(v1,v2):
    sub_arr = subtractor(v1,v2)
    power2_arr = []
    result = 0
    summ =0
    counter = 0
    while(counter<len(sub_arr)):
        power2_arr.append(sub_arr[counter]**2)

        counter += 1
    # print("this is power2 arr " + str(power2_arr))

    counter = 0
    while ( counter <len(power2_arr)):

        summ = summ + power2_arr[counter]
        counter +=1

    result = math.sqrt(summ)
    return result


   
def euclD_center(center,data_arr):
    '''
        calculate the euc_distance for the center to all the elemnts
    '''
    result = []
    counter = 0
    distance = 0
    while(counter < len(data_arr)):
        distance = euclideanCal(center,data_arr[counter])
        result.append(distance)
        counter += 1
    return result

def minimum_cal(arr1_euc, arr2_euc,csv_arr):
    counter = 0
    min_res = []
    dist_cntr1 = [] # minimum distances to center1
    dist_cntr2 = [] # minimum distances to center2

    while(counter < len(csv_arr)):
        if(arr1_euc[counter] <= arr2_euc[counter]):
           dist_cntr1.append(csv_arr[counter])
        if(arr2_euc[counter] < arr1_euc[counter]):
            dist_cntr2.append(csv_arr[counter])
  
        counter +=1
        
    return (dist_cntr1 , dist_cntr2)

def avg_cal (arr2d):
    arr_x = []
    arr_y = []
    arr_z = []
    arr_c = []
    avg_x = 0
    avg_y = 0
    avg_z = 0
    avg_c = 0
    counter = 0
    while(counter <len(arr2d)):
        counter1 =0
        while(counter1 < 4):
            arr_x.append(arr2d[counter][0])
            arr_y.append(arr2d[counter][1])
            arr_z.append(arr2d[counter][2])
            arr_c.append(arr2d[counter][3])

            counter1 += 1
        counter += 1

    avg_x = sum(arr_x)/len(arr_x)
    avg_y = sum(arr_y)/len(arr_y)
    avg_z = sum(arr_z)/len(arr_z)
    avg_c = sum(arr_c)/len(arr_c)

    new_cntr = [avg_x, avg_y, avg_z, avg_c]

    return new_cntr


def kmeans(csv_arr):
    center1 = csv_arr[0]
    center2 = csv_arr[1]
    arr1_euc = []
    arr2_euc = []
    new_points1 = []
    new_points2 = []
    counter = 0
    arr1_temp =[]
    arr2_temp =[]
    while(True):
        arr1_euc = euclD_center(center1,csv_arr)
        arr2_euc = euclD_center(center2,csv_arr)
        for point in new_points1:
            arr1_temp.append(point)
        for point in new_points2:
            arr2_temp.append(point)
        new_points1, new_points2 = minimum_cal(arr1_euc,arr2_euc,csv_arr)
        center1 = avg_cal(new_points1)
        center2 = avg_cal(new_points2)
        if(arr1_temp != new_points1 and arr2_temp != new_points2 ):
            break
    return (new_points1, new_points2)
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

arr = rows_readFile("dataset.csv")
arr_csv = strTofloat(arr)
print(arr_csv[0])
print(arr_csv[1])
# print(subtractor(arr_csv[0],arr_csv[1]))
# print(euclideanCal(arr_csv[0],arr_csv[1]))
# print ( euclideanCal([1.2,3.2,1.0],[2.1,3.1,4.0]) )
# print(euclD_center(arr_csv[0],arr_csv))
# a1 , a2 = minimum_cal(arr_csv[0],arr_csv[1],[3,2,1,4])
# print(a1)
# print(a2)

# print(avg_cal([arr_csv[0],arr_csv[1]]))

a1, a2 = kmeans(arr_csv)
print(a1)
print(" ")
print(a2)

# ploter(columnedFile("dataset.csv")) # this Line will plot the File
