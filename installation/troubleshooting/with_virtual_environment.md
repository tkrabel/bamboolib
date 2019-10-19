## Troubleshooting installation errors

Please make sure that the following is correct:
- you used a Jupyter Notebook and not Jupyter Lab.
- you opened the Jupyter Notebook with Google Chrome or Firefox. You don't use Internet Explorer.
- the ipython notebook file you are working with is **not** called "bamboolib".
- the virtual environment you created has a name that is different from your other virtual environments.

If the installation still doesn't work, please continue reading.

## Manually install and enable Jupyter Extensions

As of Jupyter Notebook 5.3+, pip will not only install bamboolib, but also it's required notebook extensions. Sometimes however, this doesn't work automatically.

In such a case, you need to install and enable the bamboolib extension manually.

Open your terminal and run

```bash
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

Then, restart your Jupyter notebook (make sure to shut down the server and start it over again) and run the code snippet again.
