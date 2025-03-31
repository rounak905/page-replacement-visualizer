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