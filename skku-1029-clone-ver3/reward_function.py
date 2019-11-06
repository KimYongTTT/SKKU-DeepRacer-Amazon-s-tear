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
    if distance_from_center >= 0.0 and distance_from_center <= 0.03:
        reward = 1.0

    # 차량의 주행속도가 기준보다 낮을 시, 리워드 감소
    SPEED_THRESHOLD = 3.0
    if speed < SPEED_THRESHOLD:
        reward *= 0.5
    elif speed >= SPEED_THRESHOLD  and speed <= SPEED_THRESHOLD*2:
        reward += speed
    else:
        reward *= speed*speed

    
        
    return float(reward)
