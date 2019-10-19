## Installing bamboolib without virtual environment

### 1. Install bamboolib

From the terminal, you can install bamboolib with the `pip install` command that you received from us via mail.

```bash
USE PIP COMMAND FROM E-MAIL
```

If you get an error like `"bad interpreter"`, use pip3 instead.

### 2. Setup Jupyter extensions

From the terminal, you need to setup the Jupyter Notebook extensions via the following command:

```bash
jupyter nbextension enable --py qgrid --sys-prefix
```

### 3. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/without_virtual_environment.md#test-the-library).
