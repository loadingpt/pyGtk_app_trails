#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Version: 0.9.4
# Authors: Miguel Seridonio Almeida Fernandes,
#       Isaac Silva,
#       Andre Pacheco


# import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import sys


import Access
import Trail


ABOUT = """
License: GPL
Version: 0.9.2
Author: Miguel Seridoneo
"""
ACCESS_FILE = "access.txt"

LOGGIN_IN = [
        "Logging in.",
        "Logging in..",
        "Logging in..."
        ]

SHOW_LABEL = ["Show Trails", "Hide Trails"]



class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        super(Window, self).__init__(title="Trails",
                                    default_width=450,
                                    default_height=300,
                                    application=app,
                                    )

        menubar = Gtk.MenuBar()
        menubar.props.hexpand = True

        fmi = Gtk.MenuItem.new_with_label("File")

        menu = Gtk.Menu()
        emi = Gtk.MenuItem.new_with_label("Exit")
        emi.connect("activate", self.quit_app)
        ami = Gtk.MenuItem.new_with_label("About")
        ami.connect("activate", self.about)
        menu.append(emi)

        fmi.set_submenu(menu)

        menubar.add(fmi)
        menubar.add(ami)

        self.user_entry = Gtk.Entry(margin_right=64,
                            halign=1,
                            max_length=18,
                            width_chars=17
                            )

        self.pass_entry = Gtk.Entry(margin_right=64,
                            halign=1,
                            max_length=18,
                            width_chars=17,
                            visibility=False,
                            )

        user_label = Gtk.Label(label="Username:",
                            margin_left=64,
                            halign=2,
                            )

        pass_label = Gtk.Label(label="Password:",
                            margin_left=64,
                            halign=2,
                            )

        self.grid2 = Gtk.Grid(column_spacing=32,
                            row_spacing=32,
                            halign=3,
                            valign=3,
                            )

        self.trails_table = Gtk.Grid(row_spacing=12,
                            column_spacing=16,
                            halign=3,
                            # column_homogeneous=True,
                            margin_left=64,
                            margin_right=64,
                            margin_bottom=64,
                            )

        trail = Trail.Trail("text.txt")
        trail_rows = trail.get_trails()

        r = 0
        for i in trail_rows:
            c = 0
            for n in trail_rows[i]:
                self.trails_table.attach(Gtk.Label(label=trail_rows[i][n]), c, r, 1, 1)
                c += 1
            r += 1

        self.login_b = Gtk.Button(label="Login", hexpand=True, halign=3, margin_bottom=64)
        self.login_b.connect("clicked", self.login)

        self.create_acc_b = Gtk.Button(label="Create Account", hexpand=True, halign=3, margin_bottom=64)
        self.create_acc_b.connect("clicked", self.create_acc)

        self.login_grid = Gtk.Grid(halign=3,
                                column_spacing=16,
                                )

        self.login_grid.attach(self.login_b, 0, 0, 1, 1)
        self.login_grid.attach(self.create_acc_b, 1, 0, 1, 1)

        self.grid2.attach(user_label, 0, 0, 1, 1)
        self.grid2.attach(pass_label, 0, 1, 1, 1)
        self.grid2.attach(self.user_entry, 1, 0, 1, 1)
        self.grid2.attach(self.pass_entry, 1, 1, 1, 1)

        self.grid = Gtk.Grid(row_spacing=64, column_homogeneous=True)
        self.grid.attach(menubar, 0, 0, 1, 1)
        self.grid.attach(self.grid2, 0, 1, 1, 1)
        self.grid.attach(self.login_grid, 0, 2, 1, 1)

        self.log = Access.Access("access.txt")
        self.tid = None
        self.add(self.grid)

    def main_menu(self, parent):
        while(self.grid.get_child_at(0, 1) != None):
            self.grid.remove_row(1)
        self.grid.attach(self.grid2, 0, 1, 1, 1)
        self.grid.attach(self.login_grid, 0, 2, 1, 1)
        self.resize
        self.grid.show_all()


    def user_win(self, parent):
        user_menu = Gtk.Grid(row_spacing=16,
                            column_spacing=16,
                            halign=3,
                            column_homogeneous=True,
                            margin_right=32,
                            margin_left=32,
                            )
        u_show_button = Gtk.Button(label="Show Trails")
        u_show_button.connect("clicked", self.show_trails)
        u_experience_button = Gtk.Button(label="Trail Experience")
        u_experience_button.connect("clicked", self.trail_experience_input, u_show_button)
        u_recomendation_button = Gtk.Button(label="Trail Recomendation")
        u_recomendation_button.connect("clicked", self.trail_recomendation, u_show_button)
        u_back_button = Gtk.Button(label="Logout")
        u_back_button.connect("clicked", self.main_menu)
        user_menu.attach(u_show_button, 0, 0, 1, 1)
        user_menu.attach(u_experience_button, 1, 0, 1, 1)
        user_menu.attach(u_recomendation_button, 2, 0, 1, 1)
        user_menu.attach(u_back_button, 1, 1, 1, 1)
        self.grid.remove(self.l)
        self.grid.attach(user_menu, 0, 1, 1, 1)
        self.grid.show_all()
        return False


    def admin_win(self, parent):
        admin_menu = Gtk.Grid(row_spacing=16,
                            halign=3,
                            row_homogeneous=True,
                            column_homogeneous=True,
                            )
        a_manage_button = Gtk.Button(label="Manage Trails")
        a_manage_button.connect("clicked", self.manage_trails_menu)
        a_back_button = Gtk.Button(label="Logout")
        a_back_button.connect("clicked", self.main_menu)
        admin_menu.attach(a_manage_button, 0, 0, 1, 1)
        admin_menu.attach(a_back_button, 0, 1, 1, 1)
        self.grid.remove(self.l)
        self.grid.attach(admin_menu, 0, 1, 1, 1)
        self.grid.attach(self.trails_table, 0, 2, 1, 1)
        self.grid.show_all()
        return False


    def manage_trails_menu(self, parent):
        pass


    def show_trails(self, parent):
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        if parent.props.label == SHOW_LABEL[0]:
            self.grid.attach(self.trails_table, 0, 2, 1, 1)
            parent.set_label(SHOW_LABEL[1])
            self.grid.show_all()
        else:
            parent.set_label(SHOW_LABEL[0])


    def trail_experience_input(self, par, parent):
        parent.set_label(SHOW_LABEL[0])
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        experience_grid = Gtk.Grid(halign=3)
        trail_grid = Gtk.Grid(halign=3)
        day_of_visit = Gtk.ComboBox(width_chars=3,
                            max_length=2,
                            placeholder_text="dd",
                            hexpand=False
                            )
        #change to ComboBox
        month_of_visit = Gtk.ComboBox(width_chars=3,
                            max_length=2,
                            placeholder_text="mm",
                            )
        year_of_visit = Gtk.ComboBox(width_chars=2,
                            max_length=2,
                            placeholder_text="yy",
                            )
        date_label = Gtk.Label(label="Date:",
                            margin_right=6,
                            )
        rating = Gtk.ComboBox(width_chars=2,
                        max_length=1,
                        )
        rating_label = Gtk.Label(label="Rating:",
                                margin_right=6,
                                margin_left=10,
                                )
        trail = Gtk.ComboBox(width_chars=22,
                        max_length=20,
                        halign=3,
                        )
        trail_label = Gtk.Label(label="Trail:",
                            margin_right=6,
                            )
        trail_grid.attach(trail_label, 0, 0, 1, 1)
        trail_grid.attach(trail, 1, 0, 1, 1)
        experience_grid.attach(date_label, 0, 1, 1, 1)
        experience_grid.attach(day_of_visit, 1, 1, 1, 1)
        experience_grid.attach(month_of_visit, 2, 1, 1, 1)
        experience_grid.attach(year_of_visit, 3, 1, 1, 1)
        experience_grid.attach(rating_label, 4, 1, 1, 1)
        experience_grid.attach(rating, 5, 1, 1, 1)
        holder_grid = Gtk.Grid(halign=3,
                            row_spacing = 16,
                            margin_bottom=16,
                            )
        holder_grid.attach(trail_grid, 0, 0, 1, 1)
        holder_grid.attach(experience_grid, 0, 1, 1, 1)
        self.grid.attach(holder_grid, 0, 2, 1, 1)
        self.grid.show_all()


    def trail_recomendation(self, par, parent):
        parent.set_label(SHOW_LABEL[0])
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)


    def create_acc(self, parent):
        while(self.grid.get_child_at(0, 1) != None):
            self.grid.remove_row(1)
        user_label = Gtk.Label(label="Username:")
        pass_label = Gtk.Label(label="Password:")
        ck_pass_label = Gtk.Label(label="Confirm Password:")
        country_label = Gtk.Label(label="Country:")
        gender_label = Gtk.Label(label="Gender:")
        age_range_label = Gtk.Label(label="Age Range:")
        user_entry = Gtk.Entry()
        pass_entry = Gtk.Entry(visibility=False)
        ck_pass_entry = Gtk.Entry(visibility=False)
        country_cbox = Gtk.ComboBox()
        gender_cbox = Gtk.ComboBox()
        age_range_cbox = Gtk.ComboBox()
        create_acc_grid = Gtk.Grid(halign=3,
                                row_spacing=16,
                                column_spacing=12,
                                                                )
        create_acc_grid.attach(user_label, 0, 0, 1, 1)
        create_acc_grid.attach(pass_label, 0, 1, 1, 1)
        create_acc_grid.attach(ck_pass_label, 0, 2, 1, 1)
        create_acc_grid.attach(country_label, 0, 3, 1, 1)
        create_acc_grid.attach(gender_label, 0, 4, 1, 1)
        create_acc_grid.attach(age_range_label, 0, 5, 1, 1)
        create_acc_grid.attach(user_entry, 1, 0, 1, 1)
        create_acc_grid.attach(pass_entry, 1, 1, 1, 1)
        create_acc_grid.attach(ck_pass_entry, 1, 2, 1, 1)
        create_acc_grid.attach(country_cbox, 1, 3, 1, 1)
        create_acc_grid.attach(gender_cbox, 1, 4, 1, 1)
        create_acc_grid.attach(age_range_cbox, 1, 5, 1, 1)
        create_acc_label = Gtk.Label(label="Create Account")
        confirm_submission = Gtk.Button(label="Submit",
                                        halign=3,
                                        )
        confirm_submission.connect("clicked", self.submit_acc, [user_entry,
                                                                pass_entry,
                                                                ck_pass_entry,
                                                                country_cbox,
                                                                gender_cbox,
                                                                age_range_cbox])
        back_b = Gtk.Button(label="Back",
                            halign=3,
                            )
        back_b.connect("clicked", self.main_menu)
        c_a_grid = Gtk.Grid(halign=3,
                        row_spacing=32,
                        column_homogeneous=True,
                        margin_right=32,
                        margin_left=32,
                        margin_bottom=48,
                        )
        b_grid = Gtk.Grid(halign=3,
                            column_spacing=12,
                            )
        b_grid.attach(confirm_submission, 0, 0, 1, 1)
        b_grid.attach(back_b, 1, 0, 1, 1)
        c_a_grid.attach(create_acc_label, 0, 0, 1, 1)
        c_a_grid.attach(create_acc_grid, 0, 1, 1, 1)
        c_a_grid.attach(b_grid, 0, 2, 1, 1)
        self.grid.attach(c_a_grid, 0, 1, 1, 1)
        self.grid.show_all()


    def submit_acc(self, parent, widgets:list):
        u, p, ck_p, c, g, a = widgets[0], widgets[1], widgets[2], widgets[3], widgets[4], widgets[5]
        status = self.log.create_acc_gtk([u.text, p.text, ck_p.text, c.text, g.text, a.text])
        if status != 0:
            pass
        else:
            pop = Gtk.Popover()
            pop.set_relative_to(parent)
            pop.add(Gtk.Label(label="Incorrect Login!"))
            pop.show_all()
            pop.popup()

            pass


    def login(self, parent):
        if self.log.login_gtk(self.user_entry.get_text(), self.pass_entry.get_text()):
            pop = Gtk.Popover()
            pop.set_relative_to(self.login_b)
            pop.add(Gtk.Label(label="Incorrect Login!"))
            pop.show_all()
            pop.popup()
            self.pass_entry.set_text("")
            self.t_pop = GLib.timeout_add(1000, self.pop_down, pop)
        else:
            parent = self.grid2.get_parent()
            while(self.grid.get_child_at(0, 1) != None):
                self.grid.remove_row(1)
            self.l = Gtk.Label(label="Logging in")
            self.l_value = 0
            parent.attach(self.l, 0, 1, 1, 1)
            parent.show_all()
            self.pass_entry.set_text("")
            self.user_entry.set_text("")
            print(self.log.get_u_pass())
            self.tid = GLib.timeout_add(300, self.loggin_in, parent)
            if self.log.logged_in == "admin":
                self.t_admin = GLib.timeout_add(1600, self.admin_win, parent)
            else:
                self.t_user = GLib.timeout_add(1600, self.user_win, parent)


    def loggin_in(self, parent):
        if self.l.get_parent() != parent:
            self.l = None
            return False
        if self.l_value < 2:
            self.l_value += 1
        else:
            self.l_value = 0
        self.l.set_text(LOGGIN_IN[self.l_value])
        parent.show_all()
        return True


    def about(self, parent):
        about_win = Gtk.Popover()
        vbox = Gtk.Grid()
        vbox.add(Gtk.Label(label=ABOUT))
        about_win.add(vbox)
        about_win.set_relative_to(parent)
        about_win.show_all()
        about_win.popup()
        self.t_pop = GLib.timeout_add(3000, self.pop_down, about_win)


    def pop_down(self, parent):
        parent.popdown()


    def quit_app(self, parent):
        app.quit()



class Application(Gtk.Application):
    def __init__(self):
        super(Application, self).__init__()


    def do_activate(self):
        self.win = Window(self)
        self.win.show_all()


    def do_startup(self):
        Gtk.Application.do_startup(self)


app = Application()
app.run(sys.argv)



#eof
