from kivy.uix.popup import Popup
from kivy.uix.label import Label
#from kivy_garden.graph import LinePlot
from kivy.uix.boxlayout import BoxLayout


class ModbusPopup(Popup):
	"""
	Popup da configuração do protocolo MODBUS
	"""

	#_info_lb = None
#	def __init__(self, server_ip,server_port ,**kwargs):
#		"""
#		Construtor da classe ModbusPopup
#		"""
#		super().__init__(**kwargs)
#		self.ids.txt_ip.text = str(server_ip)
#		self.ids.txt_porta.text = str(server_port)
#
#	def setInfo(self, message):
#		self._info_lb = Label(text=message)
#		self.ids.layout.add_widget(self._info_lb)
#
#	def clearInfo(self):
#		if self._info_lb is not None:
#			self.ids.layout.remove_widget(self._info_lb)

class ScanPopup(Popup):
	"""
	Popup da configuração do tempo de varredura
	"""
	def __init__(self, scantime, **kwargs):
		"""
		Construtor da classe
		"""
		super().__init__(**kwargs)
		self.ids.txt_st.text = str(scantime)