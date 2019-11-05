import math
def reward_function(params):
    reward = 1e-3
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    x = params['x']
    y = params['y']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    steps = params['steps']
    track_width = params['track_width']
    steering = params['steering_angle']
    speed = params['speed']
    progress = params['progress']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    # 트랙 중앙라인으로부터의 거리 기준
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    if not all_wheels_on_track: # 트랙을 이탈할 경우
        reward = reward-1
    else:
        reward += progress
    
    # 트랙 중앙에 가까울 수록 높은 리워드
    if distance_from_center <= marker_1:
        reward = reward
    elif distance_from_center <= marker_2:
        reward *= 0.7
    elif distance_from_center <= marker_3:
        reward *= 0.3
    else:
        reward = 1.0
    
    # 차량의 주행속도가 기준보다 낮을 시, 리워드 감소
    SPEED_THRESHOLD = 5
    if speed < SPEED_THRESHOLD:
        reward *= 0.5

    # 차량이 적은 스텝으로 높은 주행률을 달성할수록 높은 리워드, 속도가 빠를수록 더 큰 리워드    
    if all_wheels_on_track and steps > 0:
        reward += ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward *= 0.3
    
    
    # 트랙의 웨이포인트 정보
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    
    # 차량의 주행 방향이, 다음 웨이포인트를 향하고 있는가를 고려하는 부분
    track_direction = math.atan2(next_point[1]-prev_point[1],next_point[0]-prev_point[0])
    track_direction = math.degrees(track_direction)
    
    direction_diff = abs(track_direction-heading)
    DIRECTION_THRESHOLD = 15.0
    if direction_diff > DIRECTION_THRESHOLD :
        reward *= 0.5
        
    return float(reward)
