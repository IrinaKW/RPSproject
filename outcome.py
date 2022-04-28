# %%
def outcome(player, computer):
    r="ROCK"
    p="PAPER"
    s="SCISSORS"

    if player==computer:
        return('try')
    elif (player==r and computer==p) or (player==p and computer==s) or (player==s and computer==r):
        return('c')
    else:
        return('p')

# %%