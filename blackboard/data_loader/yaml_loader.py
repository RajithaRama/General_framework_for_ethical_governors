import yaml
from data_loader import loader

# import loader


class YAMLLoader(loader.Loader):

    def load(self, file_name):
        with open(file_name, 'r') as fp:
            yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
        return yaml_data