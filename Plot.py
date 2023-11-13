import matplotlib.pyplot as plt
timetaken, accuracies=[], []
with open("analysis.txt", 'r') as branchfile:
        line=branchfile.readline()
        accuracies = list(map(float, line.split(',')))
        line=branchfile.readline()
        timetaken = list(map(float, line.split(',')))
figure, axis = plt.subplots(2, constrained_layout = True)
figure.suptitle("Analysis on the Perceptron")
axis[0].plot(range(1, 50), accuracies)
axis[0].set_title('Accuracy vs. History Length')
axis[0].set(xlabel='History Length', ylabel='Accuracy')


axis[1].plot(range(1, 50), timetaken)
axis[1].set_title('Time Taken vs. History Length')
axis[1].set(xlabel='History Length', ylabel='Time Taken in sec')
plt.grid(True)
plt.show()
