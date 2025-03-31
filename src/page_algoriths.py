class PageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.frames = []

    def fifo(self, pages):
        """ First In First Out (FIFO) Page Replacement Algorithm """
        page_faults = 0
        self.frames = []

        for page in pages:
            if page not in self.frames:
                if len(self.frames) < self.capacity:
                    self.frames.append(page)
                else:
                    self.frames.pop(0)
                    self.frames.append(page)
                page_faults += 1
            print(f"Page: {page} | Frames: {self.frames}")

        return page_faults
    
    def lru(self, pages):
        """ Least Recently Used (LRU) Page Replacement Algorithm """
        page_faults = 0
        self.frames = []
        
        for page in pages:
            if page in self.frames:
                self.frames.remove(page)
            elif len(self.frames) >= self.capacity:
                self.frames.pop(0)
                page_faults += 1
            else:
                page_faults += 1
            self.frames.append(page)
            print(f"Page: {page} | Frames: {self.frames}")
            
        return page_faults
    
    def optimal(self, reference_string):
        memory = []
        page_faults = 0
        steps = []

        for i, page in enumerate(reference_string):
            if page not in memory:
                if len(memory) < self.capacity:
                    memory.append(page)
                else:
                    future_uses = [reference_string[i:].index(p) if p in reference_string[i:] else float("inf") for p in memory]
                    memory.pop(future_uses.index(max(future_uses)))
                    memory.append(page)
                page_faults += 1
            steps.append(list(memory))  # Store steps for visualization

        return page_faults, steps