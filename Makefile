install:
	poetry install

test_mlflow:
	poetry run python -m test_example.test_experiment