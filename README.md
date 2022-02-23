# README #

This repository contains necessary files for the Azure-MLflow integration. The next
steps will walk you through the initialization process and the testing procedure. After
completion your environment would be ready to play with Azure ML for the logging
purposes.

## Setup ###

### Install `poetry`

With your preferred method install `poetry` tool. Please note, that installing `poetry`
with other that **recommended** method (curl) could cause troubles. Using `pip`,
`homebrew` or other similar method could cause `PATH` problems and lead
to errors while setting-up some packages.
See [installation instructions for poetry](https://github.com/python-poetry/poetry#installation).

### Install dependencies

Just run:
```sh
make install
```

### Environment

You should export environment variables from `.envrc` file located in the main
project directory, but first, fill the missing `Azure` parameters -> SUBSCRIPTION_ID,
WORKSPACE_ID and RESOURCE_GROUP. Run:
```sh
source .envrc
```

**Highly recommended** to use `direnv` for automation of this procedure.

### Testing ###

To test the connection with your Azure ML Workspace run:
```sh
make test_mlflow
```

## Sources

* panda.jpg - <a href="https://www.flaticon.com/free-icons/cute" title="cute icons">Cute icons created by Smashicons - Flaticon</a>