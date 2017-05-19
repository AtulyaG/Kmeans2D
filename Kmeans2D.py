import math
import random
#from Kmeans2Dplot import plot

#Kmeansplot2Dplot.py has plot function to display the output.
#You can use your own plotting tool as needed.

#Input number of clusters, 2D data
def Kmeans():
    k = input('Input number of clusters: ')
    #d = input('Input 2D data ')
    d = [[2,2],[3,2],[1,1],[3,1],[1.5,0.5]] #used for sample only
    start(k,d)
    
#Eucledian Distance
def Distance(pt1,pt2):
    dist = math.hypot(pt2[0] - pt1[0], pt2[1] - pt1[1])
    return dist

#Split list into n subsets
def partition(lst, n):
    division = len(lst) / float(n)
    return [lst[int(round(division*i)):int(round(division*(i+1)))] for i in xrange(n)]

#Selects initial clusters and forms centroids
def start(k,d):
    #List initialization
    centroids = []
    input_data_dist = [] #k*k matrix
    centroids_dist = []
    centroid_list = []
    compared = []
    
    #Finding Distance Between Two Points (k*k matrix)
    for i in range(0,len(d)):
        for j in range(0,len(d)):
            #print('Distance between',d[i],'and',d[j], 'is', Distance(d[i],d[j]))
            input_data_dist.append(Distance(d[i],d[j]))

    #input_data_dist is distance between each points
    input_data_length = len(d)

    #Random Sample, Centroids and Centroid allocation
    random_set = random.sample(range(1, input_data_length+1), k)
    print('random',random_set)
  
    for i in range(0,len(random_set)):
        centroids.append(d[random_set[i]-1])

    for i in range(0,len(centroids)):
        for j in range(0,len(d)):
            #print('Distance between',centroids[i],'and',d[j], 'is', Distance(centroids[i],d[j]))
            centroids_dist.append(Distance(centroids[i],d[j]))
    
    #Split it into 'k' lists
    centroid_list = partition(centroids_dist,k)
    
    cl = []
    l = []

    for i in range(0,len(d)):
        for j in range(0,len(centroid_list)):
            cl.append(centroid_list[j][i])
    precompare = partition(cl,len(d))
    check=[]
    for i in range(0,len(precompare)):
        l.append(min(precompare[i]))
        check.append((precompare[i].index(min(precompare[i]))))

    #initialise f,g: g is number of clusters
    f = [[] for x in xrange(k)]
    g = [[] for x in xrange(k)]

    for i in range(0,len(f)):
        for j in range(0,len(d)):
            f[i].append('0')
    
    compared=check
    #print('precomapre',precompare)
    #print(len(precompare))
    #print('-----')
    #print('compared',compared)
    #print(len(compared))
    #print('-----')

    for j in range(0,len(compared)):
        y = compared[j]
        f[y][j]='1'

    for i in range(0,len(d)):
        for j in range(0,len(f)):
            if(f[j][i]=='1'):
                g[j].append(d[i])

    #print('f',f)
    #print(len(f))
    #print('g',g)
    #print(len(f))
    
    #lists for x,y data manipulation
    X = [[] for x in xrange(k)]
    Y = [[] for x in xrange(k)]
    x=[]
    y=[]
    xf=[]
    yf=[]
    FX=[]
    FY=[]
    lengths=[]
    updated_centroids=[]

    for i in range(0,len(g)):
        for j in range(0,len(g[i])):
            x.append(g[i][j][0])
            y.append(g[i][j][1])

    for i in range(0,len(g)):
        lengths.append(len(g[i]))
            
    for i in range(0,len(lengths)):
        for j in range(0,len(g[i])):
            X[i].append(g[i][j][0])
            Y[i].append(g[i][j][1])
        
    for i in range(0,len(X)):
        xf.append(sum(X[i]))
    for i in range(0,len(Y)):
        yf.append(sum(Y[i]))

    #print('-----')
    #print('x',x)
    #print(len(x))
    #print('-----')
    #print('y',y)
    #print(len(y))
    #print('-----')
    #print('X',X)
    #print('-----')
    #print('Y',Y)
    #print('-----')
    #print('length',lengths)
    #print(len(lengths))
    #print('-----')
    #print('xf',xf)
    #print(len(xf))
    #print('-----')
    #print('yf',yf)
    #print(len(yf))
    #print('-----')
          
    for i in range(0,len(xf)):
        if lengths[i] == 0.0 : continue;
        FX.append(xf[i]/float(lengths[i]))
    for i in range(0,len(yf)):
        if lengths[i] == 0.0 : continue;
        FY.append(yf[i]/float(lengths[i]))
        
    flag=[]
    flag = len(FX)
    
    for i in range(0,len(FX)):
        updated_centroids.append(FX[i])
        updated_centroids.append(FY[i])

    updated_centroids = partition(updated_centroids, flag)

    iteration = 0

    #print('FX', FX)
    #print(len(FX))
    #print('-----')
    #print('FY',FY)
    #print(len(FY))
    #print('updated_centroids')
    #print(updated_centroids)
    #print('-----')

    if(centroids == updated_centroids):
        print('Total number of iterations: ')
        print(iteration)
        print('Final Centroids: ')
        print(centroids)
        #print(len(centroids))
        #plot(d, centroids, k)
        
    else:
        while(centroids!=updated_centroids):
            iteration = iteration + 1
            centroids = updated_centroids
            updated_centroids=[]
            
            centroids_dist = []
            centroid_list = []
            compared = []
            del g
            del f
            
            for i in range(0,len(centroids)):
                for j in range(0,len(d)):
                    #print('Distance between',centroids[i],'and',d[j], 'is', Distance(centroids[i],d[j]))
                    centroids_dist.append(Distance(centroids[i],d[j]))

            #Split it into 'k' lists
            centroid_list = partition(centroids_dist,flag)
            
            cl = []
            l = []

            for i in range(0,len(d)):
                for j in range(0,len(centroid_list)):
                    cl.append(centroid_list[j][i])
                    
            precompare = partition(cl,len(d))
            check=[]
            for i in range(0,len(precompare)):
                l.append(min(precompare[i]))
                check.append((precompare[i].index(min(precompare[i]))))

            #initialise f,g: g is number of clusters
            f = [[] for x in xrange(k)]
            g = [[] for x in xrange(k)]

            for i in range(0,len(f)):
                for j in range(0,len(d)):
                    f[i].append('0')
            
            compared=check
            #print('precomapre',precompare)
            #print(len(precompare))
            #print('-----')
            #print('compared',compared)
            #print(len(compared))
            #print('-----')

            for j in range(0,len(compared)):
                y = compared[j]
                f[y][j]='1'

            for i in range(0,len(d)):
                for j in range(0,len(f)):
                    if(f[j][i]=='1'):
                        g[j].append(d[i])

            #print('f',f)
            #print(len(f))
            #print('g',g)
            #print(len(f))
            
            #lists for x,y data manipulation
            X = [[] for x in xrange(k)]
            Y = [[] for x in xrange(k)]
            x=[]
            y=[]
            xf=[]
            yf=[]
            FX=[]
            FY=[]
            lengths=[]
            updated_centroids=[]

            for i in range(0,len(g)):
                for j in range(0,len(g[i])):
                    x.append(g[i][j][0])
                    y.append(g[i][j][1])

            for i in range(0,len(g)):
                lengths.append(len(g[i]))
                    
            for i in range(0,len(lengths)):
                for j in range(0,len(g[i])):
                    X[i].append(g[i][j][0])
                    Y[i].append(g[i][j][1])
                
            for i in range(0,len(X)):
                xf.append(sum(X[i]))
            for i in range(0,len(Y)):
                yf.append(sum(Y[i]))

            #print('-----')
            #print('x',x)
            #print(len(x))
            #print('-----')
            #print('y',y)
            #print(len(y))
            #print('-----')
            #print('-----')
            #print('Y',Y)
            #print('-----')
            #print('length',lengths)
            #print(len(lengths))
            #print('-----')
            #print('xf',xf)
            #print(len(xf))
            #print('-----')
            #print('yf',yf)
            #print(len(yf))
            #print('-----')
                  
            for i in range(0,len(xf)):
                if lengths[i] == 0.0 : continue;
                FX.append(xf[i]/float(lengths[i]))
            for i in range(0,len(yf)):
                if lengths[i] == 0.0 : continue;
                FY.append(yf[i]/float(lengths[i]))
                
            flag=[]
            flag = len(FX)
            
            for i in range(0,len(FX)):
                updated_centroids.append(FX[i])
                updated_centroids.append(FY[i])

            updated_centroids = partition(updated_centroids, flag)

            #print('FX', FX)
            #print(len(FX))
            #print('-----')
            #print('FY',FY)
            #print(len(FY))
            #print('updated_centroids')
            #print(updated_centroids)
            #print('-----')

            if(centroids == updated_centroids):
                print('Total number of iterations: ')
                print(iteration)
                print('Final Centroids: ')
                print(centroids)
                print(len(centroids))
                #plot(d, centroids, k)

Kmeans()
#AdiVarma27: 18May17
