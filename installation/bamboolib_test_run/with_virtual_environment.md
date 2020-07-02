## Test the library

First, start Jupyter Notebook or Jupyter Lab

```bash
jupyter notebook
# jupyter lab
```

Afterwards, create a new notebook choosing the *bamboolib_venv* kernel (**New** > *bamboolib_venv*).

Finally, run the following in a Jupyter Notebook / Lab code cell:

```python
import bamboolib as bam
import pandas as pd
df = pd.read_csv(bam.titanic_csv)
df
```

After clicking on the button displayed above the dataframe, you should see a GUI.

![](/assets/img/activation_screen.png)

 If you don't see anything or get an error message, please read [here](https://docs.bamboolib.8080labs.com/etc/faq/i-dont-see-the-user-interface-after-installing-bamboolib).
