import matplotlib.pyplot as plt

def plot(d, centroids, k):
    x=[]
    y=[]
    xc = []
    yc = []
    
    for i in range(0,len(d)):
        x.append(d[i][0])
        y.append(d[i][1])

    for i in range(0,len(centroids)):
        xc.append(centroids[i][0])
        yc.append(centroids[i][1])

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_aspect(1.0/ax1.get_data_ratio())

    ax1.scatter(x,y, marker="s", c='b')
    ax1.scatter(xc[0],yc[0], marker="s", c='r', label='cluster centre 1')
    ax1.scatter(xc[1],yc[1], marker="s", c = 'y', label='cluster centre 2')
    plt.legend(loc='upper left');
    ax1.set_title('K-Means 2D')
    plt.show()
