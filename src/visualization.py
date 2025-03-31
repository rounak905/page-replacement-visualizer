import matplotlib.pyplot as plt

def plot_page_replacement(steps):
    fig, ax = plt.subplots()
    ax.imshow(steps, cmap="Blues", aspect="auto")
    ax.set_xlabel("Step")
    ax.set_ylabel("Page Frame State")
    plt.show()