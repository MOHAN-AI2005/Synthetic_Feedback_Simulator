import numpy as np

def generate_trajectory(length=5):
    return np.random.rand(length)

def compare_trajectories(traj1, traj2, noise=0.1):
    score1 = np.sum(traj1)
    score2 = np.sum(traj2)
    true_preference = 0 if score1 > score2 else 1
    if np.random.rand() < noise:
        return 1 - true_preference
    return true_preference

for i in range(10):
    t1 = generate_trajectory()
    t2 = generate_trajectory()
    preference = compare_trajectories(t1, t2)
    print(f"Comparison {i+1}: Preferred Trajectory - {preference}")
