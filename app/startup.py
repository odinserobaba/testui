from nicegui import ui, app
import subprocess
dark = ui.dark_mode()
dark.enable
def get_test_commands():
    test_commands = [
        'pytest -k "test_get_info2" test_api.py',
        'pytest -k "test_get_info1" test_api.py',
    ]
    return test_commands

def run_tests(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output

@ui.page('/')
def index():
    with ui.card().classes('w-full max-w-2xl'):
        ui.label('Select tests to run')
        test_commands = get_test_commands()
        selected_tests = ui.select(test_commands, multiple=True, label='Tests').classes('w-full')
        run_button = ui.button('Run tests', on_click=lambda: result.set_value(run_tests(selected_tests.value[0])))
        result = ui.textarea(label='Test results').classes('w-full h-64')

ui.dark_mode()

ui.run()
