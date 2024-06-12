參考老師的程式碼
#import gym
import gymnasium as gym

def choose_action(observation):
    pos, v, ang, rot = observation
    # 如果角度小於 0，向左移動以穩定竿子；如果角度大於 0，向右移動以穩定竿子
    if ang < 0:
        return 0  # 向左移動
    elif ang > 0:
        return 1  # 向右移動
    else:
        # 竿子幾乎垂直，根據速度的方向移動以保持平衡
        return 0 if v < 0 else 1

if __name__ == '__main__':
    env = gym.make('CartPole-v1')
    #env = gym.make('CartPole-v1', render_mode="human") # 改用這行會顯示動畫，但會變慢很多

    for i_episode in range(200):
        observation, info = env.reset() # reset environment to initial state for each episode
        rewards = 0 # accumulate rewards for each episode
        for t in range(250):
            env.render()

            action = choose_action(observation) # choose an action based on hand-made rule 
            observation, reward, terminated, truncated, info = env.step(action) # do the action, get the reward
            done = terminated or truncated
            rewards += reward

            if done:
                print('Episode finished after {} timesteps, total rewards {}'.format(t+1, rewards))
                break

    env.close() # need to close, or errors will be reported
