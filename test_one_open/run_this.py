from envir import Maze
from RL_brain import QLearningTable
import threading
import time
import matplotlib.pyplot as plt
import envir as en
import ble_rf as br
import numpy as np
##import pymongo
import pandas as pd
##connection = pymongo.MongoClient("localhost",27017)
##tdb = connection.RL_data1
##post_info = tdb.test


##fig = plt.figure()
##ax = fig.add_subplot(1,1,1)
def update():
##    episode_count = 0
##    episode_next = 0
##    episode_past = 0
##    count_lt = 0
    mid = env._build_maze()
    print(mid)
    for A in range(6):
        print(A)
        if mid[A] == 0.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            for episode in range(1000):
                        # initial observation
                observation = env.reset()
                while True:
                            # fresh env
                    env.render()

                            # RL choose action based on observation
                    action = RL.choose_action(str(observation))
                    RL.lt.append(action)
            ##            print(RL.lt)
                            # RL take action and get next observation and reward
                    observation_, reward, done = env.step(action)

                            # RL learn from this transition
                    table = RL.learn(str(observation), action, reward, str(observation_))
                        
                            # swap observation
                    observation = observation_

                            #count episode
                    episode_next = episode
                    episode_count += 1

                            # break while loop when end of this episode
                    if reward == 1:
                        plt.subplot(231)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='red',lw=1.5)
##        ##                ax.plot([episode_next,episode_past],[episode_count,count_lt],color='red',lw=1.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
##                        plt.xticks([7,40])
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
            ##                RL.counter += 1
            ##                print(len(RL.lt))
                        while RL.i == 1:
                            episode_low = count_lt
            ##                    print('A')
                            RL.i = 2
                                # min path
                        if episode_low >= count_lt:
                                # convergence
                            if episode_low == count_lt:
                                RL.counter += 1
                            episode_low = len(RL.lt)
                                
                        if RL.counter >= 10:
                            break
                    if done:
                        if RL.counter >= 10:
                            break
                        del RL.lt[:]
                        break
                if RL.counter >= 10:
                    print('learning is over1')
                    print(RL.lt)
                    table.to_csv('data.csv')                 
                    # mongoDB
        ##            local_data = np.genfromtxt("data1.csv",skip_header = 1,dtype = None)
        ##            local_name = ["up","down","right","left"]
        ##            local_json = []
        ##            for data in local_data:
        ##                local_list = zip(local_name,data)
        ##                local_json.append(dict(local_list))
        ##            print(local_json)
        ##            post_info.insert(local_json)
                    break

        if mid[A] == 1.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            for episode in range(1000):
                # initial observation
                observation = env.reset1()
                while True:
                    # fresh env
                    env.render()

                    # RL choose action based on observation
                    action = RL1.choose_action(str(observation))
                    RL1.lt1.append(action)
                    # RL take action and get next observation and reward
                    observation_, reward, done  = env.step1(action)


                    # RL learn from this transition
                    table1 = RL1.learn(str(observation), action, reward, str(observation_))

                    # swap observation
                    observation = observation_

                    #count episode
                    episode_next = episode
                    episode_count += 1

                    # break while loop when end of this episode
                    if reward == 1:
                        plt.subplot(232)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='blue',lw=1.5)
##    ##                    ax.plot([episode_next,episode_past],[episode_count,count_lt],color='blue',lw=1.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
##                        plt.xticks([13,50])
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
    ##                    print(len(RL.lt1))
                        while RL1.i == 1:
                            episode_low1 = count_lt
    ##                        print('B')
                            RL1.i = 2
                        if episode_low1 >= count_lt:
                            if episode_low1 == count_lt:
                                RL1.counter1 += 1
                            episode_low1 = len(RL.lt1)
                        if RL1.counter1 >= 10:
                            break
                    if done:
                        if RL1.counter1 >= 10:
                            break
                        del RL1.lt1[:]
                        break
                if RL1.counter1 >= 10:
                    print('learning is over2')
                    print(RL1.lt1)
                    table1.to_csv('data1.csv')
                    break
        if mid[A] == 2.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            for episode in range(1000):
                    # initial observation
                observation = env.reset2()
                while True:
                        # fresh env
                    env.render()

                        # RL choose action based on observation
                    action = RL2.choose_action(str(observation))
                        
                    RL2.lt2.append(action)
                        # RL take action and get next observation and reward
                    observation_, reward, done = env.step2(action)

                        # RL learn from this transition
                    table2 = RL2.learn(str(observation), action, reward, str(observation_))

                        # swap observation
                    observation = observation_
                        #count episode
                    episode_next = episode
                    episode_count += 1

                        # break while loop when end of this episode
                    if reward == 1:
                        plt.subplot(233)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='pink',lw=2.5)
