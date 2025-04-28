import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Insira a cidade: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Buscar Cidade", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Previsão do Tempo")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "cccf11721d8d0e3bdf15422d6e4ecf48"
        city = self.city_input.text()
        url = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?country=BR&token={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["id"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    print("Bad request\nPor favor confira seu input")
                case 401:
                    print("Unauthorized\nAPI Inválida")
                case 403:
                    print("Forbidden\nAcesso Negado")
                case 404:
                    print("Not Found\nCidade Não Encontrada")
                case 500:
                    print("Internal Server Error\nPor favor tente novamente")
                case 502:
                    print("Bad Gateway\nResposta Invalida do servidor")
                case 503:
                    print("Service Unavailable\nServidor caiu")
                case 504:
                    print("Gateway Timeout\nSem resposta do servidor")
                case _:
                    print(f"HTTP error ocorreu\n{http_error}")

        except requests.exceptions.RequestException as req_error:
            print(f"Erro de conexão: {req_error}")

    def display_error(self, message):
        pass

    def display_weather(self, data):
        print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
