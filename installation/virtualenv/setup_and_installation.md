## Installing bamboolib using virtualenv

### 1. Create a virtual environment for your project

In the terminal enter the following where `bamboolib_venv` is the name of the virtual environment. Please change it if you want name your virtual environment differently.

```bash
virtualenv bamboolib_venv
```

### 2. Activate your virtual environment

```bash
source bamboolib_venv/bin/activate
```

### 3. Install bamboolib

Use the pip install command we have send you via e-mail.

### 4. Add the IPython kernel to Jupyter

`bamboolib_venv` is the name that will appear in the kernel list of your Jupyter Notebook. Please change this if you want to have a different kernel name.

```bash
ipython kernel install --name=bamboolib_venv
```

### 5. Install the bamboolib jupyter extension

```bash
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

### 6. Deactivate the virtual environment

This step is optional. However it is recommended since you will likely have incompatibilities between the global Jupter version and the Jupyter version specific to your virtual environment.

```bash
deactivate
```

### 7. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/with_virtual_environment.md#test-the-library).
