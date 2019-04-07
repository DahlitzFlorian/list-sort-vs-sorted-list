import threading


class StoppableThread(threading.Thread):
    def __init__(self):
        super(StoppableThread, self).__init__()
        self.daemon = True
        self.__monitor = threading.Event()
        self.__monitor.set()
        self.__has_shutdown = False

    def run(self):
        """Overloads the threading.Thread.run"""
        # Call the User's Startup functions
        self.startup()

        # Loop until the thread is stopped
        while self.isRunning():
            self.mainloop()

        # Clean up
        self.cleanup()

        # Flag to the outside world that the thread has exited
        # AND that the cleanup is complete
        self.__has_shutdown = True

    def stop(self):
        self.__monitor.clear()

    def isRunning(self):
        return self.__monitor.isSet()

    def isShutdown(self):
        return self.__has_shutdown

    ###############################
    ### User Defined Functions ####
    ###############################

    def mainloop(self):
        """
        Expected to be overwritten in a subclass!!
        Note that Stoppable while(1) is handled in the built in "run".
        """
        pass

    def startup(self):
        """Expected to be overwritten in a subclass!!"""
        pass

    def cleanup(self):
        """Expected to be overwritten in a subclass!!"""
        pass
