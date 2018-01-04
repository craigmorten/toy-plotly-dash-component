# toy-plotly-dash-component

A toy component for using with Plotly Dash.

## Using this project

This component was generated using the Plotly Dash `Writing your own components` instructions, see the section below for details.

The component code is available in the `./toy-component/` directory.

To install the necessary packages, test and build the component, run `npm test`.

To view and test out the built component you have two options:

1. Run `python usage.py`. This imports the build component code (located within the `./toy-component/toy-component` directory) and launches a simple Dash app including the component.
1. Run `npm run demo`. This launches a development server and imports the component in a javascript/html application. This command will trigger a rebuild on code change and save, so can be quite useful for development.

To view and edit the component source code, head to `./toy-component/src/components/` and the react component will be present along with a `__tests__` directory which contains the components unit tests.

To include this component in your application elsewhere, either copy the `/toy-component/toy-component` directory to the root location of use, or you can install python package using `python setup.py install`.

## Setting up a new project

See the [Plotly Dash documentation](https://plot.ly/dash/plugins) for more detailed explanation.

1. Prerequisites include:

    - Node
    - NPM
    - Python

1. Install the builder tool:

    ```sh
    npm install -g builder-init
    ```

1. Initialise the new project by running:

    ```sh
    builder-init dash-components-archetype
    ```

    This will walk you through a series of prompts, such as the component name etc. and create the component boilerplate code.