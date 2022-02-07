import yaml


with open("yaml_test_1.yaml", 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

print(type(data))
