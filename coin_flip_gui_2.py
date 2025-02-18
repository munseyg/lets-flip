import sys
import random
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import Qt

class CoinFlipApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coin Flip App")

        self.heads_count = 0
        self.tails_count = 0

        self.result_label = QLabel("Click 'Flip Coin' to start.")
        self.heads_label = QLabel(f"Heads: {self.heads_count}")
        self.tails_label = QLabel(f"Tails: {self.tails_count}")
        self.heads_percentage_label = QLabel("Heads Percentage: 0.00%")
        self.tails_percentage_label = QLabel("Tails Percentage: 0.00%")

        flip_button = QPushButton("Flip Coin")
        flip_button.clicked.connect(self.flip_coin)

        v_layout = QVBoxLayout()  # Main vertical layout
        v_layout.addWidget(self.result_label)
        v_layout.addWidget(self.heads_label)
        v_layout.addWidget(self.tails_label)
        v_layout.addWidget(self.heads_percentage_label)
        v_layout.addWidget(self.tails_percentage_label)
        v_layout.addWidget(flip_button)

        self.setLayout(v_layout)

    def flip_coin(self):
        result = random.choice(["Heads", "Tails"])
        self.result_label.setText(f"The coin flip resulted in: {result}")

        if result == "Heads":
            self.heads_count += 1
        else:
            self.tails_count += 1

        total_flips = self.heads_count + self.tails_count

        heads_percentage = (self.heads_count / total_flips) * 100 if total_flips > 0 else 0
        tails_percentage = (self.tails_count / total_flips) * 100 if total_flips > 0 else 0

        self.heads_label.setText(f"Heads: {self.heads_count}")
        self.tails_label.setText(f"Tails: {self.tails_count}")
        self.heads_percentage_label.setText(f"Heads Percentage: {heads_percentage:.2f}%")
        self.tails_percentage_label.setText(f"Tails Percentage: {tails_percentage:.2f}%")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoinFlipApp()
    window.show()
    sys.exit(app.exec())