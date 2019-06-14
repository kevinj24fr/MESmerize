# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuDataframe = QtWidgets.QMenu(self.menubar)
        self.menuDataframe.setObjectName("menuDataframe")
        self.menuSave_current_tab = QtWidgets.QMenu(self.menuDataframe)
        self.menuSave_current_tab.setObjectName("menuSave_current_tab")
        self.menuSave_all_tabs = QtWidgets.QMenu(self.menuDataframe)
        self.menuSave_all_tabs.setObjectName("menuSave_all_tabs")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockConsole = QtWidgets.QDockWidget(MainWindow)
        self.dockConsole.setMinimumSize(QtCore.QSize(68, 200))
        self.dockConsole.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockConsole.setObjectName("dockConsole")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockConsole.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockConsole)
        self.actionDataframe_editor = QtWidgets.QAction(MainWindow)
        self.actionDataframe_editor.setObjectName("actionDataframe_editor")
        self.actionConsole = QtWidgets.QAction(MainWindow)
        self.actionConsole.setCheckable(True)
        self.actionConsole.setObjectName("actionConsole")
        self.actionCurrent_tab_filter_history = QtWidgets.QAction(MainWindow)
        self.actionCurrent_tab_filter_history.setObjectName("actionCurrent_tab_filter_history")
        self.actionUpdate_current_tab = QtWidgets.QAction(MainWindow)
        self.actionUpdate_current_tab.setObjectName("actionUpdate_current_tab")
        self.actionUpdate_all_tabs = QtWidgets.QAction(MainWindow)
        self.actionUpdate_all_tabs.setObjectName("actionUpdate_all_tabs")
        self.actionto_pickle_tab = QtWidgets.QAction(MainWindow)
        self.actionto_pickle_tab.setObjectName("actionto_pickle_tab")
        self.actionto_csv_tab = QtWidgets.QAction(MainWindow)
        self.actionto_csv_tab.setObjectName("actionto_csv_tab")
        self.actionto_excel_tab = QtWidgets.QAction(MainWindow)
        self.actionto_excel_tab.setObjectName("actionto_excel_tab")
        self.actionto_pickle = QtWidgets.QAction(MainWindow)
        self.actionto_pickle.setObjectName("actionto_pickle")
        self.actionto_excel = QtWidgets.QAction(MainWindow)
        self.actionto_excel.setObjectName("actionto_excel")
        self.actionto_csv = QtWidgets.QAction(MainWindow)
        self.actionto_csv.setObjectName("actionto_csv")
        self.actionLink_viewers = QtWidgets.QAction(MainWindow)
        self.actionLink_viewers.setObjectName("actionLink_viewers")
        self.actionSave_to_project = QtWidgets.QAction(MainWindow)
        self.actionSave_to_project.setObjectName("actionSave_to_project")
        self.menuSave_current_tab.addSeparator()
        self.menuSave_current_tab.addAction(self.actionto_pickle_tab)
        self.menuSave_current_tab.addAction(self.actionto_csv_tab)
        self.menuSave_current_tab.addAction(self.actionto_excel_tab)
        self.menuSave_all_tabs.addAction(self.actionto_pickle)
        self.menuSave_all_tabs.addAction(self.actionto_csv)
        self.menuSave_all_tabs.addAction(self.actionto_excel)
        self.menuDataframe.addAction(self.actionDataframe_editor)
        self.menuDataframe.addSeparator()
        self.menuDataframe.addAction(self.actionUpdate_all_tabs)
        self.menuDataframe.addAction(self.actionUpdate_current_tab)
        self.menuDataframe.addSeparator()
        self.menuDataframe.addAction(self.menuSave_current_tab.menuAction())
        self.menuDataframe.addAction(self.menuSave_all_tabs.menuAction())
        self.menuDataframe.addSeparator()
        self.menuDataframe.addAction(self.actionSave_to_project)
        self.menuView.addAction(self.actionCurrent_tab_filter_history)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionConsole)
        self.menuTools.addAction(self.actionLink_viewers)
        self.menubar.addAction(self.menuDataframe.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.actionConsole.toggled['bool'].connect(self.dockConsole.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuDataframe.setTitle(_translate("MainWindow", "Dataf&rame"))
        self.menuSave_current_tab.setTitle(_translate("MainWindow", "&Save current tab"))
        self.menuSave_all_tabs.setTitle(_translate("MainWindow", "Export root"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuTools.setTitle(_translate("MainWindow", "Too&ls"))
        self.dockConsole.setWindowTitle(_translate("MainWindow", "&Console: Project Browser"))
        self.actionDataframe_editor.setText(_translate("MainWindow", "&Dataframe editor"))
        self.actionConsole.setText(_translate("MainWindow", "C&onsole"))
        self.actionCurrent_tab_filter_history.setText(_translate("MainWindow", "&Current tab filter history"))
        self.actionUpdate_current_tab.setText(_translate("MainWindow", "Update &current tab"))
        self.actionUpdate_all_tabs.setText(_translate("MainWindow", "&Update all tabs"))
        self.actionto_pickle_tab.setText(_translate("MainWindow", "&to pickle"))
        self.actionto_pickle_tab.setToolTip(_translate("MainWindow", "Save current tab as a python pickle"))
        self.actionto_csv_tab.setText(_translate("MainWindow", "to &csv"))
        self.actionto_excel_tab.setText(_translate("MainWindow", "to &excel"))
        self.actionto_pickle.setText(_translate("MainWindow", "&to pickle"))
        self.actionto_excel.setText(_translate("MainWindow", "to &excel"))
        self.actionto_csv.setText(_translate("MainWindow", "to &csv"))
        self.actionLink_viewers.setText(_translate("MainWindow", "&Link viewers"))
        self.actionSave_to_project.setText(_translate("MainWindow", "Save to project"))

