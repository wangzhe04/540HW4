import csv
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from scipy.spatial.distance import euclidean
import random
import math

def load_data(filepath):
    with open(filepath, newline= '') as csvfile:
        reader = csv.DictReader(csvfile)
        return_list = []
        i = 0
        for row in reader:
            if (i >= 20):
                break
            return_list.append(dict(row))
            i += 1
        return return_list

#        b = list(reader)
#        return_list = []
#        for item in b [:20]:
#            return_list.append(item)

#       return return_list

def calculate_x_y(stats):
    x = int(stats['Attack']) + int(stats['Sp. Atk']) + int(stats['Speed'])
    y = int(stats['Defense']) + int(stats['Sp. Def']) + int(stats['HP'])
    return (x,y)

def hac(dataset):
    m = len(dataset) #length of the dataset
    i = 0
    dic = {}
    c = []
    for item in dataset:

        dic[str(i)] = item
        i += 1
    print(dic)
    list_x = []
    dismin = 0



    a = []
    for i in range(m-1):
        list = []
        shortlist = []
        point1, point2, dismin, key1, key2 = calculate_shortest_two_points(dic)
        #print(point1)
        #print(point2)
        #print(dismin)

        print(key1)
        print(key2)

        l = 0


        if type(dic.get(key1)) == type(list):
            #print(dic.get(key1))
            for i in dic.get(key1):
                #print(i)
                shortlist.append(i)
                l += 1
            if type(dic.get(key2)) == type(list):
                for i2 in dic.get(key2):
                    shortlist.append(i2)
                    l += 1
            else:
                shortlist.append(dic.get(key2))
                l += 1

        elif type(dic.get(key2)) == type(list):
            for i in dic.get(key2):
                shortlist.append(i)
                l += 1
            if type(dic.get(key1)) == type(list):
                for i2 in dic.get(key1):
                    # print(i)
                    shortlist.append(i2)
                    l += 1
            else:
                shortlist.append(dic.get(key1))
                l += 1

        else:
            shortlist.append(dic.get(key1))
            l += 1
            shortlist.append(dic.get(key2))
            l += 1
        dic[str(m)] = shortlist
        m = m + 1

        #dic = removekey(dic, key1)
        #print(dic)
        #dic = removekey(dic, key2)
        #print(dic)

        try:
            del dic[key1]
            del dic[key2]
        except KeyError:
            #print(1)
            pass
        print(dic)

        key1 = int(key1)
        key2 = int(key2)

        if key1 <key2:
            list.append(key1)
            list.append(key2)
        elif(key1 > key2):
            list.append(key2)
            list.append(key1)


        #print(dismin)
        list.append(dismin)
        list.append(l)
        a.append(list)
    print(a)


#    a = []
#    for i in range(m-1):
#        a.append([]*4)
#    a[0].append(1)
#    a[0].append(2)





    #print(a)
    #print(dic)
#def multiply_list(list):
#    result = 1
#    for x

def calculate_shortest_two_points(dic):
    tup1 = ()
    tup2 = ()
    key1 = 0
    key2 = 0
    dismin = float('inf')
    for key, value in dic.items():
        dis = float('inf')
        for k, value1 in dic.items():
            if(value1 == value):
                continue


            if type(value) == type(list):

                for i in value:
                    #print(i)
                    #print(value1)
                    if type(value1) == type(list):

                        for j in value1:
                            if (value == j):
                                continue
                            dis1 = euclidean(i, j)
                    else:


                        dis1 = euclidean(i, value1)
                    #print(dis1)

                    if dis1 < dis:
                        dis = dis1
                    if (math.ceil(dis1) == 68):
                       print(i)

            elif type (value1) == type(list):

                for j in value1:
                    if (value == j):
                        continue
                    if type(value) == type(list):
                        for i in value:
                            dis1 = euclidean(i, j)
                    else:
                        dis1 = euclidean(value, j)
                    #print(dis1)
                    if (dis1 < dis):
                        dis = dis1
                    if(math.ceil(dis1) == 68):
                        print(j)

            else:
                dis = euclidean(value, value1)

            if(dis < dismin):
                dismin = dis
                tup1 = value
                tup2 = value1
                key1 = key
                key2 = k

    return tup1, tup2, dismin, key1, key2

def removekey(d, key):
    r = dict(d)
    #print(key)
    del r[key]
    return r

def random_x_y(m):
    list = []
    for x in range(m):

        a = random.randint(1, 360)
        b = random.randint(1, 360)

        tup = (a, b)

        list.append(tup)

    return list



def shortestDist(points):
    sh = float("inf")
    for i in range(1, len(points)):
        d = euclidean(points[i - 1], points[i])
        if d < sh:
            sh = d
    return sh

def calculate_dist(x1, x2, y1, y2):
    return ((x1-x2)^2 + (y1-y2)^2)^0.5



















if __name__=="__main__":
    a = load_data('Pokemon.csv')
    list = []
    #print(a[0])
    #print(calculate_x_y(a[0]))
    #list.append(calculate_x_y(a[0]))
    #list.append(calculate_x_y(a[1]))
    #list.append(calculate_x_y(a[2]))
    #list.append(calculate_x_y(a[3]))
    #list.append(calculate_x_y(a[4]))
    #list.append(calculate_x_y(a[5]))

    for i in range(20):
        list.append(calculate_x_y(a[i]))
#    print(list)
    hac(list)
    #print(list)

    #print(random_x_y(30))


    X = list
#    print(X)
    Z = linkage(X)
    print(Z)
#    fig = plt.figure(figsize=(25, 10))
#    dn = dendrogram(Z)
#    Z = linkage(X, 'single')
#    fig = plt.figure(figsize=(25, 10))
#    dn = dendrogram(Z)
#    plt.show()
