from gradio_client import Client, file

# Create client
client = Client("http://0.0.0.0:9872/")

# Load So-VITS weights
client.predict(
    sovits_path="SoVITS_weights_v2/warframe_ordis_e8_s408.pth",
    prompt_language="English",
    text_language="English",
    api_name="/change_sovits_weights"
)

# Load GPT weights
client.predict(
    gpt_path="GPT_weights_v2/warframe_ordis-e15.ckpt",
    api_name="/change_gpt_weights"
)

# Define text for inference
inference_text = "Operator, I've run diagnostic regressions..."

# Run voice inference
result = client.predict(
    ref_wav_path=file('ordis.ogg'),
    prompt_text=inference_text,
    prompt_language="English",
    text=inference_text,
    text_language="English",
    how_to_cut="Slice by English punct",
    top_k=15,
    top_p=1,
    temperature=0.7,
    ref_free=False,
    speed=1,
    if_freeze=False,
    inp_refs=None,
    api_name="/get_tts_wav"
)

print(result) # you can use pydub/pygame etc to play the output wav file from it's path
