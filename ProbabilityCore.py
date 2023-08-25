import numpy as np

prob_win = 0.6
prob_loss = 0.4
win_reward = 50
max_loss = 50

raw_randoms = np.random.rand(1000)
moves = ((5 - (raw_randoms*10)) + 100.0)/100.0

wins = np.where(raw_randoms < 0.4, -50, 50)

print(np.product(moves.prod()))