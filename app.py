import gradio as gr
from dotenv import load_dotenv
from engine import extract_text, sanitize_text, run_battle

load_dotenv()


def scan(card):
    if card is None:
        return 'Upload an ID first.', ''
    try:
        raw = extract_text(card)
        safe = sanitize_text(raw)
        return safe or 'No non-sensitive text found.', safe
    except Exception as exc:
        return f'OCR failed: {type(exc).__name__}', ''


def battle(portrait, safe_text, style, consent):
    if not consent:
        return 'Owner consent is required.', 'Owner consent is required.'
    if portrait is None:
        return 'Upload a separate portrait image.', 'Upload a separate portrait image.'
    return run_battle(portrait, safe_text, style)


with gr.Blocks(title='AI ID Roast Battle') as demo:
    gr.Markdown('# ⚔️ AI ID Roast Battle')
    gr.Markdown('Upload an ID for OCR, then a **separate portrait** with the owner’s consent. The full ID image is never sent to either LLM. OCR text is filtered before sending.')
    with gr.Row():
        card = gr.Image(label='ID card (local OCR only)', type='pil', sources=['upload', 'webcam'])
        portrait = gr.Image(label='Separate consented portrait (sent to both vision models)', type='pil', sources=['upload', 'webcam'])
    scan_btn = gr.Button('🔎 Scan ID')
    safe_text = gr.Textbox(label='Review safe OCR text (editable)', lines=5)
    stored_safe_text = gr.State('')
    scan_btn.click(scan, inputs=card, outputs=[safe_text, stored_safe_text])
    style = gr.Dropdown(['Friendly', 'Sarcastic', 'Light roast'], value='Light roast', label='Humor style')
    consent = gr.Checkbox(label='I am the ID owner or have their permission to process the portrait and ID details.')
    start = gr.Button('🔥 Start Battle', variant='primary')
    with gr.Row():
        openai_out = gr.Textbox(label='🤖 OpenAI', lines=6)
        qwen_out = gr.Textbox(label='🐉 Qwen', lines=6)
    start.click(battle, inputs=[portrait, safe_text, style, consent], outputs=[openai_out, qwen_out])
    winner = gr.Radio(['OpenAI', 'Qwen', 'Tie'], label='🏆 Who won?')
    gr.Markdown('Privacy note: OCR filtering is heuristic; review and remove any sensitive information before starting the battle. Gradio may create temporary image files; configure deletion and retention appropriately before deployment.')

if __name__ == '__main__':
    demo.launch(share=True)
