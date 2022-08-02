# Plugins - add your own transformations, loaders or views

> __Beta:__ Plugins are currently in Beta and the API is not stable yet. Please expect that the API might change to some extent. However, we will try to minimize any changes and provide backwards compatibility.

## Scenario:
- Are you __missing a special transformation__ in bamboolib?
- Do you want to provide __custom transformations for your team__?
- Do you want to __load data from a custom source__?
- Do you want to add __custom visualizations or data explorations__?

bamboolib enables you to quickly add plugins or even write your own plugins based on your specific needs.


## Get started

1) make sure that you are running bamboolib 1.18.0 or higher. You can check this via running: `bam.__version__` If you need to upgrade, please [follow this guide](https://docs.bamboolib.8080labs.com/how-tos/update-to-a-new-version-of-bamboolib)

2) write your own plugin or [copy an example](https://github.com/tkrabel/bamboolib/tree/master/plugins/examples)

3) execute the plugin code

4) use the plugin from within the bamboolib user interface

If you have questions, please reach out via bamboolib-feedback@databricks.com

## How to permanently add my plugin to bamboolib?

3 things you should know about how plugins work:
- __Plugins are added to bamboolib after you execute the plugin code.__
- If you add a plugin, it will be available as long as the Python kernel is running.
- If you restart your Python kernel, the plugin will no longer be available.

Given those constraints there are __multiple alternatives__. Our __preferred option is number 2__:
1. Put the plugin code into an internal Python package and import the package at the top of your Jupyter Notebook. For example, you can quickly create a new Python package with [pyscaffold](https://github.com/pyscaffold/pyscaffold). You might also want to upload your own plugin package to a private or public GitHub repository and collaborate with others to make sure that you will always have all the best plugins available for your use case.
2. __[Preferred]__ Create an internal library like described in step 1. Then, use [Jupyter templates](https://towardsdatascience.com/stop-copy-pasting-notebooks-embrace-jupyter-templates-6bd7b6c00b94) in order to always automatically import bamboolib and your internal library at the top of the notebook when creating a new notebook file.
3. [Discouraged] Put the raw plugin code or the import of your internal library into a Python file in the IPython auto startup folder which is located in your home directory at `~/.ipython/profile_default/startup` This code is run by IPython every time you start a new Jupyter Python kernel. The only reason why we list this approach is because we want to let you know why we kindly discourage it. This approach hides the state and dependencies of your notebook. Thus, your notebook might not work out of the box when run on the computer of a colleague who might not have the same startup script like you do.

Do you __prefer another way?__ If so, please let us know via the issues. Your approach might be helpful to others as well :)


## Plugin architecture

If you want to build the plugins of your dreams, you basically need 2 ingredients:
1. the bamboolib internals that `bamboolib.plugins` provides to you
2. any of the user interface elements of [ipywidgets](https://github.com/jupyter-widgets/ipywidgets)


## Reference

Below, you find the description of some of the core plugin components like `LoaderPlugin`, `TransformationPlugin`, `DF_OLD`, and `DF_NEW`.

In addition, the following components can be imported from `bamboolib.plugins`:
- `BamboolibError` - helpful for raising beautiful errors
- `Singleselect`
- `Multiselect`
- `Button`
- `Text`

If you want more information about their usage, please check the Docstring e.g. using `Text?` or `help(Text)`

For more infos about their usage in the real life, please check the examples.

### bamboolib.plugins.LoaderPlugin

__Methods that you can OVERRIDE:__
- __get_code()__: this is the __bare minimum__ that is required. You need to return a string that contains Python code.
- __render()__: for adding custom user interface elements

__Helpers that you might want to USE:__

__Methods:__
- set_title()
- set_content()
- execute(): starts the code execution

__Attributes:__
- new_df_name_group: input for giving the new dataframe a name that is referenced as DF_NEW in the code
- execute_button: button that calls execute() when called


### bamboolib.plugins.TransformationPlugin

__Methods that you can OVERRIDE:__
- __get_code()__: this is the __bare minimum__ that is required. You need to return a string that contains Python code.
- __render()__: for adding custom user interface elements
- __is_valid_transformation()__: return True or False or even raise exceptions
- __get_description()__: return a description of the transformation that is shown in the history


__Helpers that you might want to USE:__

__Methods:__
- set_title()
- set_content()
- get_df()
- get_name_of_df()
- ADVANCED
    - update_code_preview()
    - get_final_code()
    - execute()

__Attributes:__
- rename_df_group
- code_preview_group
- spacer
- new_df_name_input

### bamboolib.plugins.DF_OLD

- Placeholder that you __NEED to use__ within `get_code()`

- At runtime, bamboolib will replace the placeholder with the name of the current dataframe.

### bamboolib.plugins.DF_NEW

- Placeholder that you __CAN use__ within `get_code()`

- At runtime, bamboolib will replace the placeholder with the new name of the current dataframe.
The new name can be specified by the user inside the `rename_df_group` input element.

> Attention: for TransformationPlugin the renaming will only work if you add `self.rename_df_group` to `self.set_content()`

> Attention: for LoaderPlugin the renaming will only work if you add `self.new_df_name_group` to `self.set_content()`
