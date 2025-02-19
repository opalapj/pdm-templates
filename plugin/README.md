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

- install `my-package` locally:

        pdm install --plugins

    > `my-package` is installed in development mode, according to `pyproject.toml`

- test `my-package` locally:

        pdm hello

    > `hello` is temporary name specified in plugin source code.

- activate plugin globally:

    - published to `PyPI`:

            pdm self add <plugin>
    
    - using locally developed plugin:

            pdm self add file:///path/to/plugin
