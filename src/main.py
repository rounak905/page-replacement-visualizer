import tkinter as tk
from page_algorithms import PageReplacement

def run_algorithm():
    """ Function to run the selected page replacement algorithm """
    pages = [int(x) for x in entry_pages.get().split()]
    capacity = int(entry_capacity.get())
    algorithm = algo_var.get()

    pr = PageReplacement(capacity)
    if algorithm == "FIFO":
        faults = pr.fifo(pages)
    else:
        faults = pr.lru(pages)

    result_label.config(text=f"Total Page Faults: {faults}")

# GUI Setup
root = tk.Tk()
root.title("Page Replacement Visualizer")
root.geometry("400x300")

# Page Input
tk.Label(root, text="Enter Pages (space-separated):").pack()
entry_pages = tk.Entry(root)
entry_pages.pack()

# Capacity Input
tk.Label(root, text="Enter Frame Capacity:").pack()
entry_capacity = tk.Entry(root)
entry_capacity.pack()

# Algorithm Selection
algo_var = tk.StringVar(value="FIFO")
tk.Radiobutton(root, text="FIFO", variable=algo_var, value="FIFO").pack()
tk.Radiobutton(root, text="LRU", variable=algo_var, value="LRU").pack()

# Run Button
btn_run = tk.Button(root, text="Run Algorithm", command=run_algorithm)
btn_run.pack()

# Result Display
result_label = tk.Label(root, text="Total Page Faults: ")
result_label.pack()

root.mainloop()
