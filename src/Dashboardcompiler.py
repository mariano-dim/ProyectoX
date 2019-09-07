#!/usr/bin/env python


from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
							 QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
							 QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
							 QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
							 QVBoxLayout, QWidget)

import sys


class WidgetGallery(QDialog):
	def __init__(self, parent=None):
		super(WidgetGallery, self).__init__(parent)

		self.originalPalette = QApplication.palette()

		styleComboBox = QComboBox()
		styleComboBox.addItems(QStyleFactory.keys())

		styleLabel = QLabel("E&stilo:")
		styleLabel.setBuddy(styleComboBox)

		self.useStylePaletteCheckBox = QCheckBox("&Usar estilos predeterminados")
		self.useStylePaletteCheckBox.setChecked(True)

		disableWidgetsCheckBox = QCheckBox("&Deshabilitar widgets")

		self.createTopLeftGroupBox()
		self.createTopRightGroupBox()
		self.createbottomRightTabWidget()
		self.createbottomLeftGroupBox()
		# self.createProgressBar()

		styleComboBox.activated[str].connect(self.changeStyle)
		self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
		disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
		disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
		disableWidgetsCheckBox.toggled.connect(self.bottomRightTabWidget.setDisabled)
		disableWidgetsCheckBox.toggled.connect(self.bottomLeftGroupBox.setDisabled)

		topLayout = QHBoxLayout()
		topLayout.addWidget(styleLabel)
		topLayout.addWidget(styleComboBox)
		topLayout.addStretch(1)
		topLayout.addWidget(self.useStylePaletteCheckBox)
		topLayout.addWidget(disableWidgetsCheckBox)

		mainLayout = QGridLayout()
		mainLayout.addLayout(topLayout, 0, 0, 1, 2)
		mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
		mainLayout.addWidget(self.topRightGroupBox, 1, 1)
		mainLayout.addWidget(self.bottomLeftGroupBox, 2, 0)
		mainLayout.addWidget(self.bottomRightTabWidget, 2, 1)
		# mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
		mainLayout.setRowStretch(1, 1)
		mainLayout.setRowStretch(2, 1)
		mainLayout.setColumnStretch(0, 1)
		mainLayout.setColumnStretch(1, 1)
		self.setLayout(mainLayout)

		self.setWindowTitle("Proyecto X")
		self.changeStyle('fusion')

	def changeStyle(self, styleName):
		QApplication.setStyle(QStyleFactory.create(styleName))
		self.changePalette()

	def changePalette(self):
		if self.useStylePaletteCheckBox.isChecked():
			QApplication.setPalette(QApplication.style().standardPalette())
		else:
			QApplication.setPalette(self.originalPalette)

	def advanceProgressBar(self):
		curVal = self.progressBar.value()
		maxVal = self.progressBar.maximum()
		self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

	def createTopLeftGroupBox(self):
		self.topLeftGroupBox = QGroupBox("Input")

		radioButton1 = QRadioButton("Radio button 1")
		radioButton2 = QRadioButton("Radio button 2")
		radioButton3 = QRadioButton("Radio button 3")
		radioButton1.setChecked(True)

		checkBox = QCheckBox("Tri-state check box")
		checkBox.setTristate(True)
		checkBox.setCheckState(Qt.PartiallyChecked)

		layout = QVBoxLayout()
		layout.addWidget(radioButton1)
		layout.addWidget(radioButton2)
		layout.addWidget(radioButton3)
		layout.addWidget(checkBox)
		layout.addStretch(1)
		self.topLeftGroupBox.setLayout(layout)

	def createTopRightGroupBox(self):
		self.topRightGroupBox = QGroupBox("Output")

		defaultPushButton = QPushButton("Default Push Button")
		defaultPushButton.setDefault(True)

		togglePushButton = QPushButton("Toggle Push Button")
		togglePushButton.setCheckable(True)
		togglePushButton.setChecked(True)

		# flatPushButton = QPushButton("Flat Push Button")
		# flatPushButton.setFlat(True)

		layout = QVBoxLayout()
		layout.addWidget(defaultPushButton)
		layout.addWidget(togglePushButton)
		# layout.addWidget(flatPushButton)
		layout.addStretch(1)
		self.topRightGroupBox.setLayout(layout)

	def createbottomRightTabWidget(self):
		self.bottomRightTabWidget = QTabWidget()
		self.bottomRightTabWidget.setSizePolicy(QSizePolicy.Preferred,
												QSizePolicy.Ignored)

		tab1 = QWidget()
		textEditTokensSourceCode = QTextEdit()

		textEditTokensSourceCode.setPlainText("salida")

		tab1hbox = QHBoxLayout()
		tab1hbox.setContentsMargins(5, 5, 5, 5)
		tab1hbox.addWidget(textEditTokensSourceCode)
		tab1.setLayout(tab1hbox)

		tab2 = QWidget()
		textEditTokensSourceCode = QTextEdit()

		textEditTokensSourceCode.setPlainText("salida")

		tab2hbox = QHBoxLayout()
		tab2hbox.setContentsMargins(5, 5, 5, 5)
		tab2hbox.addWidget(textEditTokensSourceCode)
		tab2.setLayout(tab2hbox)

		tab3 = QWidget()
		textEditTokensSourceCode = QTextEdit()

		textEditTokensSourceCode.setPlainText("salida")

		tab3hbox = QHBoxLayout()
		tab3hbox.setContentsMargins(5, 5, 5, 5)
		tab3hbox.addWidget(textEditTokensSourceCode)
		tab3.setLayout(tab3hbox)

		self.bottomRightTabWidget.addTab(tab1, "Source Code Tokenize&d")
		self.bottomRightTabWidget.addTab(tab2, "Source Code Pars&ed")
		self.bottomRightTabWidget.addTab(tab3, "Source Code Trans&piled")

	def createbottomLeftGroupBox(self):
		self.bottomLeftGroupBox = QGroupBox("Source Code")
		self.bottomLeftGroupBox.setCheckable(True)
		self.bottomLeftGroupBox.setChecked(True)

		textEditSourceCode = QTextEdit()

		textEditSourceCode.setPlainText("int variable = 10\n")

		# lineEdit = QLineEdit('s3cRe7')
		# lineEdit.setEchoMode(QLineEdit.Password)

		# spinBox = QSpinBox(self.bottomLeftGroupBox)
		# spinBox.setValue(50)

		# dateTimeEdit = QDateTimeEdit(self.bottomLeftGroupBox)
		# dateTimeEdit.setDateTime(QDateTime.currentDateTime())

		# slider = QSlider(Qt.Horizontal, self.bottomLeftGroupBox)
		# slider.setValue(40)

		# scrollBar = QScrollBar(Qt.Horizontal, self.bottomLeftGroupBox)
		# scrollBar.setValue(60)

		# dial = QDial(self.bottomLeftGroupBox)
		# dial.setValue(30)
		# dial.setNotchesVisible(True)

		layout = QGridLayout()
		layout.addWidget(textEditSourceCode, 0, 0, 1, 2)
		# layout.addWidget(lineEdit, 0, 0, 1, 2)
		# layout.addWidget(spinBox, 1, 0, 1, 2)
		# layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
		# layout.addWidget(slider, 3, 0)
		# layout.addWidget(scrollBar, 4, 0)
		# layout.addWidget(dial, 3, 1, 2, 1)
		layout.setRowStretch(5, 1)
		self.bottomLeftGroupBox.setLayout(layout)

	def createProgressBar(self):
		self.progressBar = QProgressBar()
		self.progressBar.setRange(0, 10000)
		self.progressBar.setValue(0)

		timer = QTimer(self)
		timer.timeout.connect(self.advanceProgressBar)
		timer.start(1000)


if __name__ == '__main__':
	app = QApplication([])
	gallery = WidgetGallery()
	gallery.show()
	app.exec_()
