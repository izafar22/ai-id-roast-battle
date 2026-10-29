# ⚔️ AI ID Roast Battle

A playful **Gradio** app where **OpenAI** and **Qwen** compete to write the wittiest introduction based on non-sensitive text extracted from an ID card and a **separately supplied portrait**.

> **Privacy first:** Only upload your own ID and portrait, or material you have the owner's permission to process. The app runs OCR locally and does **not** send the full ID card to the LLMs. It sends the separately uploaded portrait and the OCR text you review. Do not include ID numbers, dates of birth, home addresses, or other sensitive information.

## ✨ Features

- 📷 Upload or capture an ID image using Gradio.
- 🔎 Extract printed text locally using **EasyOCR**.
- 🛡️ Apply basic filtering to OCR results, then **review and edit** the text before sending it.
- 🖼️ Upload a separate, consented portrait for visual analysis.
- 🔥 Click **Start Battle** to query **OpenAI** and **Qwen** concurrently with the same prompt, portrait, and reviewed OCR text.
- 🎭 Choose a humor style: **Friendly**, **Sarcastic**, or **Light roast**.
- 🏆 Compare responses side by side and select a winner (the selection is not persisted).

## 🏗️ How it works

```text
ID card image ──> EasyOCR (local) ──> filtered, editable text ──┐
                                                                │
Separate portrait (with consent) ────────────────────────────────┤
                                                                ▼
                                                       Start Battle
                                                        /         \
                                                 OpenAI Vision   Qwen Vision
                                                        \         /
                                                 Side-by-side replies
                                                        │
                                                   Vote for winner
```

## 🧰 Tech stack

- Python
- [Gradio](https://www.gradio.app/) — web UI
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) — text extraction
- [OpenAI Python SDK](https://github.com/openai/openai-python) — OpenAI API and OpenAI-compatible Qwen API
- Pillow and NumPy — image processing
- python-dotenv — local environment configuration

## 🚀 Run locally

**Prerequisites:** Python 3.10+ (use a supported Python version for your platform), access to an OpenAI vision-capable model, and access to a Qwen vision-capable model via an OpenAI-compatible endpoint.

1. Clone your repository and open its folder:

   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-id-battle.git
   cd ai-id-battle
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Copy the example configuration:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and supply **your own** credentials and supported model IDs:

   ```dotenv
   OPENAI_API_KEY=your_openai_key
   OPENAI_MODEL=gpt-4.1-mini

   QWEN_API_KEY=your_qwen_provider_key
   QWEN_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1
   QWEN_MODEL=qwen-vl-max
   ```

   The Qwen URL shown is an example for a compatible provider endpoint; use the endpoint appropriate for your account and region. Model availability and pricing vary by provider.

5. Start Gradio:

   ```bash
   python app.py
   ```

6. Open the local address printed in the terminal (typically `http://127.0.0.1:7860`). The first OCR run may download EasyOCR model weights.

## 🎮 Using the app

1. Upload an ID image in **ID card (local OCR only)**.
2. Click **Scan ID**.
3. Inspect the **editable OCR text** and remove any personal or sensitive information that the automatic filter missed.
4. Upload a **separate portrait** that the owner has agreed to share with the two model providers.
5. Select a humor style and check the consent box.
6. Click **🔥 Start Battle**.
7. Compare the two responses and choose **OpenAI**, **Qwen**, or **Tie**.

## 🔒 Privacy and security

- **Do not commit `.env`**. Add it to `.gitignore`, and rotate keys immediately if they were ever exposed.
- The OCR filter is **heuristic, not guaranteed** to remove every sensitive field. Always manually review the text before starting the battle.
- The separate portrait **is sent to both configured model providers**; the full ID image is not sent by the current battle flow.
- Avoid real government ID images in public demos. Prefer synthetic or redacted sample cards.
- Before deploying publicly, add upload limits, abuse protection, API spending limits, and a clear data retention/deletion policy. Gradio may create temporary files.
- This project is for consensual, lighthearted entertainment—not identity verification, profiling, or consequential decisions.

## 📁 Project files

```text
ai-id-battle/
├── app.py             # Gradio interface and user interactions
├── engine.py          # OCR, filtering, prompts, and concurrent model calls
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variable template (safe to commit)
├── .gitignore         # Local secrets and generated files excluded from Git
└── README.md          # Project documentation
```

## 🛠️ Troubleshooting

**`ModuleNotFoundError` when scanning:** Ensure dependencies are installed into the same Python environment used to run `app.py`:

```bash
python -m pip install -r requirements.txt
python -c "import easyocr; print('EasyOCR ready')"
```

**One model fails:** Verify its API key, endpoint, account access, and model ID in `.env`. Both models must support image input.

**OCR result is inaccurate:** Improve image sharpness and lighting, then correct the editable text manually before starting the battle.

## 📌 Roadmap

- [ ] Automatic portrait cropping from a locally processed ID, with reliable redaction
- [ ] Streaming model responses
- [ ] Persisted vote counts and battle history without storing ID data
- [ ] Public deployment with privacy and cost safeguards

---

Made for fun: **two models, one portrait, one battle.**