##    ##                    ax.plot([episode_next,episode_past],[episode_count,count_lt],color='pink',lw=2.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
##                        plt.xticks([11,45])
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
    ##                    print(len(RL.lt2))
                        while RL2.i == 1:
                            episode_low2 = count_lt
    ##                        print('C')
                            RL2.i = 2
                        if episode_low2 >= count_lt:
                            if episode_low2 == count_lt:
                                RL2.counter2 += 1
                            episode_low2 = len(RL.lt2)
                        if RL2.counter2 >= 10:
                            break
                    if done:
                        if RL2.counter2 >= 10:
                            break
                        del RL2.lt2[:]
                        break
                if RL2.counter2 >= 10:
                    print('learning is over3')
                    print(RL2.lt2)
                    table2.to_csv('data2.csv')
                    break
        if mid[A] == 3.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            for episode in range(1000):
                    # initial observation
                observation = env.reset3()
                while True:
                        # fresh env
                    env.render()

                        # RL choose action based on observation
                    action = RL3.choose_action(str(observation))
                        
                    RL3.lt3.append(action)
                        # RL take action and get next observation and reward
                    observation_, reward, done = env.step3(action)

                        # RL learn from this transition
                    table3 = RL3.learn(str(observation), action, reward, str(observation_))

                        # swap observation
                    observation = observation_
                        #count episode
                    episode_next = episode
                    episode_count += 1

                        # break while loop when end of this episode
                    if reward == 1:
                        plt.subplot(234)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='green',lw=2.5)
##    ##                    ax.plot([episode_next,episode_past],[episode_count,count_lt],color='green',lw=2.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
##                        plt.xticks([7,45])
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
    ##                    print(len(RL.lt3))
                        while RL3.i == 1:
                            episode_low3 = count_lt
    ##                        print('D')
                            RL3.i = 2
                        if episode_low3 >= count_lt:
                            if episode_low3 == count_lt:
                                RL3.counter3 += 1
                            episode_low3 = len(RL.lt3)
                        if RL3.counter3 >= 10:
                            break
                    if done:
                        if RL3.counter3 >= 10:
                            break
                        del RL3.lt3[:]
                        break
                if RL3.counter3 >= 10:
                    print('learning is over4')
                    print(RL3.lt3)
                    table3.to_csv('data3.csv')
                    break
        if mid[A] == 4.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            for episode in range(1000):
                    # initial observation
                observation = env.reset4()
                while True:
                        # fresh env
                    env.render()

                        # RL choose action based on observation
                    action = RL4.choose_action(str(observation))
                        
                    RL4.lt4.append(action)
                        # RL take action and get next observation and reward
                    observation_, reward, done = env.step4(action)

                        # RL learn from this transition
                    table4 = RL4.learn(str(observation), action, reward, str(observation_))

                        # swap observation
                    observation = observation_
                    #count episode
                    episode_next = episode
                    episode_count += 1

                        # break while loop when end of this episode
                    if reward == 1:
                        plt.subplot(235)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='purple',lw=2.5)
##    ##                    ax.plot([episode_next,episode_past],[episode_count,count_lt],color='purple',lw=2.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
##                        plt.xticks([28,70])
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
    ##                    print(len(RL.lt4))
                        while RL4.i == 1:
                            episode_low4 = count_lt
    ##                        print('E')
                            RL4.i = 2
                        if episode_low4 >= count_lt:
                            if episode_low4 == count_lt:
                                RL4.counter4 += 1
                            episode_low4 = len(RL.lt4)
                        if RL4.counter4 >= 10:
                            break
                    if done:
                        if RL4.counter4 >= 10:
                            break
                        del RL4.lt4[:]
                        break
                if RL4.counter4 >= 10:
                    print('learning is over5')
                    print(RL4.lt4)
                    table4.to_csv('data4.csv')
                    break
        if mid[A] == 5.0:
            episode_count = 0
            episode_next = 0
            episode_past = 0
            count_lt = 0
            for episode in range(1000):
                    # initial observation
                observation = env.reset5()
                while True:
                        # fresh env
                    env.render()

                        # RL choose action based on observation
                    action = RL5.choose_action(str(observation))
                        
                    RL5.lt5.append(action)
                        # RL take action and get next observation and reward
                    observation_, reward, done = env.step5(action)

                        # RL learn from this transition
                    table5 = RL5.learn(str(observation), action, reward, str(observation_))

                        # swap observation
                    observation = observation_

                    #count episode
                    episode_next = episode
                    episode_count += 1

                        # break while loop when end of this episode
                    if reward == 1:
                        plt.subplot(236)
