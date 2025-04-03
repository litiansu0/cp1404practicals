from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Chalice", "David", "Eve"]

    def build(self):
        self.title = "Dynamic Labels Demo"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """动态创建标签并添加到布局"""
        for name in self.names:
            label = Label(
                text=name,
                font_size='20sp',
                color=(0.2, 0.6, 1, 1),
                size_hint_y=None,
                height=40
            )
            self.root.ids.labels_container.add_widget(label)

DynamicLabelsApp().run()