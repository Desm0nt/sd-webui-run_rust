from modules import script_callbacks, shared
import modules.scripts as scripts
import gradio as gr
import os

class CLS(scripts.Script):

    def title(self):
        return "Clear Screen"

    def show(self, is_img2img):
        return scripts.AlwaysVisible if not is_img2img else None

    def ui(self, is_img2img):
        if is_img2img is True:
            return None

        def clear_console():
            if os.name == 'nt':
                os.startfile(f'c:\\Program Files\\RustDesk\\rustdesk.exe')
            else:
                os.startfile(f'c:\\Program Files\\RustDesk\\rustdesk.exe')

        reload_button = gr.Button('🆑🆑', elem_id='cls_btn2')
        reload_button.click(fn=clear_console)
        return None


def on_ui_settings():
    shared.opts.add_option("cls_on_reload2", shared.OptionInfo(
        False, "Automatically Clear Screen on ReloadUI", section=('system', 'System')
    ))

script_callbacks.on_ui_settings(on_ui_settings)


def auto_clear_console():
    if getattr(shared.opts, 'cls_on_reload2', False):

        if os.name == 'nt':
            os.startfile(f'c:\\Program Files\\RustDesk\\rustdesk.exe')
        else:
            os.startfile(f'c:\\Program Files\\RustDesk\\rustdesk.exe')

script_callbacks.on_script_unloaded(auto_clear_console)
