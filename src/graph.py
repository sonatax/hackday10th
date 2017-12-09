import numpy as np
from matplotlib import pyplot as plt

class Graph:
    def __init__(self):
        # 配列
        self.t = np.zeros(100)
        self.y = np.zeros(100)
        self.time = 0
        self.result = 0

        #インタラクティブ描画
        plt.ion()
        plt.figure()
        plt.ylim(0, 10000)
        self.li, = plt.plot(self.t, self.y)
        plt.xlabel("count")
        plt.ylabel("score")

    #while True:
    #try:
    def drawing(self, result):
        print(self)
        # 配列をキューと見たてて要素を追加・削除
        self.t = np.append(self.t, self.time)
        self.t = np.delete(self.t, 0)
        self.y = np.append(self.y, result)
        self.y = np.delete(self.y, 0)

        self.li.set_xdata(self.t)
        self.li.set_ydata(self.y)           
        plt.xlim(min(self.t), max(self.t))
        plt.draw()

        self.time += 1
        #plt.pause(1)

# DEBUG
#graph = Graph();
#while True:
#    try:
#        graph.drawing(10);
#    except KeyboardInterrupt:
#        break
