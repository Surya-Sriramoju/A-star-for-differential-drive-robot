import numpy as np
import heapq as heap
import cv2
import math




def astar(start_point, goal_point, free_points, step_size, threshold, actions, radius, wheel_d):
    visited = []
    queue = []
    node_cost = {}
    parent_nodes = {}
    goal_reached = False
    node_cost[start_point] = 0
    thresh_nodes = set()
    heap.heappush(queue, (0, start_point))

    
    if dist_between_nodes(start_point, goal_point) < threshold:
        
        goal_reached = True
    
    while not goal_reached and queue:
        current_cost, current_node = heap.heappop(queue)
        if node_visited(thresh_nodes, current_node, threshold):
            continue
        visited.append(current_node)
        new_nodes = populate_nodes(current_node, free_points, step_size, actions, radius, wheel_d)
        for new_node, new_action, cost in new_nodes:
            # print(new_node[:2])
            status, node_cost, queue, parent_nodes = calculate_cost(new_node, current_node, node_cost, queue, parent_nodes, cost, goal_point, threshold, new_action)
            if status:
                thresh_nodes.add((current_node[0]//threshold, current_node[1]//threshold))
                visited.append(new_node)
                goal_reached = True
                break
    return goal_reached, parent_nodes, visited






