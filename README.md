# Audio to Text Transcription App

This small Python app uses OpenAI's Whisper model to transcribe audio files to text. It converts audio to mono and 16kHz before processing and returns the transcription. The app supports various audio formats and ensures the file is optimized for transcription.


## Project Structure

```bash
├── README.md
├── assets
│   ├── harvard.wav
│   └── jackhammer.wav
└── audio-to-text.py
```
**Note**: A `.env` **Note**: A `.env` file is used to store the OpenAI API key and is not included in this repository for security reasons.

## Requirements

- Python 3.7+
- [OpenAI Python package](https://pypi.org/project/openai/)
- [pydub](https://pypi.org/project/pydub/)
- FFmpeg (required by `pydub` for audio processing)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ivansing/audio-to-text-app.git
    cd audio-to-text-app
```

2. Install dependencies:
```bash
pip install openai pydub python-dotenv
```

3. Install FFmpeg:
   - On macOS (using Homebrew): `brew install ffmpeg`
   - On Ubuntu: `sudo apt install ffmpeg`
   - On Windows: Download and install from [ffmpeg.org](https://ffmpeg.org/download.html)

4. Set up your OpenAI API key:
    - Create a `.env` file at the root of the project and add your API key:
      ```
      OPENAI_API_KEY=your-api-key-here
      ```

## Usage

1. Add your aduio file to the `assets` directory or use the provided samples wav files (e.g., `jackhammer.wav`).

2. Run the `audio-to-text.py`script to convert and transcribre your aduio file:

```bash
python3 audio-to-text.py
```

3. The transcription will be prited in the console.

## How it works

1. **Convert Audio**: The script first converts the input audio file to mono and resamples it to 16kHz using `pydub`.
2. **Transcription**: It then sends the processed audio to OpenAI's Whisper model for transcription.
3. **Output**: The transcribed text is printed.

## License

This project is licensed under the MIT License.

## Acknoledgements

- [OpenAI Whisper API](https://openai.com/index/whisper/)
- [pydub](https://github.com/jiaaro/pydub)

