
def maximize_notebook():
    try:
        from IPython.core.display import display, HTML
        display(HTML("<style>.container { width:100% !important; }</style>"))
    except Exception as e:
        print(f'Error while maximizing the notebook cells: {str(e)}')

def apply_options(pd, max_rows = 500, max_columns = 500, d_width = 1000):
    if pd is None:
        print('Please import pandas before calling this function.')
        return

    pd.set_option('display.expand_frame_repr', True)
    pd.set_option('display.max_rows', max_rows)
    pd.set_option('display.max_columns', max_columns)
    pd.set_option('display.width', d_width)
    pd.set_option('display.max_colwidth', None)
    
    pd.options.mode.chained_assignment = None

def reload(module):
    import importlib
    importlib.reload(module)

maximize_notebook()
