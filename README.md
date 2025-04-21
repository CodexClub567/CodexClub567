## Overview

The OML Tools Plugin automates high-quality script generation, fact-checking, audio processing, SEO optimization, and integrates real-time YouTube analytics for our content creation.

## Core Components

-   **Script Generator:** Uses OpenAI (and optionally Gemini) to create chapter-structured scripts.
-   **Fact Checker:** Validates the accuracy of content using external APIs.
-   **Audio Processor:** Converts finalized scripts into audio via ElevenLabs.
-   **SEO Optimizer:** Generates optimized metadata for YouTube uploads.
-   **YouTube Analytics:** Retrieves real-time metrics for continuous improvement.

## Setup

1.  Populate the `backend/.env` file with your API keys.
2.  Install dependencies: `pip install -r backend/requirements.txt`
3.  Run the executor: `python backend/services/special_executor/executor_bot.py`

## Usage

Describe how to use the plugin's features.  For example:

1.  Run the main script.
2.  The script will generate a script, fact-check it, generate audio, and output SEO metadata.
3.  View the results in the console and in the generated audio file.

##  Configuration
Describe any configuration options, such as API keys, voice settings, etc.
## Technical Details

-   Python
-   OpenAI API
-   ElevenLabs API
-   YouTube Data API
-   (Optional) Google Gemini API

## Contributing

Explain how others can contribute to the project.

## License

[LICENSE]

## Contact

ARIFUR RAHMAN CHOWDHURY/learners@codexcreativestudio.com
