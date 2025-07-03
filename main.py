import waypoint_rrt as wp
import waypoint_rrt2 as wp2
import visualization as visual
import numpy as np

def main():
    bounds = wp.Boundaries()
    bounds.add_bound((250,500), (500, 0))
    bounds.add_bound((0, 1000), (500, 550))
    bounds2 = wp2.Boundaries()
    bounds2.add_bound((250,500), (500, 0))
    bounds2.add_bound((0, 1000), (500, 550))
    # print(bounds.bound_list[:20])
    start = (1, 1)
    goal = (999, 999)
    thresh = 100
    
    
    

    # Compares regular RTT and RRT*
    # costs = np.empty((2, 10))
    # for i in range(10):
    #     rrt = wp.RRT(start, goal, bounds, thresh)
    #     rrt()
    #     costs[0][i] = rrt.total_cost
    #     rrt = wp2.RRT(start, goal, bounds, thresh, 2.75)
    #     rrt()
    #     costs[1][i] = rrt.total_cost
    # print("Old Average Cost:", np.mean(costs[0]))
    # print("New Average Cost:", np.mean(costs[1]))
    # print("Old Min Cost:", min(costs[0]))
    # print("New Min Cost:", min(costs[1]))

    # Compares Different Factors for RTT*
    # factors = [1, 1.5, 2, 2.25, 2.5, 2.75, 3]
    # costs = np.empty((7, 20))
    # means = np.empty(7)
    # for i in range(7):
    #     for j in range(20):
    #         rrt = wp2.RRT(start, goal, bounds, thresh, factors[i])
    #         rrt()
    #         costs[i][j] = rrt.total_cost
    #     means[i] = np.mean(costs[i])
    # print(means)

    #Visualization
    rrt = wp2.RRT(start, goal, bounds, thresh, 2.75)
    vis = visual.RRTvis(rrt)
    vis.plot_all()

if __name__ == "__main__":
    main()