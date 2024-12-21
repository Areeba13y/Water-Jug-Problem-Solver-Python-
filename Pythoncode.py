import tkinter as tk
from tkinter import messagebox
from collections import deque
import matplotlib.pyplot as plt
# Function to check if goal state is reached
def is_goal_state(state, goal):
    return goal in state
# Function to generate possible next states
def get_next_states(state, capacities):
    jug1, jug2 = state
    max1, max2 = capacities
    states = []
    # Fill Jug 1
    states.append((max1, jug2))
    # Fill Jug 2
    states.append((jug1, max2))
    # Empty Jug 1
    states.append((0, jug2))
    # Empty Jug 2
    states.append((jug1, 0))
    # Pour Jug 1 -> Jug 2
    pour = min(jug1, max2 - jug2)
    states.append((jug1 - pour, jug2 + pour))
    # Pour Jug 2 -> Jug 1
    pour = min(jug2, max1 - jug1)
    states.append((jug1 + pour, jug2 - pour))
    return states
# BFS Implementation
def bfs(start, capacities, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        state, path = queue.popleft()
        if is_goal_state(state, goal):
            return path
        for next_state in get_next_states(state, capacities):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None
# DFS Implementation
def dfs(start, capacities, goal):
    stack = [(start, [start])]
    visited = set([start])
    while stack:
        state, path = stack.pop()
        if is_goal_state(state, goal):
            return path
        for next_state in get_next_states(state, capacities):
            if next_state not in visited:
                visited.add(next_state)
                stack.append((next_state, path + [next_state]))
    return None
# Function to plot the solution path
def plot_solution(path):
    jug1_levels = [state[0] for state in path]
    jug2_levels = [state[1] for state in path]
    steps = list(range(len(path)))
    plt.figure(figsize=(8, 6))
    plt.plot(steps, jug1_levels, label="Jug 1 Level (L)", marker='o', color='blue')
    plt.plot(steps, jug2_levels, label="Jug 2 Level (L)", marker='o', color='green')
    plt.xlabel("Steps")
    plt.ylabel("Water Level (L)")
    plt.title("Water Jug Problem Solution Path")
    plt.legend()
    plt.grid(True)
    plt.show()
# Function to handle the Solve button click
def solve():
    try:
        capacity1 = int(entry_jug1.get())
        capacity2 = int(entry_jug2.get())
        goal = int(entry_goal.get())
        method = var_method.get()
        if goal > max(capacity1, capacity2):
            messagebox.showerror("Error", "Goal volume cannot exceed jug capacities.")
            return
        start_state = (0, 0)
        capacities = (capacity1, capacity2)
        if method == "BFS":
            path = bfs(start_state, capacities, goal)
        elif method == "DFS":
            path = dfs(start_state, capacities, goal)
        else:
            messagebox.showerror("Error", "Please select a search method.")
            return

        if path:
            solution_text = "\n".join([f"Jug1: {state[0]}L, Jug2: {state[1]}L" for state in path])
            result_text.set("Solution Path:\n" + solution_text)
            plot_solution(path)  # Call the plotting function
        else:
            result_text.set("No solution found.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for jug capacities and goal volume.")
# Setting up the GUI
root = tk.Tk()
root.title("Water Jug Problem Solver")
# Input for Jug 1 Capacity
tk.Label(root, text="Jug 1 Capacity (L):").grid(row=0, column=0, padx=10, pady=5)
entry_jug1 = tk.Entry(root)
entry_jug1.grid(row=0, column=1, padx=10, pady=5)
# Input for Jug 2 Capacity
tk.Label(root, text="Jug 2 Capacity (L):").grid(row=1, column=0, padx=10, pady=5)
entry_jug2 = tk.Entry(root)
entry_jug2.grid(row=1, column=1, padx=10, pady=5)
# Input for Goal Volume
tk.Label(root, text="Goal Volume (L):").grid(row=2, column=0, padx=10, pady=5)
entry_goal = tk.Entry(root)
entry_goal.grid(row=2, column=1, padx=10, pady=5)
# Radio buttons for method selection
var_method = tk.StringVar(value="BFS")
tk.Label(root, text="Search Method:").grid(row=3, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="BFS", variable=var_method, value="BFS").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="DFS", variable=var_method, value="DFS").grid(row=3, column=1, sticky="e")
# Button to solve the problem
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=4, column=0, columnspan=2, pady=10)
# Result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
# Start the GUI event loop
root.mainloop()# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

