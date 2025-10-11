#%%
import numpy as np

def exponential_rand(mu: float) -> float:
    return np.random.exponential(mu, size=1)[0]

def uniform_rand(a: float, b: float) -> float:
    return np.random.uniform(a, b, size=1)[0]

def simulation():
    queue = [] # 受付時刻が入る
    waiting_times = [] # 待ち時間が入る
    elapsed_minutes = 0
    while elapsed_minutes < (16-9)*60: # 9時から16時まで
        elapsed_minutes += exponential_rand(10) # 指数分布に従って患者が来る
        queue.append(elapsed_minutes)
    elapsed_minutes = queue[0] # 時間を最初の人の受付時間に巻き戻す
    #print(elapsed_minutes, queue)
    while len(queue) > 0:
        waiting_time = max(elapsed_minutes - queue.pop(0), 0) # 最初の待ち時間は0分になるはず
        assert waiting_time >= 0
        waiting_times.append(waiting_time)
        consult_time = uniform_rand(5, 20) # 5分から20分
        elapsed_minutes = max(elapsed_minutes + consult_time, 
                              (queue[0] if len(queue) > 0 else 0))

    return len(waiting_times), np.count_nonzero(waiting_times, axis=0), np.mean(waiting_times), elapsed_minutes

#%%

num_patients, num_wait_patients, mean_waiting_times, total_consult_times = [],[],[],[]
for _ in range(100):
    result = simulation()
    num_patients.append(result[0])
    num_wait_patients.append(result[1])
    mean_waiting_times.append(result[2])
    total_consult_times.append(result[3])
print(num_patients[0], num_wait_patients[0], mean_waiting_times[0], total_consult_times[0])
#%%
import pandas as pd
print(
    np.median(num_patients),
    np.median(num_wait_patients),
    np.median(mean_waiting_times),
    np.median(total_consult_times)
)
df = pd.DataFrame({
    "num_patients": num_patients,
    "num_wait_patients": num_wait_patients,
    "mean_waiting_times": mean_waiting_times,
    "total_consult_times": total_consult_times
})
print(df.describe())
# %%
