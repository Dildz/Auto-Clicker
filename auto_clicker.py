# Depencency imports
import ctypes
from pynput import mouse
import time
import threading


# This script will start clicking when mouse button 5 is pressed and stop clicking when mouse button 4 is pressed.
class AutoClicker:
    # Initialize the clicking variable to False
    def __init__(self):
        self.clicking = False

    # This function will use ctypes to click the mouse rapidly
    def auto_clicker(self):
        while self.clicking:
            self.click_mouse()
            print("Clicking!")
            time.sleep(0.05)

    # Use ctypes to generate mouse clicks
    def click_mouse(self):
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # Mouse down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # Mouse up

    # This function will be called when a mouse button is pressed
    def on_click(self, x, y, button, pressed):

        # If mouse button 5 (x2) is pressed then start clicking
        if button == mouse.Button.x2 and pressed:
            print("Mouse button 5 (x2) pressed, starting auto clicker!")
            if not self.clicking:
                self.clicking = True
                # Start the auto-clicker on a new thread
                threading.Thread(target=self.auto_clicker).start()
                
        # If mouse button 4 (x1) is pressed then stop clicking
        elif button == mouse.Button.x1 and pressed:
            print("Mouse button 4 (x1) pressed, stopping auto clicker!")
            self.clicking = False

# Start the script
if __name__ == '__main__':
    print("========================================")
    print("=           AutoClicker v1.0           =")
    print("========================================")
    print("\nInstructions for using AutoClicker:")
    print("Press mouse button 5 to start auto-clicking.")
    print("Press mouse button 4 to stop auto-clicking.")
    print("To stop the script, close this terminal window.")
    print("----------------------------------------\n")
    
    autoclicker = AutoClicker()
    with mouse.Listener(on_click=autoclicker.on_click) as listener:
        listener.join()
