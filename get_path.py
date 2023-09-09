
class GetPaths:
    def __init__(self, path):
        self.root_path = path

    def get_scene_path(self, proj_name, seq_name, shot_name, step_name):
        """

        :return:
        """
        self.path_name = '{0}/{1}/sequences/{2}/{3}/{4}/'.format(self.root_path, proj_name, seq_name,
                                                                             shot_name, step_name)
        #print(self.root_path, proj_name, seq_name, shot_name, step_name)
        self.scene_path = '{0}/{1}/sequences/{2}/{3}/{4}/work/silhouette/'.format(self.root_path, proj_name, seq_name,
                                                                             shot_name, step_name)
        self.publish_path = '{0}/{1}/sequences/{2}/{3}/{4}/publish/silhouette/'.format(self.root_path, proj_name, seq_name,
                                                                             shot_name, step_name)
        #return self.scene_path
        #return [scene_path, publish_path]
