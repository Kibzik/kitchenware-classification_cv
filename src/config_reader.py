import yaml


def read_config(config_path: str) -> dict:
    """
    Reads config from .yaml file.
    :param config_path: path to .yaml file to load from

    :return: configuration dictionary
    """
    with open(config_path, "rb") as f_in:
        config = yaml.safe_load(f_in)
    return config


def parse_train_config(config: dict) -> dict:
    """
    Parses the model configuration dictionary.
    :param config: model configuration dictionary

    :return: model configuration parameters
    """
    params = dict()
    params["input_data_path"] = config["input_data_path"]
    params["output_model_path"] = config["output_model_path"]
    params["split_test_size"] = config["splitting_params"]["test_size"]
    params["split_random_state"] = config["splitting_params"]["random_state"]

    params["learning_rate"] = config["train_params"]["learning_rate"]
    params["input_size"] = config["train_params"]["input_size"]
    return params
