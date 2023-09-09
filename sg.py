from shotgun_api3.shotgun import Shotgun
import getpass
import os
import requests

class sg_con:
    def __init__(self):
        # self.__sg = Shotgun(
        #     base_url='https://seecubicindia.shotgrid.autodesk.com',
        #     script_name='api_admin',
        #     api_key='rcmremmTkwj1ozngvrvbbfg@o'
        # )
        self.__sg = Shotgun(
            'https://samit.shotgunstudio.com',
            'HDD',
            'qd-sskykmwvqe3vPibwqadswo'
        )

    def get_seq(self, shot_id):
        shot = self.__sg.find_one("Shot", [["id", "is", int(shot_id)]], ["sg_sequence"])
        return shot.get('sg_sequence')['name']

    def get_projects(self, user_name=getpass.getuser()):
        """
        Get the projects that the user is part of
        :param user_name:name of the user
        :return:
        """
        user_id = self.get_shotgun_user_id(user_name)['id']
        proj_fields = ['name', 'id']
        proj_filter = [
            ["is_demo", "is_not", True],
            ['is_template', 'is_not', True],
            ["users", "in", {"type": "HumanUser", "id": user_id}],
        ]

        projects = self.__sg.find('Project', proj_filter, proj_fields)
        return projects

    def get_shotgun_user_id(self, user_name=getpass.getuser()):
        """

        :param user_name:
        :return:
        """
        filers = [
            ['login', 'is', user_name]
        ]
        fields = ['id']
        return self.__sg.find_one('HumanUser', filers, fields)

    def get_shots(self, project_id):
        s_fields = ['code', 'id']
        s_filter = [
            ['project', 'is', {'type': 'Project', 'id': project_id}]
        ]
        shots = self.__sg.find('Shot', s_filter, s_fields)
        return shots

    def get_tasks(self, shot_id, user_id):
        t_fields = ['step', 'id']
        if user_id is None:
            t_filter = [
                ["entity", "is", {"type": "Shot", "id": shot_id}],
            ]
        else:
            t_filter = [
                ["entity", "is", {"type": "Shot", "id": shot_id}],
                ["task_assignees", "in", {"type": "HumanUser", "id": user_id}],
            ]
        tasks = self.__sg.find('Task', t_filter, t_fields)
        return tasks

    def get_publishes(self, task_id):
        p_fields = ['id', 'name', 'code', 'path']
        p_filter = [
            ["task", 'is', {"type": "Task", "id": int(task_id)}],
        ]
        publishes = self.__sg.find('PublishedFile', p_filter, p_fields)
        print(publishes)
        return publishes

    def get_user(self, user_name):
        filers = [
            ['login', 'is', user_name]
        ]
        fields = ['id']
        return self.__sg.find_one('HumanUser', filers, fields)

    def find_publish(self, pub_id, path):
        published_file = self.__sg.find_one("PublishedFile", [["id", "is", pub_id]], fields=["path", "name", 'code'])

        download_url = published_file['path']['url']

        # Specify the local path where you want to save the downloaded file
        local_path = os.path.join(path, published_file["code"])
        return [local_path, download_url]

    def get_publish(self, pub_id):
        published_file = self.__sg.find_one("PublishedFile", [["id", "is", pub_id]], fields=["path", "name", 'code'])
        return published_file