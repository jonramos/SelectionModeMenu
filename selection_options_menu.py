import bpy
from bpy.types import Menu


bl_info = {
    "name": "Select Mode Pie Menu",
    "author": "Jonathan Ramos",
    "version": (0, 0, 0, 1),
    "description": "Creates a pie menu to mesh selection options. Press tilde (~) twice to open the menu",
    "blender": (2, 80, 0),
    "category": "Mesh"
}
addon_keymaps = []


def add_hotkey():

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if not kc:
        print('Keymap Error')
        return

    km = kc.keymaps.new(name='Mesh', space_type='EMPTY')

    kmi = km.keymap_items.new(
        VIEW3D_OT_PIE_template_call.bl_idname, 'Q', 'PRESS', ctrl=False, shift=False, alt=True)
    addon_keymaps.append((km, kmi))


def remove_hotkey():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()

class VIEW3D_MT_PIE_template(Menu):
    bl_label = 'Mesh Select Mode'
    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator_enum("mesh.select_mode", "type")

class VIEW3D_OT_PIE_template_call(bpy.types.Operator):
    bl_idname = 'sop.sm_template'
    bl_label = 'Mesh Select Mode'
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="VIEW3D_MT_PIE_template")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VIEW3D_MT_PIE_template)
    bpy.utils.register_class(VIEW3D_OT_PIE_template_call)
    add_hotkey()

def unregister():
    bpy.utils.unregister_class(VIEW3D_MT_PIE_template)
    bpy.utils.unregister_class(VIEW3D_OT_PIE_template_call)
    remove_hotkey()

if __name__ == "__main__":
    register()
