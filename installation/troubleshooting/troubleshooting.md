## Troubleshooting installation errors

Please make sure that the following is correct:
- you try to run bamboolib in a Jupyter Notebook and not Jupyter Lab.
- you opened the Jupyter Notebook in the Chrome or Firefox browser. You don't use the Internet Explorer.

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
