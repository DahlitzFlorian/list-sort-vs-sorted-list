from stoppable_thread import StoppableThread


class FunctionSniffingClass(StoppableThread):
    def __init__(self, target_function, arr):
        super(FunctionSniffingClass, self).__init__()
        self.target_function = target_function
        self.arr = arr
        self.results = None

    def startup(self):
        # Overload the startup function
        print("Calling the Target Function...")

    def cleanup(self):
        # Overload the cleanup function
        print("Function Call Complete")

    def mainloop(self):
        # Start the function Call
        self.results = self.target_function(self.arr)

        # Kill the thread when complete
        self.stop()
