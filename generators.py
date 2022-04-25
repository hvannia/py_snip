# from os import RTLD_LAZY


### redshift cursor w nested generator


class NestedGenerator(object):
    def __init__(self, cursor, itersize):
        self.cursor = cursor
        self.itersize = itersize
        self.last_num = 0
        self.fetch_count = 0
        self.group = []

    def generate_rows(self):
        self.cursor.execute(f"FETCH FORWARD {self.itersize} FROM cursor_name")
        while True:
            try:
                row = self.cursor.fetchone()
                if not row:
                    self.cursor.execute(
                        f"FETCH FORWARD {self.itersize} FROM cursor_name"
                    )
                    row = self.cursor.fetchone()
                if row:
                    self.fetch_count += 1
                yield row
            except StopIteration:
                break

    def gen_groups(self):
        row = self.generate_rows()
        for r in row:
            if r:
                if r.num != self.last_num and self.group != []:
                    self.last_num = r.num
                    yield self.group
                    self.group = [r]
                else:
                    if self.last_num == 0:
                        self.last_num = r.num
                    self.group.append(r)
            else:
                yield self.consolidation
                break

    def run_gen(self):
        QUERY = """DECLARE cursor_name CURSOR FOR 
            SELECT .... """
        a_cursor.execute(QUERY)
        ng = NestedGenerator(a_cursor, 10)
        gc = ng.generate_groups()
        a_cursor.execute("CLOSE cursor_name")
        a_crusor.execute("COMMIT")