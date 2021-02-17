class GuiCrudMaker:

    def __init__(self):
        from db import connect
        self.connect = connect
        self.cursor = connect.cursor()

    def create(self, data):
        add_data = ("INSERT INTO wish_list "
                    "(title, price, link, about) "
                    "VALUES (%s, %s, %s, %s)")
        self.cursor.execute(add_data, data)
        self.connect.commit()
        self.cursor.close()

    def read(self):
        # read_data = f"SELECT * FROM wish_list WHERE id={id}"
        read_all = "SELECT * FROM wish_list"
        self.cursor.execute(read_all)
        data = self.cursor.fetchall()
        self.cursor.close()
        return data

    def update(self, data, id):
        update_data = f"UPDATE wish_list SET title=%s, price=%s, link=%s, about=%s, done=%s WHERE (id={id})"
        self.cursor.execute(update_data, data)
        self.connect.commit()
        self.cursor.close()

    def delete(self, id):
        delete_data = f"DELETE FROM wish_list WHERE id={id}"
        self.cursor.execute(delete_data)
        self.connect.commit()
        self.cursor.close()



