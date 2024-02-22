from kivy.app import App
from mainwidget import MainWidget
from kivy.lang.builder import Builder

class MainApp(App):
	"""
	Classe com aplicativo
	"""
	def build(self):
		"""
		Método que gera o aplicativo como no widget principal
		"""
		
		self._widget = MainWidget(scan_time=1000,server_ip='127.0.0.1',server_port=502,
		modbus_addrs ={
			'Tensao':1000,
			'Tipo':1001,
			'Endereço':1002,
			'Multiplicador':1003
			},
			db_path="C:\\Users\\55329\\Desktop\\Materias2021-1\\Informatica Industrial\\Trabalho Final\\Trabalho final\\db"
		)
		return self._widget

if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv",encoding="utf-8").read(),rulesonly=True)
    Builder.load_string(open("popups.kv",encoding="utf-8").read(),rulesonly=True)
    MainApp().run()