# Dyanmic Branch Prediction with Perceptron

Prerequisites:
Ensure you have Python installed on your system. You can download it from Python's official website preferrable 3.7 or greater version of python compiler.

Steps:
1. Download the Code

2. Open a terminal or command prompt.
    Navigate to the directory where you saved the Python file.
    Run the script using the command: python branchPerceptron.py
    Alternatively, you can run the script directly from your IDE.

3. GUI Interaction:
    The script will launch a GUI window. Click the "Browse" button to select a trace file (a text file with branch history information). After selecting the file,
    click the "Run Perceptron" button. The results will be displayed in the GUI window, including the length of the perceptron list and accuracy for different history lengths.

4. Analysis Output:
    If successful, the accuracy values and time taken for different history lengths will be saved to "analysis.txt."

Perceptron Analysis Visualization Code:

Steps: 
1. Install the matplotlib library if not already installed:
    Open a terminal or command prompt, run "pip install matplotlib"

2. Open a terminal or command prompt.
    Navigate to the directory where you saved the Python file.
    Run the script using the command: python plot.py, ensure that "analysis.txt" is present in the same directory.


The script will generate two subplots visualizing accuracy vs. history length and time taken vs. history length using the data from "analysis.txt." 
The plots will be displayed, and the script will remain open until you close the plot window.
