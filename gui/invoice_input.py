from PyQt5.QtWidgets import *
import sys


class Inputable():
    def __init__(self, name=None):
        self.hbox = QHBoxLayout() 
        self.label = QLabel(name)
        self.obj = QLineEdit()

    def add_row(self, layout):
        layout.addRow(self.label, self.obj)

class Window(QDialog):
    mandatory_input = [
        "Invoice Number",
        "Date",
        "Challan",
        "Dated",
        "Buyer",
        "Buyer Address",
        "Buyer GSTIN"
    ]
    input_columns = [
        "Description", 
        "HSN/SAC", 
        "GST%",
        "Qty",
        "Rate",
        "Amt"]

    input_field_reference = dict()

    number_items = 10

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Invoice Generator v0.1")
        self.setGeometry(100, 100, 1000, 400)
        self.formGroupBox = QGroupBox("Invoice")
        self.createForm()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.getInfo)
        self.buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

    def getInfo(self):
        for i in self.input_field_reference.keys():
            print("{0} = {1}".format(i, self.input_field_reference[i].text()))
        print("Input taken care of")
        # self.close()

    def createForm(self):
        vbox = QVBoxLayout()
        layout = QFormLayout()
        layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        for i in self.mandatory_input:
            self.input_field_reference[i] = QLineEdit()
            layout.addRow(i, self.input_field_reference[i])
        
        vbox.addLayout(layout)
        num_inputs = 10
        grid = QGridLayout()
        for (index, label) in enumerate(self.input_columns):
            grid.addWidget(QLabel(label), 0, index)
            for i in range(1, self.number_items):
                self.input_field_reference[label + str(i)] = QLineEdit()
                grid.addWidget(self.input_field_reference[label + str(i)], i, index)

        vbox.addLayout(grid)
        self.formGroupBox.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())