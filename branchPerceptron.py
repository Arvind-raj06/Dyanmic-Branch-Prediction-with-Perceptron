import os
import tkinter as tk
from tkinter import filedialog, Text
import time
import sys
from collections import deque

class Perceptron:
    weights = []
    N = 0
    bias = 0
    threshold = 0

    def __init__(self, N):
        self.N = N
        self.bias = 0
        self.threshold = 2 * N + 14  # optimal threshold depends on history length
        self.weights = [0] * N

    def predict(self, global_branch_history):
        running_sum = self.bias
        for i in range(0, self.N):  # dot product of branch history with the weights
            running_sum += global_branch_history[i] * self.weights[i]
        prediction = -1 if running_sum < 0 else 1
        return (prediction, running_sum)

    def update(self, prediction, actual, global_branch_history, running_sum):
        if (prediction != actual) or (abs(running_sum) < self.threshold):
            self.bias = self.bias + (1 * actual)
            for i in range(0, self.N):
                self.weights[i] = self.weights[i] + (actual * global_branch_history[i])

def perceptron_pred(trace, l=1, tablesize=None):
    global_branch_history = deque([])
    global_branch_history.extend([0] * l)

    p_list = {}
    num_correct = 0

    for br in trace:  # iterating through each branch
        if tablesize:
            index = hash(br[0]) % tablesize
        else:
            index = hash(br[0])

        if index not in p_list:  # if no previous branch from this memory location
            p_list[index] = Perceptron(l)
        results = p_list[index].predict(global_branch_history)
        pr = results[0]
        running_sum = results[1]
        actual_value = 1 if br[1] else -1
        p_list[index].update(pr, actual_value, global_branch_history, running_sum)
        global_branch_history.appendleft(actual_value)
        global_branch_history.pop()
        if pr == actual_value:
            num_correct += 1
    return num_correct, len(p_list)

def getTableSize(ratio, k):
    return int(ratio * k)

def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    file_path.delete(0, tk.END)
    file_path.insert(0, file)

def run_perceptron():
    file_in = file_path.get()
    if not os.path.exists(file_in):
        result_text.insert(tk.END, "ERROR: The input file does not exist.\n")
        return

    with open(file_in, 'r') as branchfile:
        trace = []
        for line in branchfile.readlines():
            tok = line.split(' ')
            trace.append([tok[0], int(tok[1])])

    num_correct, num_p = perceptron_pred(trace, 5)

    result_text.insert(tk.END, f'Length of Perceptrons list: {num_p}\n')

    results = []
    accuracies = []
    timetaken = []
    for i in range(1, 50):
        start_time = time.time()
        num_correct, num_p = perceptron_pred(trace, i)
        end_time = time.time()
        accuracy = num_correct / float(len(trace))
        accuracies.append(str(accuracy))
        timetaken.append(str(end_time-start_time))
        results.append((accuracy, end_time - start_time))
        result_text.insert(tk.END, f'i:{i} -->\n{results[-1]}\n')


    accuracy_text.insert(tk.END, f'Accuracy: {num_correct / float(len(trace)) * 100}%\n')
    f = open("analysis.txt", "w")
    f.write(",".join(accuracies)+"\n"+','.join(timetaken))
    f.close()


root = tk.Tk()
root.title("Perceptron Branch Predictor")

frame = tk.Frame(root)
frame.pack(pady=10)

file_path_label = tk.Label(frame, text="Trace File:")
file_path_label.grid(row=0, column=0, padx=10)

file_path = tk.Entry(frame, width=50)
file_path.grid(row=0, column=1, padx=10)

browse_button = tk.Button(frame, text="Browse", command=open_file)
browse_button.grid(row=0, column=2, padx=10)

run_button = tk.Button(frame, text="Run Perceptron", command=run_perceptron)
run_button.grid(row=1, column=1, padx=10)

result_text = Text(root, height=15, width=50)
result_text.pack(pady=10)

accuracy_text = Text(root, height=1, width=50)
accuracy_text.pack(pady=5)

root.mainloop()
