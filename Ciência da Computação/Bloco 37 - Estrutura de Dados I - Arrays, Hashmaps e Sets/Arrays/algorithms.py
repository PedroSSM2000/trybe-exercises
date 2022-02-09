from random import randint
# In a software monitor, which checks the resiliency of other software, we need
# to know the maximum time that a software has remained unstable. To do this,
# every hour a request is made to the system and we check if it is ok. Assuming
# an array containing the states collected by our software, calculate the
# maximum time that the server remained unstable.
# 1 = stable, 0 = unstable
# Input: [1,1,1,1,0,0,1]
# Output: 4

def max_stable_time(array):
    max_time = 0
    current_time = 0
    for i in range(len(array)):
        if array[i] == 1:
            current_time += 1
        else:
            max_time = max(max_time, current_time)
            current_time = 0
    return max_time

# In a card game, the cards are represented by a numerical array. To start the
# game we must shuffle the cards. We will do this by splitting a portion of
# cards into 2 and then merging the two portions. For example: 

# Example 1:
# cards = [2, 6, 4, 5]
# cards per part = 2

# result = [2, 4, 6, 5].

# Example 2:
# cards = [1, 4, 4, 7, 6, 6]
# cards per part = 3

# score = [1, 7, 4, 6, 4, 6]

def shuffle_cards(cards):
    assert len(cards) > 0 and len(cards) % 2 == 0
    left = cards[:len(cards)//2]
    right = cards[len(cards)//2:]
    for i in range(len(right)//2):
        random_idxs = set()
        while len(random_idxs) < len(right)//2:
            random_idxs.add(randint(0, len(right)-1))
        for idx in random_idxs:
            right[idx], left[idx] = left[idx], right[idx]
    return left + right
