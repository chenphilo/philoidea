import sys
import time
import requests
import pytz
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer, QPoint


class BitcoinPriceWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 记录程序启动时间
        self.start_time = time.time()

        # 设置窗口属性
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 透明背景
        self.setStyleSheet("background-color: rgba(0, 0, 0, 180); border-radius: 10px;")

        # 创建标签
        self.time_label = QLabel("东京时间: Loading...", self)
        self.time_label.setStyleSheet("color: white; font-size: 14px; font-weight: bold; padding: 5px;")

        self.uptime_label = QLabel("已学习 00:00:00", self)
        self.uptime_label.setStyleSheet("color: white; font-size: 14px; font-weight: bold; padding: 5px;")

        self.price_label = QLabel("Loading...", self)
        self.price_label.setStyleSheet("color: white; font-size: 18px; font-weight: bold; padding: 5px;")

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.uptime_label)
        layout.addWidget(self.price_label)
        self.setLayout(layout)

        self.resize(250, 140)  # 调整窗口大小

        # 定时器：每 1 秒更新时间
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(1000)  # 每 1 秒更新

        # 定时器：每 30 秒更新价格
        self.price_timer = QTimer(self)
        self.price_timer.timeout.connect(self.update_price)
        self.price_timer.start(30000)  # 每 30 秒更新价格

        self.last_price = "Loading..."
        self.update_time()  # 立即更新时间
        self.update_price()  # 立即更新价格

        # 初始化拖动相关变量
        self.dragging = False
        self.drag_start_position = QPoint()

    def update_time(self):
        """每秒更新东京时间和学习时间"""
        # 更新时间
        tokyo_time = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.setText(f"东京时间: {tokyo_time}")

        # 计算程序运行时间
        uptime_seconds = int(time.time() - self.start_time)
        uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
        self.uptime_label.setText(f"已学习 {uptime_str}")

    def fetch_price_from_coingecko(self):
        """尝试从 CoinGecko 获取价格"""
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,bitcoin-cash&vs_currencies=usd,jpy"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "btc_usd": data["bitcoin"]["usd"],
            "btc_jpy": data["bitcoin"]["jpy"],
            "bch_usd": data["bitcoin-cash"]["usd"],
            "bch_jpy": data["bitcoin-cash"]["jpy"]
        }

    def fetch_price_from_coincap(self):
        """备用方案：尝试从 CoinCap 获取价格"""
        btc_response = requests.get("https://api.coincap.io/v2/assets/bitcoin", timeout=5)
        bch_response = requests.get("https://api.coincap.io/v2/assets/bitcoin-cash", timeout=5)

        btc_response.raise_for_status()
        bch_response.raise_for_status()

        btc_data = btc_response.json()
        bch_data = bch_response.json()

        # 由于 CoinCap 没有直接提供 JPY 价格，我们需要手动换算
        jpy_rate = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()["rates"]["JPY"]

        return {
            "btc_usd": float(btc_data["data"]["priceUsd"]),
            "btc_jpy": float(btc_data["data"]["priceUsd"]) * jpy_rate,
            "bch_usd": float(bch_data["data"]["priceUsd"]),
            "bch_jpy": float(bch_data["data"]["priceUsd"]) * jpy_rate
        }

    def update_price(self):
        """每 30 秒更新价格"""
        try:
            try:
                prices = self.fetch_price_from_coingecko()
            except requests.exceptions.RequestException:
                prices = self.fetch_price_from_coincap()

            btc_usd = prices["btc_usd"]
            btc_jpy = prices["btc_jpy"]
            bch_usd = prices["bch_usd"]
            bch_jpy = prices["bch_jpy"]

            self.last_price = f"BTC: ${btc_usd:.2f}\nBTC: ¥{btc_jpy:.2f}\nBCH: ${bch_usd:.2f}\nBCH: ¥{bch_jpy:.2f}"
        except requests.exceptions.RequestException:
            self.last_price += "\n(API Error, using last price)"

        self.price_label.setText(self.last_price)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.drag_start_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = BitcoinPriceWidget()
    widget.show()
    sys.exit(app.exec())
