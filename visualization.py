from matplotlib import collections as mc, patches, pyplot as plt
import numpy as np
from waypoint_rrt import ExceededMaxPointsException

class RRTvis():

    def __init__(self, rrt):
        self.rrt = rrt
        self.index = 0
        plt.ion()


    def plot_all(self):
        try:
            self.rrt()
            path = self.rrt.extract_path()
            goal_seg = np.array((self.rrt.goal.prev.as_tuple(), self.rrt.goal.as_tuple())).reshape(1, 2, 2)
        except(ExceededMaxPointsException):
            print("RIP")
            path = []
            goal_seg = np.array([], dtype=np.int64).reshape(0, 2, 2)

        bounds = self.rrt.bounds
        
        x = self.rrt.coords[ : self.rrt.index, 0]
        y = self.rrt.coords[ : self.rrt.index, 1]

        line_segs = np.concatenate((self.rrt.prev_coords[ : self.rrt.index - 1].reshape((self.rrt.index - 1), 1, 2), 
            self.rrt.coords[1 : self.rrt.index].reshape((self.rrt.index - 1), 1, 2)), axis=1)
        
        line_segs = np.concatenate((line_segs, goal_seg), axis=0)

        fig, ax = plt.subplots()
        txt = "Cost: " + str(self.rrt.total_cost)
        plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)


        rect = patches.Rectangle((250, 0), 250, 500, edgecolor='r', facecolor='none')
        h = 450
        rect2 = patches.Rectangle((0, 1000 - h), 500, h, edgecolor='r', facecolor='none')
        outer_bound = patches.Rectangle((0, 0), 1000, 1000, edgecolor='g', facecolor='none')
        lc = mc.LineCollection(line_segs)

        red_rgba = (1, 0, 0, 1)

        path_col = mc.LineCollection(path, colors=[red_rgba])

        ax.add_collection(lc)
        ax.add_collection(path_col)
        ax.add_patch(rect)
        ax.add_patch(rect2)
        ax.add_patch(outer_bound)

        plt.scatter(x, y)
        plt.scatter(*self.rrt.goal.as_tuple(), c='r')
        plt.show(block = True)
