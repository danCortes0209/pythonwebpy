import web

db_host = 'localhost'
db_name = 'products'
db_user = 'root'
db_pw = 'Vaneamor'

db = web.database(
			dbn='mysql',
			host=db_host,
			db=db_name,
			user=db_user,
			pw=db_pw			
			)

def get_products():
	return db.select('productos')

def get_product(id):
    try:
        return db.select('productos', where='id=$id', vars=locals())#[0]
    except IndexError:
        return None

def insert(producto, descripcion, existencias, p_compra, p_venta, imagen):
	db.insert('productos', producto=producto, descripcion=descripcion, existencias=existencias, p_compra=p_compra, p_venta=p_venta, imagen=imagen)

def modify(id, producto, descripcion, existencias, p_compra, p_venta, imagen):
	try:
		db.update('productos', where='id=$id', producto=producto, descripcion=descripcion, existencias=existencias, p_compra=p_compra, p_venta=p_venta, imagen=imagen)
	except Exception as e:
		return e
