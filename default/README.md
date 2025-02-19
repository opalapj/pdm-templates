# my-package

## Steps after initialization

- go to `my-package` root directory:

        cd path/to/my-package

- check `pyproject.toml`:

        type pyproject.toml

- check `.pdm-python`:

        type .pdm-python

- show `my-package` info:

        pdm info

- install `my-package`:

        pdm install

- run sandbox main script:

    - with `run` command:

            pdm run python sandbox
    
    - with active `venv`:

            pdm venv activate | clip
            ctrl + v
            python sandbox

    > Logs from sandbox and `my-package` should show up.
    >
    > Error should show up as well. Check `sandbox/setup/logs.log`.

- go to sandbox main script and comment erroneus statement:

        print('Erroneous statement:', 1/0)
