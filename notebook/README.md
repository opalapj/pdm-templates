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

    > Important note:
    >
    > `pdm.toml` config file is added during initialization because of problem
    > with `jupyterlab-widgets` installation.

        pdm install

    > `Notebook` group from `dependencies-groups` will be installed as well.
    > Dependencies from this group are responsible for:
    > - kernelspec installation [`ipykernel`],
    > - interactive plots [`ipympl`].

- install kernelspec:

        pdm run kernel

- check if kernelspec from `my-package` venv exist:

        jupyter kernelspec list
