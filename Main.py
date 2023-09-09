import os
import sys
import requests

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import Ui.loaderr as loader
import sg
import get_path

class MainWindow(QtWidgets.QMainWindow, loader.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.sg = sg.sg_con()
        self.user = 'alam'
        self.path_cls = get_path.GetPaths('C:/Users/s8/OneDrive - Autodesk/Desktop/checking')
        project_details = self.sg.get_projects(user_name=self.user)
        k = 1
        for proj in project_details:
            self.Projects.addItem("")
            self.Projects.setItemText(k, proj['name'])
            self.Projects.setItemData(k, proj['id'])
            k += 1
        self.Projects.activated.connect(self.display_shots)
        self.TreeView.itemClicked.connect(self.get_published)
        self.mytask.stateChanged.connect(self.display_shots)
        self.tasklist.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tasklist.customContextMenuRequested.connect(self.open_context)

    def get_published(self, data):
        if data.parent():
            self.sequence = self.sg.get_seq(data.parent().data(0,1))
            print(self.sequence)
            self.shot = data.parent().text(0)
            self.task_step = data.text(0)
            self.tasklist.clear()
            self.display.setText(f'{self.project}_{self.shot}_{self.task_step}')
            publishes = self.sg.get_publishes(data.data(0, 1))

            if len(publishes) == 0:
                QMessageBox.information(self, "Message", f"No publishes for this task")
            for publish in publishes:

                item = QListWidgetItem(publish['code'])
                item.setData(1, publish['id'])
                self.tasklist.addItem(item)

    def display_shots(self):
        self.project = self.Projects.currentText()
        self.tasklist.clear()
        self.TreeView.clear()
        self.display.clear()
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, f"{self.Projects.currentText()}")
        self.TreeView.setHeaderItem(__qtreewidgetitem)

        shots = self.sg.get_shots(self.Projects.currentData())
        k = 0
        for shot in shots:
            user = None
            if self.mytask.isChecked():
                user = self.sg.get_user('alam')['id']
            tasks = self.sg.get_tasks(shot['id'], user)
            if len(tasks) != 0:
                shot_child = QTreeWidgetItem(self.TreeView)
                shot_child.setText(0, f"{shot['code']}")
                shot_child.setData(0, 1, f"{shot['id']}")
                k += 1
            for task in tasks:
                task_child = QTreeWidgetItem(shot_child)
                task_child.setText(0, f"{task['step']['name']}")
                task_child.setData(0, 1, f"{task['id']}")
            #print(shot_child.data(0,1))
        self.details.setText(f'Total: {k} Shots')

    def open_context(self, position):
        self.path_cls.get_scene_path(self.project, self.sequence, self.shot, self.task_step)
        item = self.tasklist.itemAt(position)
        item_data = item.data(1)
        if item is not None:
            context_menu = QMenu(self)

            import_file = QAction("Import File", self)
            context_menu.addAction(import_file)
            import_file.triggered.connect(lambda: self.importer(self.sg.find_publish(item_data, self.path_cls.scene_path)))

            import_reference = QAction("Import Reference", self)
            context_menu.addAction(import_reference)
            import_reference.triggered.connect(lambda: self.import_ref())

            open_file = QAction("Open File", self)
            context_menu.addAction(open_file)
            open_file.triggered.connect(lambda: self.open_file(self.sg.get_publish(item_data)))

            file_location = QAction("File Location", self)
            context_menu.addAction(file_location)
            file_location.triggered.connect(lambda: self.open_loc())

            context_menu.exec_(self.tasklist.mapToGlobal(position))

    def importer(self, paths):
        #os.makedirs(self.path_cls.scene_path)
        #os.makedirs(self.path_cls.publish_path)

        print(paths[0], paths[1])
        response = requests.get(paths[1], stream=True)
        with open(paths[0], "wb") as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)


    def import_ref(self):
        pass

    def open_file(self, published_file):
        path = os.path.join(self.path_cls.scene_path, published_file["code"])
        try:
            os.startfile(path)
        except Exception as e:
            QMessageBox.information(self, "Message", f"Unable to open file")

    def open_loc(self):
        path = self.path_cls.publish_path
        try:
            os.startfile(self.path_cls.path_name)
        except Exception as e:
            QMessageBox.information(self, "Message", f"No path found")

if __name__ == '__main__':
    import qdarkstyle as qdarkstyle

    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    sys.exit(app.exec_())