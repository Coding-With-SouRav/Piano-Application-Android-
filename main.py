import os
from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView


# Number of total keys
TOTAL_KEYS = 61
WHITE_KEYS_COUNT = 31
BLACK_KEYS_COUNT = 30

# Load and sort 61 sound files
SOUNDS_DIR = "sounds"
sound_files = sorted(
    [os.path.join(SOUNDS_DIR, f) for f in os.listdir(SOUNDS_DIR) if f.endswith(".mp3")]
)

if len(sound_files) < TOTAL_KEYS:
    raise Exception(f"Not enough sounds found in '{SOUNDS_DIR}' folder. Required: 61, Found: {len(sound_files)}")

# Preload all sounds once
assigned_sounds = [SoundLoader.load(path) for path in sound_files[:TOTAL_KEYS]]

class PianoKey(Button):
    def __init__(self, sound, color, **kwargs):
        super().__init__(**kwargs)
        self.sound = sound
        self.original_color = color  # Store original color
        self.background_color = color
        self.color = (1, 1, 1, 1) if color == (0, 0, 0, 1) else (0, 0, 0, 1)
        self.font_size = 14
        self.bind(on_press=self.play_sound)
        self.bind(on_press=self.change_color_press)
        self.bind(on_release=self.change_color_release)

    def play_sound(self, *args):
        if self.sound:
            self.sound.seek(0)
            self.sound.play()

    def change_color_press(self, *args):
        if self.original_color == (0, 0, 0, 1):
            self.background_color = (0, 1, 1, 1)  # Cyan

    def change_color_release(self, *args):
        self.background_color = self.original_color

class PianoApp(App):
    def build(self):
        self.black_keys = []

        # Create ScrollView
        scroll_view = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
            scroll_type=['bars', 'content'],
            bar_width=dp(10),
            size_hint=(1, 1),
            scroll_timeout=50,
            scroll_distance=5
        )

        white_key_height = dp(80)
        total_piano_height = white_key_height * WHITE_KEYS_COUNT
        white_key_width = Window.width

        piano_layout = FloatLayout(size_hint=(1, None), height=total_piano_height)
        scroll_view.add_widget(piano_layout)

        black_key_height = white_key_height * 0.6
        black_key_width = white_key_width * 0.3
        black_key_offset = white_key_height * 0.3

        sound_index = 0

        for i in range(WHITE_KEYS_COUNT):
            piano_layout.add_widget(PianoKey(
                sound=assigned_sounds[sound_index],
                color=(1, 1, 1, 1),
                size_hint=(None, None),
                size=(white_key_width, white_key_height),
                pos=(0, i * white_key_height)
            ))
            sound_index += 1

        black_key_pattern = [0, 1, 3, 4, 5]
        for i in range(WHITE_KEYS_COUNT):
            if (i % 7) in black_key_pattern:
                if sound_index >= len(assigned_sounds):
                    break
                y_pos = i * white_key_height + black_key_offset
                key = PianoKey(
                    sound=assigned_sounds[sound_index],
                    color=(0, 0, 0, 1),
                    size_hint=(None, None),
                    size=(black_key_width, black_key_height),
                    pos=(Window.width - black_key_width, y_pos)  # Right side
                )
                piano_layout.add_widget(key)
                self.black_keys.append((key, y_pos, black_key_width))
                sound_index += 1

        Window.bind(on_resize=self.update_black_keys)
        return scroll_view

    def update_black_keys(self, *args):
        for key, y_pos, width in self.black_keys:
            key.pos = (Window.width - width, y_pos)


if __name__ == '__main__':
    PianoApp().run()