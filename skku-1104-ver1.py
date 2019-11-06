def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
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
    
    reward = 1e-3
    
    # Calculate 3 markers that are at varying distances away from the center line
    
    if not all_wheels_on_track: # 트랙을 이탈할 경우
        reward = reward/2
    else:
        reward = reward + progress
        
    
        
    if distance_from_center >= 0.0 and distance_from_center <= 0.03:
        reward += 1.0
        
    SPEED_THRESHOLD = 3.0
    if speed < SPEED_THRESHOLD:
        reward *= 0.5
    elif speed >= SPEED_THRESHOLD  and speed <= SPEED_THRESHOLD*2:
        reward += speed
    else:
        reward = reward
        
    return float(reward)
