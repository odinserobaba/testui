from nicegui import ui, app
import subprocess

def get_test_commands():
    test_commands = [
        {
            'name': 'Test get info 1',
            'command': 'pytest test_api.py -k test_get_info1',
            'description': 'This test checks the get info 1 endpoint'
        },
        {
            'name': 'Test get info 2',
            'command': 'pytest test_api.py -k test_get_info2',
            'description': 'This test checks the get info 2 endpoint'
        },
    ]
    return test_commands

def run_tests(command, param):
    command = command.format(param=param)
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output

@ui.page('/')
def index():
    ui.label('Select tests to run')

    # Добавляем переключатель темной и светлой темы
    dark = ui.dark_mode()
    ui.label('Switch mode:')
    ui.button('Dark', on_click=dark.enable)
    ui.button('Light', on_click=dark.disable)

    test_commands = get_test_commands()
    for test in test_commands:
        with ui.card().classes('w-full max-w-5xl'):
            ui.label(test['description'])
            param = ui.input(label='Parameter').classes('w-full max-w-5xl')
            result = ui.textarea(label='Test results').classes('w-full max-w-5xl')
            ui.button('Run test', on_click=lambda test=test, param=param, result=result: result.set_value(run_tests(test['command'], param.value)))

ui.run()
