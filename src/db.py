from .table import Table

class Database():

    def __init__(self):
        self.tables = []
        # Only goes up, starting from 1. 0 reps none
        self.next_rid = 1
        
        pass

    def open(self):
        pass

    def close(self):
        pass

    """
    # Creates a new table
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """
    def create_table(self, name, num_columns, key):
        table = Table(name, num_columns, key)
        return table

    """
    # Deletes the specified table
    """
    def drop_table(self, name):
        pass

    def _get_rid(self):
        self.next_rid += 1
        return self.next_rid