import cv2
from src import map
from src import astar
import time

def main():
    radius = 3.8
    wheel_d = 35.4
    step = 1
    threshold = 10
    while True:
        clearance = int(input("Enter the clearance values: "))

        start_point = input('Enter the start_node in the format x,y,theta: ')
        x_start = int(start_point.split(",")[0])
        y_start = int(start_point.split(",")[1])
        theta_start = int(start_point.split(",")[2])

        goal_point = input('Enter the goal_node in the format x,y: ')
        x_goal = int(goal_point.split(",")[0])
        y_goal = int(goal_point.split(",")[1])

        img, image_bw = map.map(clearance, radius)
        free_points = map.free_points(image_bw)


        try:
            if ((x_start, y_start) in free_points and (x_goal, y_goal) in free_points):
                rpm = input('Input RPMs of two wheels in format- rpm1, rpm2: \n')
                rpm1 = int(rpm.split(",")[0])
                rpm2 = int(rpm.split(",")[1])
                break
            else:
                print("Please enter the points which are in free space and right orientation!")
                continue
        except:
            print("Dimensions more than the given map, try again!")

    actions = [(rpm1, 0), (0, rpm1), (rpm1, rpm1),
                 (rpm2, 0), (0, rpm2), (rpm2, rpm1),
                 (rpm1, rpm2), (rpm2, rpm2)]
    start_point = (x_start, y_start, theta_start)
    goal_point = (x_goal, y_goal)
    for i in range(0,5):
        for j in range(0,5):
            img[y_goal+j, x_goal+i] = (0,255,0)
    
    a = time.time()
    
    goal_reached, parents_nodes, visited = astar.astar(start_point, goal_point, free_points, step, threshold, actions, radius, wheel_d)
    print('Reached!')
    print('time taken: ', time.time()-a)
    path = astar.getPath(parents_nodes, start_point, goal_point, visited)
    for point in path:
            # if len(point[0]) == 3:
            x_goal = point[0][0]
            y_goal = point[0][1]
            print(x_goal, y_goal)
            for i in range(0,5):
                for j in range(0,5):
                    img[y_goal+j, x_goal+i] = (0,255,0)
        
    for i in range(len(path)-1):
        point1 = (path[i][0][0], path[i][0][1])
        point2 = (path[i+1][0][0], path[i+1][0][1])
        img = cv2.line(img, point1, point2, (255,0,0), 3)

        cv2.imwrite('visited.jpg', img[::-1,:,:])
    


if __name__ == '__main__':
    main()
