import web
import json
import model
        
urls = (
	'/','Index',
    '/agregar', 'Agregar',
    '/modify/(\d+)', 'Modify',
    '/view/(\d+)', 'View'
)

app = web.application(urls, globals())
render = web.template.render('templates', base='master')
web.config.debug = False

class Index:        
    def GET(self):
        productos = model.get_products()
        return render.index(productos)

class View():
    def GET(self, id):
        id = int(id)
        producto = model.get_product(id)
        return render.view(producto)

class Modify():
    def GET(self, id):
        id = int(id)
        producto = model.get_product(id)
        return render.edit(producto)
    def POST(self):
        #id = int(id)
        form = web.input()
        imagen = web.input(imagen={})
        filedir = 'static/img'
        filepath =imagen.imagen.filename.replace('\\','/')
        filename = filepath.split('/')[-1]

        fout = open(filedir + '/' + filename,'w')
        fout.write(imagen.imagen.file.read())
        fout.close()
        imagen=filename 

        model.modify(
            form['producto'],
            form['descripcion'],
            form['existencias'],
            form['p_compra'],
            form['p_venta'],
            imagen
            )
        raise web.seeother('/')
        return render.index()
        
    
        

class Agregar():
    def GET(self):
        """encode = model.get_products()"""
        return render.insert()
        """return json.dumps(encode)"""
    def POST(self):
        form = web.input()
        imagen = web.input(imagen={})
        filedir = 'static/img'
        filepath =imagen.imagen.filename.replace('\\','/')
        filename = filepath.split('/')[-1]

        fout = open(filedir + '/' + filename,'w')
        fout.write(imagen.imagen.file.read())
        fout.close()
        imagen=filename 

        model.insert(
            form['producto'],
            form['descripcion'],
            form['existencias'],
            form['p_compra'],
            form['p_venta'],
            imagen
            )
        raise web.seeother('/')
        return render.index()

if __name__ == "__main__":
    app.run()