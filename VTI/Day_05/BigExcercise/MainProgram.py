import sys
from functools import partial
from studentMng import *
from subjectMng import *
from scoreMng import *


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QMenu,
    QSpinBox,
    QToolBar,
)

class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("VTI - Python 01 Class")
        self.resize(400, 200)
        self.centralWidget = QLabel("Student Score Management")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._connectActions()

    def _createMenuBar(self):
        menuBar = self.menuBar()

        # Student menu
        studentMenu = QMenu("&Student", self)
        menuBar.addMenu(studentMenu)
        studentMenu.addAction(self.addAction)
        studentMenu.addAction(self.editAction)
        studentMenu.addAction(self.deleteAction)
        studentMenu.addAction(self.findAction)

        # Subject menu
        subjectMenu = menuBar.addMenu("&Subject")
        subjectMenu.addAction(self.addSubject)
        subjectMenu.addAction(self.editSubject)
        subjectMenu.addAction(self.deleteSubject)
        subjectMenu.addAction(self.findSubject)

        # Score menu
        scoreMenu = menuBar.addMenu("&Score")
        scoreMenu.addAction(self.addScore)
        scoreMenu.addAction(self.editScore)
        # scoreMenu.addAction(self.findScore)
        findMenu = scoreMenu.addMenu("Find by")
        findMenu.addAction(self.findScorebyID)
        findMenu.addAction(self.findScorebyName)
        scoreMenu.addAction(self.statisticScore)

        # Export Excel menu
        exportMenu = menuBar.addMenu("&Export")
        exportMenu.addAction(self.export)

    def _createActions(self):
        # Student actions
        self.addAction = QAction(self)
        self.addAction.setText("&Add")
        self.addAction.setIcon(QIcon(":file-new.svg"))
        self.editAction = QAction(QIcon(":file-open.svg"), "&Edit", self)
        self.deleteAction = QAction(QIcon(":file-save.svg"), "&Delete", self)
        self.findAction = QAction("&Find", self)

        # Subjects actions
        self.addSubject = QAction(QIcon(":file-new.svg"), "&Add", self)
        self.editSubject = QAction(QIcon(":file-open.svg"), "&Edit", self)
        self.deleteSubject = QAction(QIcon(":file-save.svg"), "&Delete", self)
        self.findSubject = QAction("&Find", self)

        # Score actions
        self.addScore = QAction(self)
        self.addScore.setText("&Add")
        self.addScore.setIcon(QIcon(":file-new.svg"))
        self.editScore = QAction(QIcon(":file-open.svg"), "&Edit", self)
        self.findScorebyID = QAction("Student ID", self)
        self.findScorebyName = QAction("Student name", self)
        self.statisticScore = QAction(QIcon(":file-save.svg"), "&Score Statistic", self)

        # Export actions
        self.export = QAction(self)
        self.export.setText("&Export Excel")

    def contextMenuEvent(self, event):
        # Context menu
        menu = QMenu(self.centralWidget)
        # Populating the menu with actions
        menu.addAction(self.addAction)
        menu.addAction(self.openAction)
        menu.addAction(self.saveAction)
        enu.exec(event.globalPos())

    def _connectActions(self):
        # Connect Students actions
        self.addAction.triggered.connect(self.addStudent)
        self.editAction.triggered.connect(self.editStudent)
        self.deleteAction.triggered.connect(self.deleteStudent)
        self.findAction.triggered.connect(self.findStudent)

        # Connect Subjects actions

        self.addSubject.triggered.connect(self.addSubjects)
        self.editSubject.triggered.connect(self.editSubjects)
        self.deleteSubject.triggered.connect(self.deleteSubjects)
        self.findSubject.triggered.connect(self.findSubjects)

        # Connect Scores actions
        self.addScore.triggered.connect(self.addScores)
        self.editScore.triggered.connect(self.editScores)
        self.findScorebyID.triggered.connect(self.findScoresID)
        self.findScorebyName.triggered.connect(self.findScoresName)
        self.statisticScore.triggered.connect(self.statisticScores)

        # Connect Export actions
        self.export.triggered.connect(self.exportExcel)

    # def code implement
    # Student def
    def addStudent(self):
        insertStd()

    def editStudent(self):
        editStd()

    def deleteStudent(self):
        deleteStd()

    def findStudent(self):
        findStd()

    # Subjects def
    def addSubjects(self):
        insertSbj()

    def editSubjects(self):
        editSbj()

    def deleteSubjects(self):
        deleteSbj()

    def findSubjects(self):
        findSbj()

    # Score def
    def addScores(self):
        insertScr()

    def editScores(self):
        editScr()

    def statisticScores(self):
        statisticScr()

    def exportExcel(self):
        processExportToExcel()

    def findScoresID(self):
        studentid = input('Input student ID:: ')
        findScrID(studentid)

    def findScoresName(self):
        studentName = input('Input student Name:: ')
        findScrName(studentName)

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())