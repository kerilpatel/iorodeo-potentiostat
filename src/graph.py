import matplotlib.pyplot as plt

def showgraph():

    potential = [10, 12, 17, 26, 50]
    time = [2, 4, 6, 8, 10]

    fig, axs = plt.subplots()

    axs.plot(potential, time)
    axs.set(xlabel = 'time', ylabel = 'potential')
    axs.grid()
    plt.show()
