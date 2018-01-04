'''
usage.py
'''

import os
from toy_component import ToyComponent
import flask
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

# <div className="container">
#     <h1>Demo: toy-component</h1>

#     <ToyComponent
#         className="toy"
#         label="This is an example label"
#         value={this.state.value}
#         setProps={newProps => this.setState({value: newProps.value})}
#     />
# </div>

app.layout = html.Div([
    html.H1(
        ['Demo: toy-component']
    ),

    ToyComponent(
        id='toy-input',
        value='',
        label='This is an example label'
    ),

    html.Div(
        [],
        id='output',
        className='output'
    )
], className='container')


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('toy-input', 'value')])
def display_output(value):
    '''
    Display the output
    '''
    return 'You have entered: {}'.format(value)

@app.server.route('/demo/<path:path>')
def static_file(path):
    '''
    Serve up local static files using flask
    '''
    static_folder = os.path.join(os.getcwd(), 'demo')
    return flask.send_from_directory(static_folder, path)

app.css.append_css({"external_url": "/demo/style.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
