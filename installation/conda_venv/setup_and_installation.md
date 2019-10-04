## Installing bamboolib using conda environment

### 1. Create a virtual environment for your project

In the terminal enter the following where `bamboolib_venv` is the name you want to call your environment.

```bash
conda create -n bamboolib_venv
```

Press y to proceed. This will install the Python version and all the associated anaconda packaged libraries at `<path_to_your_anaconda_location>/anaconda/envs/bamboolib_venv`

### 2. Activate your virtual environment

`bamboolib_venv` is the name you gave to your environement at creation.

```bash
conda activate bamboolib_venv
```

### 3. Install pip and ipykernel in your virtual environment

```bash
conda install pip
conda install ipykernel
```

At this point you have two versions of pip installed; a global version and a version specific to your virtual environment. Please make sure that the command `which pip` returns a path to the pip version specific to your virtual environment (something similar to "anaconda/envs/bamboolib_venv/bin/pip"). If it doesn't do so, you will need to change the `pip install` command in the following step.

### 4. Install bamboolib

First, check if you use the correct pip version (the one specific to your virtual environment). To do so, type

```bash
which pip
```

You sould read a path that contains the name of your virtual environment (something similar to "anaconda/envs/bamboolib_venv/bin/pip"). There are two cases:

- `which pip` contains the virtual environment name: In this case, you can simply use the pip install command we have send you via e-mail.
- `which pip` **doesn't show the correct path**: In this case, you need to replace "pip" in the pip install command with the absolute path to your virtual environment's pip, i.e. replace "**pip** install" with something similar to "**/anaconda/envs/bamboolib_venv/bin/pip** install".

### 5. Add the IPython kernel to Jupyter

```bash
python -m ipykernel install --user --name bamboolib_venv --display-name "bamboolib_venv"
```

### 6. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/Installation.md#test-the-library).
