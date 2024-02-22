
from kivy.uix.boxlayout import BoxLayout
from popups import ModbusPopup ,ScanPopup #DataGraphPopup, HistGraphPopup
from pyModbusTCP.client import ModbusClient
from kivy.core.window import Window
from threading import Thread
from time import sleep
from datetime import datetime
import random
#from timeseriesgraph import TimeSeriesGraph
from bdhandler import BDHandler
#from kivy_garden.graph import LinePlot

class MainWidget(BoxLayout):

	"""
	Widget principal da aplicação
	"""
	_updateThread = None
	_updateWidgets = True
	_tags = {}
	_max_points = 20

	def __init__(self, **kwargs):
		"""
		Construtor do widget principal
		"""
		super().__init__()
		self._scan_time = kwargs.get('scan_time')
		self._serverIP = kwargs.get('server_ip')
		self._serverPort = kwargs.get('server_port')
		self._modbusPopup = ModbusPopup(self._serverIP, self._serverPort)
		self._scanPopup = ScanPopup(self._scan_time)
		self._modbusClient = ModbusClient(host=self._serverIP, port=self._serverPort)
		self._meas = {}
		self._meas['timestamp'] = None
		self._meas['values'] = {}

	def startDataRead(self, ip, port):
		"""
		Método utilizado para a configuração do IP e porta do servidor MODBUS e
		inicializar uma thread para a leitura dos dados e a tualização da interface
		gráfica
		"""
		self._serverIP = ip
		self._serverPort = port
		self._modbusClient.host = self._serverIP
		self._modbusClient.port = self._serverPort
		try:
			Window.set_system_cursor("wait")
			self._modbusClient.open() 
			Window.set_system_cursor("arrow")
			if self._modbusClient.is_open():
				self._updateThread = Thread(target=self.updater)
				self._updateThread.start()
				self.ids.img_con.source = 'imgs/conectado.png'
				self._modbusPopup.dismiss()
			else:
				self._modbusPopup.setInfo("Falha na conexão com servidor")
		except Exception as e:
			print("Erro: ", e.args)
