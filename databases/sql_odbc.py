"""

    SQL Server Helper functions using pypyodbc:
    https://pypi.python.org/pypi/pypyodbc
    > pip install pypyodbc

    @author: Alex Bugrimenko
"""
import sys
import pypyodbc as sql

# driver = '{SQL Server Native Client 10.0}'
_SQL_CONNSTR_TEST_ = 'Driver={SQL Server};Server=localhost\SQL2014E;Database=temp;uid=test;pwd=test;'


# ---- test ----
def test_read(con_string):
    assert con_string, "Connection string is required"
    err = ''
    data = []
    con = sql.connect(con_string)
    try:
        cursor = con.cursor()
        sqlcmd = 'select top 10 * from users'
        cursor.execute(sqlcmd)
        result = cursor.fetchone()
        while result:
            data.extend(result)
            result = cursor.fetchone()
    except:
        err = sys.exc_info()
    con.close()
    return err, data


def test_write(con_string, id=2, email='a.b@abc.com'):
    assert con_string, "Connection string is required"
    err = ''
    con = sql.connect(con_string)
    try:
        cursor = con.cursor()
        sqlcmd = "update users set email=? where id=?"
        values = [email, id]
        cursor.execute(sqlcmd, values)
        con.commit()
    except:
        con.rollback()
        err = sys.exc_info()
    con.close()
    return err


if __name__ == "__main__":
    # print("~~~ There is no Main method defined. ~~~")

    # tests: write
    e = test_write(_SQL_CONNSTR_TEST_)
    if e == '':
        print('--- Status: OK')
    else:
        print('--- ERROR:', e)

    # tests: read
    e, d = test_read(_SQL_CONNSTR_TEST_)
    if e == '':
        print('--- Status: OK')
    else:
        print('--- ERROR:', e)
    print('--- Data ---')
    print(d)
