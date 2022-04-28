# %%
import time
def countdown(timer=5):
    print("Ready, Set, GO")
    for i in range(timer):
        print (f"0{timer-i}", end="\r")
        time.sleep(1)


# %%
