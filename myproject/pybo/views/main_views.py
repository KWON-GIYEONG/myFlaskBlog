# --------------------------------- [edit] ---------------------------------- #
from flask import Blueprint
from pybo.module.dbModule import Database

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    db = Database()
    sql = """
    CREATE TABLE blog_post(
        post_index int NOT NULL AUTO_INCREMENT,
        post_title varchar(45) NOT NULL,
        post_content varchar(255) NOT NULL,
        post_created_time datetime NOT NULL,
        post_author varchar(45) NOT NULL,
        PRIMARY KEY(post_index)
    )   
     """

    db.executeAll(sql)

    return 'Pybo index'
# --------------------------------------------------------------------------- #
