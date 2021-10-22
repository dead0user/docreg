from peewee import *
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


db = SqliteDatabase('documents.db')


class Document(Model):
    date = DateField()
    netto_quota = FloatField()
    doc_number = CharField()
    company = CharField()
    if_short_date = CharField(max_length=25)
    if_beer = FloatField()
    if_wine = FloatField()
    if_vodka = FloatField()

    class Meta():
        database = db

db.connect()
db.create_tables([Document])



class mainWindow(Gtk.Window):

    def __init__(self) -> None:
        Gtk.Window.__init__(self, title='Rejestr dokumentów')
        self.main_grid()

    def main_grid(self) -> None:
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(5)
        self.grid.set_row_spacing(5)
        self.add(self.grid)

        self.doc_date = Gtk.Entry()
        self.grid.attach(self.doc_date, 0, 0, 1, 1)

        self.quota = Gtk.Entry()
        self.grid.attach(self.quota, 1, 0, 1, 1)

        self.invoice_number = Gtk.Entry()
        self.grid.attach(self.invoice_number, 2, 0, 1, 1)

        self.doc_company = Gtk.Entry()
        self.grid.attach(self.doc_company, 3, 0, 1, 1)

        self.options = ['brak', 'nabiał', 'wędliny']
        self.is_short_date = Gtk.ComboBoxText()
        self.is_short_date.set_entry_text_column(0)
        for list_item in self.options:
            self.is_short_date.append_text(list_item)
        self.grid.attach(self.is_short_date, 0, 1, 1, 1)

        self.is_beer_quota = Gtk.Entry()
        self.grid.attach(self.is_beer_quota, 1, 1, 1, 1)

        self.is_wine_quota = Gtk.Entry()
        self.grid.attach(self.is_wine_quota, 2, 1, 1, 1)

        self.is_vodka_quota = Gtk.Entry()
        self.grid.attach(self.is_vodka_quota, 3, 1, 1, 1)

        self.add_document = Gtk.Button.new_with_mnemonic("_Dodaj")
        self.grid.attach(self.add_document, 2, 2, 1, 1)
        self.add_document.connect("clicked", self.add_record)

        self.quit_from_app = Gtk.Button.new_with_mnemonic("_Wyjdź")
        self.grid.attach(self.quit_from_app, 3, 2, 1, 1)


    def add_record(self, add_document):
        new_record = Document.create(
            date = self.doc_date.get_text(),
            netto_quota = self.quota.get_text(),
            doc_number = self.invoice_number.get_text(),
            company = self.doc_company.get_text(),
            if_short_date = self.is_short_date.get_active_text(),
            if_beer = self.is_beer_quota.get_text(),
            if_wine = self.is_wine_quota.get_text(),
            if_vodka = self.is_vodka_quota.get_text()
        )
        new_record.save()


if __name__ == "__main__":
    win = mainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
