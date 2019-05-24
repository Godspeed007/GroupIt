#Trademark ~ El Patron ~
#Finding clusters of various video games based on their sales value by taking use of K-Means Clustering

import math

c1=[7.55,50.00] #high sales cluster
c2=[5.25,28.75] #medium sales cluster
c3=[3.20,14.80] #low sales cluster
new_c1=[] #to save the new value c1
new_c2=[] #to save the new value c2
new_c3=[] #to save the new value c3
dicdata={} #To accommodate the data that becomes the calculation parameter
c1cluster=[]
c2cluster=[]
c3cluster=[]
count=0
count1=0

#calculate euclidean distance
def euclidean(x1, y1, x2, y2):    
    S = 0.0
    S = math.sqrt(( ( float(x1) - y1 )**2 )+( ( float(x2) - y2 )**2 ))
    return S

#open the dataset file for processing
with open('videogames.csv') as file:
    for line in file:
        count = count + 1
        if count == 1:
            continue
        else:
            x = line.split(',')
            dicdata[x[0]] = {'OTHERSALES':x[8], 'GLOBALSALES':x[9]}
            valc1=euclidean(x[8],c1[0],x[9],c1[1])
            valc2=euclidean(x[8],c2[0],x[9],c2[1])
            valc3=euclidean(x[8],c3[0],x[9],c3[1])
            if valc1 < valc2 and valc1 < valc3:
                c1cluster.append(x[0]) #enter the high sales cluster
            elif valc2 < valc1 and valc2 < valc3:
                c2cluster.append(x[0]) #enter the medium sales cluster
            elif valc3 < valc1 and valc3 < valc2:
                c3cluster.append(x[0]) #enter the low sales cluster
            else:
                c1cluster.append(x[0])

temp_osl1 = 0
temp_gsl1 = 0
temp_osl2 = 0
temp_gsl2 = 0
temp_osl3 = 0
temp_gsl3 = 0
for i in c1cluster:
    temp_osl1 = temp_osl1 + float(dicdata[i]['OTHERSALES'])
    temp_gsl1 = temp_gsl1 + float(dicdata[i]['GLOBALSALES'])
for j in c2cluster:
    temp_osl2 = temp_osl2 + float(dicdata[j]['OTHERSALES'])
    temp_gsl2 = temp_gsl2 + float(dicdata[j]['GLOBALSALES'])
for k in c3cluster:
    temp_osl3 = temp_osl3 + float(dicdata[k]['OTHERSALES'])
    temp_gsl3 = temp_gsl3 + float(dicdata[k]['GLOBALSALES'])

new_c1.append(float(temp_osl1) / len(c1cluster))
new_c1.append(float(temp_gsl1) / len(c1cluster))
new_c2.append(float(temp_osl2) / len(c2cluster))
new_c2.append(float(temp_gsl2) / len(c2cluster))
new_c3.append(float(temp_osl3) / len(c3cluster))
new_c3.append(float(temp_gsl3) / len(c3cluster))
    
#re-calculate the centroid value
while c1 != new_c1 and c2 != new_c2 and c3 != new_c3:
    count1 += 1
    c1 = list(new_c1)
    c2 = list(new_c2)
    c3 = list(new_c3)
    del c1cluster[:]
    del c2cluster[:]
    del c3cluster[:]
    with open('videogames.csv') as file:
        count = 0
        for line in file:
            count = count + 1
            if count == 1:
                continue
            else:
                x = line.split(',')
                valc1=euclidean(x[8],c1[0],x[9],c1[1])
                valc2=euclidean(x[8],c2[0],x[9],c2[1])
                valc3=euclidean(x[8],c3[0],x[9],c3[1])
                if valc1 < valc2 and valc1 < valc3:
                    c1cluster.append(x[0])
                elif valc2 < valc1 and valc2 < valc3:
                    c2cluster.append(x[0])
                elif valc3 < valc1 and valc3 < valc2:
                    c3cluster.append(x[0])
                else:
                    c1cluster.append(x[0])

    del new_c1[:]
    del new_c2[:]
    del new_c3[:]
    temp_osl1 = 0
    temp_gsl1 = 0
    temp_osl2 = 0
    temp_gsl2 = 0
    temp_osl3 = 0
    temp_gsl3 = 0
    for i in c1cluster:
        temp_osl1 = temp_osl1 + float(dicdata[i]['OTHERSALES'])
        temp_gsl1 = temp_gsl1 + float(dicdata[i]['GLOBALSALES'])
    for j in c2cluster:
        temp_osl2 = temp_osl2 + float(dicdata[j]['OTHERSALES'])
        temp_gsl2 = temp_gsl2 + float(dicdata[j]['GLOBALSALES'])
    for k in c3cluster:
        temp_osl3 = temp_osl3 + float(dicdata[k]['OTHERSALES'])
        temp_gsl3 = temp_gsl3 + float(dicdata[k]['GLOBALSALES'])
    
    #insert a new centroid
    new_c1.append(float(temp_osl1) / len(c1cluster))
    new_c1.append(float(temp_gsl1) / len(c1cluster))
    new_c2.append(float(temp_osl2) / len(c2cluster))
    new_c2.append(float(temp_gsl2) / len(c2cluster))
    new_c3.append(float(temp_osl3) / len(c3cluster))
    new_c3.append(float(temp_gsl3) / len(c3cluster))

#Output Program    
print ("CLUSTERING DONE")
print
print ("TOTAL ITERATION = ", count1)
print ("Final centroid cluster 1 (High Sales) = ", c1)
print ("Final centroid cluster 2 (Medium Sales) = ", c2)
print ("Final centroid cluster 3 (Low Sales) = ", c3)
print
print
print( "=========CLUSTERING RESULTS=========")
print
print ("CLUSTER 1 (High Sales):")
print (c1cluster)
print
print
print
print ("CLUSTER 2 (Medium Sales):")
print (c2cluster)
print
print
print
print ("CLUSTER 3 (Low Sales):")
print (c3cluster)

