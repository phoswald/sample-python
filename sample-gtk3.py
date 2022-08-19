import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

window = Gtk.Window(title="Hello, World!", default_width=300, default_height=200)

vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, border_width=10, spacing=10)
window.add(vbox)

entry = Gtk.Entry()
entry.set_text("Input...")
vbox.pack_start(entry, False, True, 0)

def on_button_clicked (button):
    print("Button has been clicked: " + entry.get_text())
    entry.set_text("Result")

button = Gtk.Button(label="Click Here")
button.connect("clicked", on_button_clicked)
vbox.pack_start(button, True, True, 0)

window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
