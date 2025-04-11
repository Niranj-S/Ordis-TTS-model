# ORDIS using GPT-SoVITS

This project replicates the voice of Warframe's ORDIS using GPT-SoVITS TTS model. The model was trained using just 22 audio clips of 4-5 seconds each and benefits greatly from SoVITS's few shot cloning capabilities. This model can not only capture the robotic, reverberating voice effect of ordis but also can replicate emotional sounds such as laughter. Suitable for enabling realistic voice TTS to LLMs for personal assistants, as the processing speed is faster than real time.

<div align="center"> 
<img src="https://github.com/user-attachments/assets/154d0310-3991-4497-8a0b-3e0abd28f0a1">
</div>

## Comparison

**original**

https://github.com/user-attachments/assets/beeb9e74-cbef-4189-af66-a69762a076f5

**cloned**

https://github.com/user-attachments/assets/2e4fe52d-e67a-4791-8f29-1f2f480e8b27



## More samples

Welcome back operator. How was your day?

https://github.com/user-attachments/assets/b6f6a92f-9bb7-4e5b-a927-0aaee3637c4e

The quick brown fox jumps over the lazy dog

https://github.com/user-attachments/assets/81a86e9c-efc7-407d-ae04-22247b5438b1

Laughter:
Did you hear about the new restaurant on the moon? The food is great, but there's just no atmosphere. haha

https://github.com/user-attachments/assets/727f9d08-ca3f-4a0d-81c5-7ef12e11ba3d

## Model

Download the model weights from [this](https://drive.google.com/drive/folders/1ZV4tcDUlsQsW0Yfl1ocWb5kAMcX1ywyx?usp=sharing) link

## Usage 

- Download and install [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS).
- copy the GPT weights file to GPT_weights_v2 folder.
- copy the SoVITS weights file to SoVITS_weights_v2 folder.
- while running inference webui, select the warframe_ordis-e15.ckpt in the gpt weights drop down and warframe_ordis_e8_s408.pth in sovits weights drop down.
- upload the given reference audio.
- enter inference text and generate.

To run using python, gradio api can be used after launching the webui

```python
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

print(result)
```
VRAM usage ~1.5 GB

Processing time: faster than real time

## Credits

Special thanks to RVC-Boss's [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) project

## License

MIT License