##                        plt.plot([episode_next,episode_past],[episode_count,count_lt],color='orange',lw=2.5)
##    ##                    ax.plot([episode_next,episode_past],[episode_count,count_lt],color='orange',lw=2.5)
##                        plt.xlabel('episode')
##                        plt.ylabel('step')
##                        plt.xticks([19,50])
                        episode_past = episode_next
                        count_lt = episode_count
                        episode_count = 0
    ##                    print(len(RL.lt5))
                        while RL5.i == 1:
                            episode_low5 = count_lt
    ##                        print('F')
                            RL5.i = 2
                        if episode_low5 >= count_lt:
                            if episode_low5 == count_lt:
                                RL5.counter5 += 1
                            episode_low5 = len(RL.lt5)
                        if RL5.counter5 >= 10:
                            break
                    if done:
                        if RL5.counter5 >= 10:
                            break
                        del RL5.lt5[:]
                        break
                if RL5.counter5 >= 10:
                    print('learning is over6')
                    print(RL5.lt5)
                    table5.to_csv('data5.csv')
                    break
            
    # end of game
    print('game over')
##    RL.status == 6
##    if RL.status == 6:
##        rfcomm_0 = threading.Thread(target=br.rfcomm0_d,args = (RL.lt))
##        rfcomm_1 = threading.Thread(target=br.rfcomm1_d,args = (RL1,lt1))
##        rfcomm_2 = threading.Thread(target=br.rfcomm2_d,args = (RL2.lt2))
##        rfcomm_3 = threading.Thread(target=br.rfcomm3_d,args = (RL3.lt3))
##        rfcomm_4 = threading.Thread(target=br.rfcomm4_d,args = (RL4,lt4))
##        rfcomm_5 = threading.Thread(target=br.rfcomm5_d,args = (RL5,lt5))
##        br.rfcomm0_d(RL.lt)
    plt.show()
if __name__ == "__main__":

##    lock = threading.Lock()
##    rfcomm_0 = threading.Thread(target=br.rfcomm0_d)
##    rfcomm_1 = threading.Thread(target=br.rfcomm1_d)
##    rfcomm_2 = threading.Thread(target=br.rfcomm2_d)
##    rfcomm_3 = threading.Thread(target=br.rfcomm3_d)
##    rfcomm_4 = threading.Thread(target=br.rfcomm4_d)
##    rfcomm_5 = threading.Thread(target=br.rfcomm5_d)
    ##a = int(input('input_motor_status:'))
##    s_t = time.time()
##    en.rfcomm0()
##    en.rfcomm1()
##    en.rfcomm2()
##    en.rfcomm3()
##    en.rfcomm4()
##    en.rfcomm5()
##    rfcomm_0.start()
##    rfcomm_1.start()
##    rfcomm_2.start()
##    rfcomm_3.start()
##    rfcomm_4.start()
##    rfcomm_5.start(
##    rfcomm_0.join()
##    rfcomm_1.join()
 ##    rfcomm_2.join()
##    rfcomm_3.join()
##    rfcomm_4.join()
##    rfcomm_5.join()
##    print('time :',time.time() - s_t)
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    RL1 = QLearningTable(actions=list(range(env.n_actions)))
    RL2 = QLearningTable(actions=list(range(env.n_actions)))
    RL3 = QLearningTable(actions=list(range(env.n_actions)))
    RL4 = QLearningTable(actions=list(range(env.n_actions)))
    RL5 = QLearningTable(actions=list(range(env.n_actions)))
    #Thread_1 = threading.Thread(target = updeee)
    #env.mainloop()
    #env.after(100, update)
    #env.after(100, update1)
    #Thread_0.start()
    #Thread_1.start()
    #env.mainloop()
    #Thread_0.join()
    #Thread_1.join()
    env.after(100, update)
    env.mainloop()
##    if RL.status == 6:
##        rfcomm0_d(RL.lt)
##        rfcomm1_d(RL1.lt1)
##        rfcomm2_d(RL2.lt2)
##        rfcomm3_d(RL3.lt3)
##        rfcomm4_d(RL4.lt4)
##        rfcomm5_d(RL5.lt5)
