from csv import reader
from csv import writer
import math 


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np




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

    '''
        2ta center migire va bad hameye fasele haro ta in 2ta hesab mikone va bad
        kootah tarin ro beyne in 2ta peyda mikone 
        va oon elementi ke fasele kootah tari nesbat be har markaz dare dar dasteye oon markaz gharar migire


    '''
    index1 , index2 = center_finder(csv_arr)
    center1 = csv_arr[index1]
    center2 = csv_arr[index2]
    arr1_euc = []
    arr2_euc = []
    new_points1 = []
    new_points2 = []
    counter = 0
    arr1_temp =[]
    arr2_temp =[]
    i =0
    while(True):
        arr1_euc = euclD_center(center1,csv_arr)
        arr2_euc = euclD_center(center2,csv_arr)
        arr1_temp = []
        arr2_temp = []
        for point in new_points1:
            arr1_temp.append(point)
        for point in new_points2:
            arr2_temp.append(point)
        new_points1, new_points2 = minimum_cal(arr1_euc,arr2_euc,csv_arr)
        center1 = avg_cal(new_points1)
        center2 = avg_cal(new_points2)
        i +=1
        if(arr1_temp == new_points1 and arr2_temp == new_points2 ):
            print("THIS IS I "+ str(i) )
            
            break
        
    return (new_points1, new_points2)


def d_cal(points1, points2 ):
    counter = 0
    min_arr = []
    while(counter < len(points1)):
        el = points1[counter]
        arr_d = euclD_center(el,points2)
        min_arr.append(min(arr_d))

        counter +=1
    
    return min(min_arr)


def center_finder(csv_arr):
    counter = 0
    max_arr = []
    index_arr =[]
    index_temp1 = 0
    index_temp2 = 0
    max_temp =0
    while(counter < len(csv_arr)):
        el = csv_arr[counter]
        arr_d = euclD_center(el,csv_arr)

        for i in range(len(arr_d)):

            if(arr_d[i] > max_temp):
                max_temp = arr_d[i]
                index_temp1 = counter
                index_temp2 = i

        counter +=1



    return (index_temp1,index_temp2)

# reading and ploter section in down below ~~~~~~~~~~~~~~~~~~ #

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
        temp_row = column_readFile(file_name,counter)
        
        file_col.append(temp_row)
       

        counter +=1

    file_col = strTofloat(file_col)

    return file_col
def ploter(columned_file):
    '''
        this function will plot 4D dots
        just for a test
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


'''

    kari k man kardam ine ke az algorithm Kmeans estefade kardam ke bar asase minmume fasele byne noghat miad 2 daste mikone
    tozih:
    aval 2ta markaz ro entekhab mikonam b in shekl ke miam 2ta noghte k bishtarin fasele ro darand be onvane 
    center 1 va center 2 entekhab mikonam va bad miam fasele tamam noghat ro ta in 2ta center be dast miaram
    bad be har kodom ke nazdik tar bood oon noghtaro mizaram tooye oon daste va hamintowr edame midam

    vaghty ke 1 dowr in etefagh oftad baraye bare 2om bayad 2 ta center jadid entekhab konam va baraye in kar az 
    average noghat har daste estefade kardam , be in soorat ke noghati ke dar dasteye 1 hastand average_x o y o z o c ro hesab kardam
    va noghteye jadid be dast oomad va dobare raveshe bala ra edame dadam
    
    ravesehe bala inghadr edame peyda mikonad ta 2ta liste jadidam ba 2ta liste dowre ghabli yeki shavand dar in marhale
    2ta cluster peyda shodand va braye mohasebeye D kootah tarin faseleye beyne noghate cluster1 va noghate cluster2 ast

    cluster1 tooye file result1.csv va cluster2 tooye file result2.csv rikhte mishavand

    va Output morede nazar soal tooye result.txt rikhte shode ast

'''

arr = rows_readFile("dataset.csv")
arr_csv = strTofloat(arr)
a1, a2 = kmeans(arr_csv)

if(arr_csv[0] in a1):
    file = open("result.txt","w")
    for el in arr_csv:
        if(el in a1):
            file.write("0" + "\n")
        else:
            file.write("1\n")
        
else:
    file = open("result.txt", "w")
    for el in arr_csv:
        if(el in a2):
            file.write("0\n")
        else:
            file.write("1\n")

file.write(str(d_cal(a1,a2)))

file.close()

print("d is equal to:"+ str(d_cal(a1,a2)))
# ploter(columnedFile("dataset.csv")) # this Line will plot the dataset File








with open('result1.csv', 'w',newline='') as write_file:
    csv_writer = writer( write_file )
    for c in a1:
        csv_writer.writerow(c)

with open('result2.csv', 'w',newline='') as write_file:
    csv_writer = writer( write_file )
    for c in a2:
        csv_writer.writerow(c)



# ploter(columnedFile("result2.csv"))