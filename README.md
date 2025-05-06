This Kivy-based Python application simulates a vertical piano keyboard with 61 keys (31 white, 30 black). Key features:  
- **Sound Handling**: Loads 61 pre-recorded MP3 files from a `sounds` directory. Each key triggers a unique sound.  
- **Visual Layout**:  
  - White keys are stacked **vertically on the left** as scrollable buttons.  
  - Black keys appear in a **separate column on the right**, positioned slightly higher than their corresponding white keys.  
  - Includes a scrollable interface to navigate the tall keyboard.  
- **Interaction**:  
  - Pressing a black key temporarily changes its color to cyan.  
  - Sounds restart on repeated presses (no overlapping).  
- **Responsive Design**: Adjusts black key positions when the window is resized.  

**Note**: The layout deviates from traditional pianos, with keys arranged in vertical columns instead of an interleaved horizontal pattern.

# Demo Images
![Screenshot 2025-05-06 213135](https://github.com/user-attachments/assets/97a90d5a-6b22-45ec-be3b-86c3e29b8f82)
![Screenshot 2025-05-06 213106](https://github.com/user-attachments/assets/45f3f860-1eef-45be-9893-567905da565c)
![Screenshot 2025-05-06 213157](https://github.com/user-attachments/assets/dbc61a9d-b3bc-4710-8030-768de62e22cb)
