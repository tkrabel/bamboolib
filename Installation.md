# Installation of bamboolib

**Please note: bamboolib currently only supports Jupyter Notebook.**

In order to install bamboolib, you only need to do one thing.

## pip install

From the terminal, you can install bamboolib with the pip install command that you received from us via mail.

## Test the library

To check whether everything went smoothly, start your Jupyter Notebook (`jupyter notebook`) in the terminal, create a new notebook file and run the following:

```python
import bamboolib as bam
df = bam.get_titanic_df()  # the titanic pd.DataFrame with 891 rows and 12 columns
# df = bam.get_1mio_rows_titanic_df()  # 1.079.001 rows and 12 columns
bam.show(df)
```

You should see a GUI if everything worked fine. If you don't see anything, please continue reading.

## Troubleshooting installation errors

Please make sure that the following is correct:
- you try to run bamboolib in a Jupyter Notebook. And not Jupyter Lab.
- you opened the Jupyter Notebook in the Chrome or Firefox browser. You don't use the Internet Explorer.

If the installation still doesn't work, you should try to [manually install the needed Jupyter Extensions](https://github.com/tkrabel/bamboolib/blob/master/Installation.md#manually-install-and-enable-jupyter-extensions).

## Manually install and enable Jupyter Extensions

As of Jupyter Notebook 5.3+, pip will not only install bamboolib, but also it's required notebook extensions. Sometimes however, this doesn't work automatically.

In such a case, you need to install and enable the bamboolib extension manually.

Open your terminal and run
```bash
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

Then, restart your Jupyter notebook (make sure to shut down the server and start it over again) and try the code snippet from above again.

## Installing bamboolib using virtualenv

If you manage your python packages using `virtualenv`, then follow these steps to install and use bamboolib in your virtual environment (venv).

0. pip install virtualenv if you haven't done already: `pip install virtualenv`
1. create your venv with `virtualenv <venv_name>`
2. activate the venv: `source <venv_name>/bin/activate`
3. install bamboolib
5. add the ipython kernel to jupyter: `ipython kernel install --user --name=<any_name_you_want>`. Note that the name you choose will appear in the kernel list of your jupyter notebook.

You should now be able to run bamboolib using the ipython kernel from your venv.s