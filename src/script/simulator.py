from main import *

v = np.arange(1,4+0.5,0.5)
phi = np.arange(0,2*np.pi,0.25*np.pi)
T = ["Formal_Table","Ellipse_Table","Table_O1","Table_O2"]

# for t in ["Formal_Table","Ellipse_Table"]:
#     print("=== {} ===".format(t))
#     res = []
#     for vi in v:
#         temp = []
#         for pi in phi:
#             temp.append(do_simulation(pi,vi,t))
#         res.append(temp)

#     file = open("simulation_result_{}.txt".format(t),"w")
#     file.write(str(res))
#     file.close()

#     np.save("simulation_result_{}".format(t),np.array(res))
#     print("=================\n")

for t in T:
    data = np.load("simulation_result_{}.npy".format(t))
    plt.xlabel("V (cue stick)")
    plt.ylabel("# collision")
    plt.ylim(0,20)
    plt.plot(v,data,"ko")
    m_data = []
    for i in np.arange(0,len(v)):
        m_data.append(np.mean(data[i,np.where(data[i,:]<1000)]))

    plt.plot(v,m_data)
    plt.draw();plt.savefig("result_{}.png".format(t))
    plt.clf()

print("program terminated.")