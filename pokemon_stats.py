import csv
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from scipy.spatial.distance import euclidean
import random
import numpy

def load_data(filepath):
    with open(filepath, newline= '') as csvfile:
        reader = csv.DictReader(csvfile)
        return_list = []
        i = 0
        for row in reader:
            if (i >= 20):
                break
            dic1 = dict(row)
            # delete column of 'Generation' and 'Legendary'
            del dic1['Generation']
            del dic1['Legendary']
            return_list.append(dic1)
            i += 1
        return return_list


def calculate_x_y(stats):
    x = int(stats['Attack']) + int(stats['Sp. Atk']) + int(stats['Speed'])
    y = int(stats['Defense']) + int(stats['Sp. Def']) + int(stats['HP'])
    return (x,y)

def hac(dataset):
    u = 0
    h = dataset
    for q in dataset:
        if(q[0] == float('NaN')):
            h.pop(u)
        elif (q[1] == float('NaN')):
            h.pop(u)
        elif (q[0] == float('inf')):
            h.pop(u)
        elif (q[1] == float('inf')):
            h.pop(u)
        u += 1

    dataset = h

    m = len(dataset) #length of the dataset
    i = 0
    dic = {}

    # matches data with labels in dic
    for item in dataset:

        dic[str(i)] = item
        i += 1




    a = [] # the list of information about clusters
    for i in range(m-1):
        # the list of size 4
        list = []
        #temp list
        shortlist = []
        point1, point2, dismin, key1, key2 = calculate_shortest_two_points(dic)

        l = 0

        #iterate through every two loops in the dic
        if type(dic.get(key1)) == type(list):
            for i in dic.get(key1):
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

        #delete clusters
        try:
            del dic[key1]
            del dic[key2]
        except KeyError:
            #print(1)
            pass
        ###print(dic)

        key1 = int(key1)
        key2 = int(key2)

        #compare the size of keys
        if key1 <key2:
            list.append(key1)
            list.append(key2)
        elif(key1 > key2):
            list.append(key2)
            list.append(key1)


        list.append(dismin)
        list.append(l)
        a.append(list)
    b = numpy.matrix(a)
    return b







# returns point1, point2, mindis, and key1, key2 of shortest points
def calculate_shortest_two_points(dic):
    key1 = 0
    key2 = 0
    dismin = float('inf')
    for key, value in dic.items():
        dis = float('inf')
        tup3 = ()
        tup4 = ()
        for k, value1 in dic.items():
            if(value1 == value):
               continue
            dis1 = float('inf')



            if type(value) == type(list):


                for i in value:
                    #print(i)
                    #print(value1)
                    if type(value1) == type(list):

                        for j in value1:

                            #if (value == j):
                                #continue
                            dis3 = euclidean(i, j)
                            if(dis3 < dis1):
                                dis1 = dis3
                                tup3 = i
                                tup4 = j
                    else:


                        dis1 = euclidean(i, value1)
                        tup3 = i
                        tup4 = value1
                    #print(dis1)

                    if dis1 < dis:
                        dis = dis1
                        tup1 = tup3
                        tup2 = tup4
                    #print(dis1)

            elif type (value1) == type(list):
#                tup3 = ()
#                tup4 = ()
                for j in value1:

                    if (value == j):
                        continue
                    if type(value) == type(list):
                        for i in value:
                            dis3 = euclidean(i, j)
                            if( dis3 < dis1):
                                dis1 = dis3
                                tup3 = i
                                tup4 = j
                    else:
                        dis1 = euclidean(value, j)
                        tup3 = value
                        tup4 = j
                    #print(dis1)
                    if (dis1 < dis):
                        dis = dis1
                        tup1 = tup3
                        tup2 = tup4




            else:
                dis = euclidean(value, value1)
                tup1 = value
                tup2 = value1
            #print(dis)

            if(dis < dismin):
                dismin = dis
                return_tup1 = tup1
                return_tup2 = tup2
                key1 = key
                key2 = k


    return return_tup1, return_tup2, dismin, key1, key2


def random_x_y(m):
    list = []
    for x in range(m):

        a = random.randint(1, 360)
        b = random.randint(1, 360)

        tup = (a, b)

        list.append(tup)

    return list

def imshow_hac(dataset):
    u = 0
    h = dataset
    for q in dataset:
        if(q[0] == float('NaN')):
            h.pop(u)
        elif (q[1] == float('NaN')):
            h.pop(u)
        elif (q[0] == float('inf')):
            h.pop(u)
        elif (q[1] == float('inf')):
            h.pop(u)
        u += 1

    dataset = h

    m = len(dataset)  # length of the dataset
    i = 0
    dic = {}
    # matches data with label in dic
    for item in dataset:
        dic[str(i)] = item
        i += 1

    a = []

    for i in dataset:
        plt.scatter(i[0], i[1])

    plt.ion()

    for i in range(m - 1):
        list = []
        shortlist = []

        # set_x = []
        # set_y = []

        point1, point2, dismin, key1, key2 = calculate_shortest_two_points(dic)
        # set_x.append(point1[0])
        # set_x.append(point2[0])
        # set_y.append(point1[1])
        # set_y.append(point2[1])

        plt.plot([point1[0], point2[0]], [point1[1], point2[1]])
        plt.pause(0.1)
        # print(point1, point2)

        #print(point1, point2)

        l = 0

        if type(dic.get(key1)) == type(list):
            # print(dic.get(key1))
            for i in dic.get(key1):
                # print(i)
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

        try:
            del dic[key1]
            del dic[key2]
        except KeyError:
            print(1)
            pass
        ###print(dic)

        key1 = int(key1)
        key2 = int(key2)

        if key1 < key2:
            list.append(key1)
            list.append(key2)
        elif (key1 > key2):
            list.append(key2)
            list.append(key1)

        plt.ioff()

        list.append(dismin)
        list.append(l)
        a.append(list)

    plt.pause(5)



























if __name__=="__main__":
    a = load_data('Pokemon.csv')
    list = []
    #print(a)

    for i in range(20):
        list.append(calculate_x_y(a[i]))
#    print(list)
    hac(list)
    #print(list)

    imshow_hac(list)
    #print(list)

    random_x_y(30)


    X = list
#    print(X)
    Z = linkage(X)
    #print(Z)
#    fig = plt.figure(figsize=(25, 10))
#    dn = dendrogram(Z)
#    Z = linkage(X, 'single')
#    fig = plt.figure(figsize=(25, 10))
#    dn = dendrogram(Z)
#    plt.show()


    #print(a, b, c, d, e)
    #print(dic)