from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'width', 450)
Config.set('graphics', 'height', 900)
from kivy.uix.widget import Widget
from kivy.graphics import Line, Rectangle, Color
from kivy.core.window import Window
import numpy as np
import math

from kivy.uix.label import Label

from tensorflow import keras

model = keras.models.load_model('digit_recognition_model')


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        self.x_size = Window.size[0]
        self.y_size = Window.size[1] / 2

        self.pixels_binary = np.zeros((28, 28))

        self.lbl = Label(size=(Window.width, Window.height / 2), font_size=300, markup=True)
        self.add_widget(self.lbl)

        self.lbltwo = Label(size=(Window.width / 5, 30), font_size=25, markup=True, pos=(150, 16))
        self.add_widget(self.lbltwo)

        self.lblnumber = Label(size=(Window.width / 5, Window.height / 10), font_size=25, markup=True, pos=(65, 370))
        self.add_widget(self.lblnumber)

        self.lblprobability = Label(size=(Window.width / 5, 30), font_size=25, markup=True, pos=(35, 16))
        self.add_widget(self.lblprobability)

        with self.canvas:
            Color(0.3, 0.3, 0.3, 1, mode='rgba')
            Line(points=(0, Window.height / 2, Window.width, Window.height / 2))

    def on_touch_down(self, touch):
        x_value = math.floor(touch.pos[0] / 16.07142857)
        y_value = math.floor((touch.pos[1] - 450) / 16.07142857)

        if Window.size[1] / 2 < touch.pos[1] < Window.size[1]:
            with self.canvas:
                Color(1, 1, 1, 1, mode='rgba')
                self.rect = Rectangle(pos=(16.07142857 * x_value, (16.07142857 * y_value) + 450),
                                      size=(self.x_size / 28, self.y_size / 28))

                self.pixels_binary[x_value][y_value] = 1.0

                drawNeighbors(self, x_value, y_value)

        elif Window.size[1] / 2 > touch.pos[1] >= 0:
            with self.canvas:
                Color(0, 0, 0, 1, mode='rgba')

                self.rect = Rectangle(pos=(0, 450), size=(450, 450))

            self.pixels_binary = np.zeros((28, 28))

            self.lbl.text = ''
            self.lbltwo.text = ''

            self.lblnumber.text = ''
            self.lblprobability.text = ''

    def on_touch_move(self, touch):
        x_value = math.floor(touch.pos[0] / 16.07142857)
        y_value = math.floor((touch.pos[1] - 450) / 16.07142857)

        if Window.size[1] / 2 < touch.pos[1] < Window.size[1]:
            with self.canvas:
                Color(1, 1, 1, 1, mode='rgba')
                self.rect = Rectangle(pos=(16.07142857 * x_value, (16.07142857 * y_value) + 450),
                                      size=(self.x_size / 28, self.y_size / 28))

                self.pixels_binary[x_value][y_value] = 1.0

                drawNeighbors(self, x_value, y_value)

    def on_touch_up(self, touch):
        if touch.pos[1] > Window.size[1] / 2:
            self.pixels_binary = np.rot90(self.pixels_binary, k=3, axes=(1, 0))

            class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            prediction = model.predict([[self.pixels_binary]])

            self.lbl.text = f'[color=ffffff]{class_names[np.argmax(prediction)]}[/color]'
            self.lbltwo.text = f'{(prediction[0][np.argmax(prediction)] * 100)}'[:5] + '%'
            self.lblnumber.text = 'Detected number:'
            self.lblprobability.text = 'Confidence:'

            self.pixels_binary = np.rot90(self.pixels_binary, k=1, axes=(1, 0))


def drawNeighbors(self, x_value, y_value):
    # Left
    if x_value > 0:
        self.rect = Rectangle(pos=(16.07142857 * x_value - 16.07142857, (16.07142857 * y_value) + 450),
                              size=(self.x_size / 28, self.y_size / 28))
        self.pixels_binary[x_value - 1][y_value] = 1.0

    # Top
    if y_value < 27:
        self.rect = Rectangle(pos=(16.07142857 * x_value, (16.07142857 * y_value) + 450 + 16.07142857),
                              size=(self.x_size / 28, self.y_size / 28))
        self.pixels_binary[x_value][y_value + 1] = 1.0

    # Top left
    if y_value < 27 and x_value > 0:
        if y_value < 27:
            self.rect = Rectangle(
                pos=(16.07142857 * x_value - 16.07142857, (16.07142857 * y_value) + 450 + 16.07142857),
                size=(self.x_size / 28, self.y_size / 28))
            self.pixels_binary[x_value - 1][y_value + 1] = 1.0


class MyApp(App):
    def build(self):
        return Touch()
