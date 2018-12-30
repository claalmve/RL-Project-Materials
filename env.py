import gym
import time
env = gym.make('DoubleDunk-ram-v0')
env.reset()
env.render()
time.sleep(10)
