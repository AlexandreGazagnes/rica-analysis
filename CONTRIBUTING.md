# Contributing

## Local development


### Prerequisites
- The complete test suite depends on having at least the following installed
  (possibly not a complete list)
  - git (Version 2.24.0 or above is required )
  - python3.10.x (Required by a test which checks different python versions)
  - poetry, pip, pipeenv, virtualenv, or similar
  - please not that poetry is highly recommended

### Setting up an environment

The project uses [Poetry](https://python-poetry.org/) to manage its dependencies. 
Please install it using the following command :

```bash
pip install poetry
```

Then, please install the dependencies using the following command :

```bash
poetry install
```

Alternatively, you can install the dependencies using the following command :

```bash
python3 -m [ venv | virtualenv ] .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r ./utils/requirements-dev.txt
```

### Running a specific test

Running a specific test with the environment activated is as easy as:
`pytest tests -k test_the_name_of_your_test`

### Running all the tests

With the environment activated you can run all of the tests
using:
```bash
pytest tests
```

### Setting up pre-commit hooks

You will have to set up pre-commit hooks by running the following command:
```bash
pre-commit install
```


### Contributing

Feel free to contribute to this project : 

* open an issue if you have any question.
* open a pull request if you want to contribute.

And as matter of fact, in your life in general, please feel free. 😉


### Documentation

For further information, please visit the [documentation](https://alexandregazagnes.github.io/rica-analysis) for more information.