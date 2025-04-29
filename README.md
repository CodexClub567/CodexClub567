# OML Tools Plugin

The **OML Tools Plugin** is an all-in-one solution for automating high-quality content creation. It offers script generation, fact-checking, audio processing, SEO optimization, and real-time YouTube analytics integration to streamline your workflow.

## 🚀 Features

- **Script Generator**  
  Leverages OpenAI (and optionally Gemini) to produce chapter-structured scripts for your projects.

- **Fact Checker**  
  Ensures the accuracy of content by validating information through external APIs.

- **Audio Processor**  
  Converts finalized scripts into professional-grade audio using the ElevenLabs API.

- **SEO Optimizer**  
  Generates optimized metadata for YouTube uploads, ensuring higher discoverability.

- **YouTube Analytics**  
  Fetches real-time metrics for continuous content improvement and strategy refinement.

---

## 🛠️ Setup

Follow these steps to get started:

1. **Configure Environment Variables**  
   Populate the `backend/.env` file with your API keys for services like OpenAI, ElevenLabs, and YouTube Data API.

2. **Install Dependencies**  
   Run the following command to install all required Python packages:  
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Run the Executor**  
   Start the main execution bot:  
   ```bash
   python backend/services/special_executor/executor_bot.py
   ```

---

## 📖 Usage

1. Execute the main script to initiate the process.  
   ```bash
   python backend/services/special_executor/executor_bot.py
   ```
2. The plugin will generate:  
   - A structured script  
   - Fact-checked content  
   - Audio output  
   - SEO metadata
3. View the results in the console and retrieve the generated audio file.

---

## ⚙️ Configuration

Customize the following options to suit your needs:

- **API Keys**: Add required keys for OpenAI, ElevenLabs, YouTube Data API, and optionally Google Gemini in the `.env` file.
- **Voice Settings**: Configure voice settings for the audio processor in the `backend/settings` directory.
- **Output Formats**: Specify output file formats and directories for scripts, audio, and SEO metadata.

---

## 🛠️ Technical Details

The OML Tools Plugin is built with the following technologies:

- **Python**  
- **OpenAI API**  
- **ElevenLabs API**  
- **YouTube Data API**  
- *(Optional)* **Google Gemini API**

---

## 🤝 Contributing

We welcome contributions to improve and expand the OML Tools Plugin! Follow these steps to contribute:  

1. Fork the repository.  
2. Create a new branch for your feature or bug fix.  
3. Commit your changes and push them to your fork.  
4. Submit a pull request for review.

For major changes, please open an issue to discuss your proposal first.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For inquiries or support, feel free to reach out:

**Arifur Rahman Chowdhury**  
[learners@codexcreativestudio.com](mailto:learners@codexcreativestudio.com)

---
```

You can copy and paste this into your editor to replace the existing content in the `README.md` file. Let me know if you need further assistance!
