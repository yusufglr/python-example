
from PyQt5.QtWidgets import *
import sys
import os

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Checkbox Example")

        # QHBoxLayout is a horizontally stacking layout with new widgets
        # added to the right of previous widgets.
        layout = QVBoxLayout()
        layout2 = QHBoxLayout()

        checkbox = {}
        checkbox2 = []
        checkboxControl = {"resolvconf":True,"crda":True,"ufw":False,"sysvinit":True}
        print(os.listdir("/lib"))
        for dir in os.listdir("/lib"):
            checkbox[dir] = QCheckBox(dir)
            if dir in checkboxControl:
                checkbox[dir].setChecked(checkboxControl[dir])
            # SIGNAL: The .pressed signal fires whenever the button is pressed.
            # We connect this to self.my_custom_fn via a lambda to pass in
            # additional data.
            # IMPORTANT: You must pass the additional data in as a named
            # parameter on the lambda to create a new namespace. Otherwise
            # the value of n will be bound to the final value in the parent
            # for loop (always 9).

            checkbox[dir].clicked.connect(lambda: self.my_custom_fn(checkbox[dir]))

            # Add the button to the layout. It will go to the right by default.
            layout.addWidget(checkbox[dir])

        for n in range(10):
            # Create a push button labeled with the loop number 0-9
            checkbox2.append(QCheckBox(str(n)))
            # SIGNAL: The .pressed signal fires whenever the button is pressed.
            # We connect this to self.my_custom_fn via a lambda to pass in
            # additional data.
            # IMPORTANT: You must pass the additional data in as a named
            # parameter on the lambda to create a new namespace. Otherwise
            # the value of n will be bound to the final value in the parent
            # for loop (always 9).
            checkbox2[n].clicked.connect(lambda n=n: self.my_custom_fn(checkbox2[n]))

            # Add the button to the layout. It will go to the right by default.
            layout2.addWidget(checkbox2[n])

        # Create a empty widget to hold the layout containing our buttons.
        widget = QWidget()

        # Set the layout containing our buttons onto the blank widget. We only
        # need to do this here because we can't set a layout on a QMainWindow.
        # So instead we're setting a layout on a widget, and then adding that
        # widget to the window(!)
        layout.addLayout(layout2)
        widget.setLayout(layout)

        self.setCentralWidget(widget)


    # SLOT: This function will receive the single value passed from the signal
    def my_custom_fn(self, a):
        print(self.sender().text())
        print(self.sender().isChecked())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()