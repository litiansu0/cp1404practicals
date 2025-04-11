from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.609344  # Conversion factor for miles to kilometers

class MilesToKmApp(App):
    def build(self):
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.miles = 0.0  
        return self.root

    def update_km_from_input(self):
        try:
            self.miles = float(self.root.ids.input_miles.text)
        except ValueError:
            self.miles = 0.0
        self._update_output()

    def increment_miles(self, delta):
        try:
            current_value = float(self.root.ids.input_miles.text)
        except ValueError:
            current_value = 0.0
        self.miles = current_value + delta
        self.root.ids.input_miles.text = f"{self.miles}"
        self._update_output()

    def _update_output(self):
        km_value = self.miles * MILES_TO_KM
        self.root.ids.output_km.text = f"{km_value:.5f}" if self.miles != 0 else "0.0"

if __name__ == "__main__":
    MilesToKmApp().run()