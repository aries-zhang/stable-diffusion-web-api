from flask import Flask, request, send_file
from flask_cors import CORS
import io
import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16
).to("mps")

# https://huggingface.co/docs/diffusers/v0.6.0/en/optimization/mps
def run_inference(prompt):
    # First-time "warmup" pass (see explanation above)
    _ = pipe(prompt, num_inference_steps=1)

    # Results match those from the CPU device after the warmup pass.
    image = pipe(prompt).images[0]
    img_data = io.BytesIO()
    image.save(img_data, "PNG")
    img_data.seek(0)
    return img_data

app = Flask(__name__)

@app.route("/")
def get():
    prompt = request.args["prompt"]
    image_data = run_inference(prompt)
    return send_file(image_data, mimetype='image/png')