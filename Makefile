install:
	poetry install

test_mlflow:
	poetry run python -m azure_config.test_experiment