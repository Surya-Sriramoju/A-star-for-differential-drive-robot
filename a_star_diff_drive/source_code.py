import cv2
from src import map

def main():
    radius = 3.8
    wheel_d = 35.4
    step = 1
    while True:
        clearance = int(input("Enter the clearance values: "))

        start_point = input('Enter the start_node in the format x,y,theta: ')
        x_start = int(start_point.split(",")[0])
        y_start = int(start_point.split(",")[1])
        theta_start = int(start_point.split(",")[2])

        goal_point = input('Enter the goal_node in the format x,y: ')
        x_goal = int(goal_point.split(",")[0])
        y_goal = int(goal_point.split(",")[1])

        image, image_bw = map.map(clearance, radius)
        cv2.imwrite('map_bw.jpg', image_bw)
        free_points = map.free_points(image_bw)

        try:
            if ((x_start, y_start) in free_points and (x_goal, y_goal) in free_points):
                break
            else:
                print("Please enter the points which are in free space and right orientation!")
                continue
        except:
            print("Dimensions more than the given map, try again!")



    # start_points = ()
    # goal_points = ()
    # RPM = ()
    # clearance = ()
    # image, image_bw = map.map()
    # free_points = map.free_points(image_bw)


if __name__ == '__main__':
    main()
