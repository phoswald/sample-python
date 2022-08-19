import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("glade-dialog.glade")

entry1 = builder.get_object("entry1")
entry2 = builder.get_object("entry2")

def onButton1(button):
    print("Button1: pressed: " + entry1.get_text() + " " + entry2.get_text())

def onButton2(button):
    print("Button2: pressed")
    entry1.set_text("Empty...")
    entry2.set_text("...again")

handlers = {
    "onDestroy": Gtk.main_quit,
    "onButton1": onButton1,
    "onButton2": onButton2
}

builder.connect_signals(handlers)
window = builder.get_object("root")
window.show_all()

Gtk.main()
