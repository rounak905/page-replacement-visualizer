class PageReplacement:
    def __init__(self, frame_size):
        self.frame_size = frame_size

    def fifo(self, reference_string):
        memory = []
        page_faults = 0
        steps = []

        for page in reference_string:
            if page not in memory:
                if len(memory) < self.frame_size:
                    memory.append(page)
                else:
                    memory.pop(0)
                    memory.append(page)
                page_faults += 1
            steps.append(list(memory))  # Store steps for visualization

        return page_faults, steps
