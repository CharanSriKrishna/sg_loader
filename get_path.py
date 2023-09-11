
class GetPaths:
    def __init__(self, path):
        self.root_path = path

    def get_scene_path(self, proj_name, seq_name, shot_name, step_name):
        """
        get the paths for scene and publish
        :return:
        """
        self.scene_path = '{0}/{1}/sequences/{2}/{3}/{4}/work/silhouette/'.format(self.root_path, proj_name, seq_name,
                                                                             shot_name, step_name)
        self.publish_path = '{0}/{1}/sequences/{2}/{3}/{4}/publish/silhouette/'.format(self.root_path, proj_name, seq_name,
                                                                             shot_name, step_name)

