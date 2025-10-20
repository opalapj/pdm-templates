# my-package

## Steps after initialization

- go to project root directory:

        cd path/to/my-package

- check `pyproject.toml`:

        type pyproject.toml

- check `.pdm-python`:

        type .pdm-python

- show project info:

        pdm info

- install `my-package`:

        pdm install

- run example script:

        pdm run python scripts/example.py

    > Logs from `example.py` and `my-package` should show up.
    >
    > Error should show up as well. Check `scripts/setup/logs.log`.

- go to example script and comment erroneus statement:

        print('Erroneous statement:', 1/0)
