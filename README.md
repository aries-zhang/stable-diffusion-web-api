# stable-diffusion-web-api

This is a web app that runs StableDiffusion to generate an image from a text prompt.

NB: this is tested on macOS ONLY.

Run the app

```
make run
```

The model (~5.1GB) is downloaded into `~/.cache/huggingface/hub` by default.

Then call the API with some prompt test, e.g.

```
curl --get \
     --header "Content-Type:application/json" \
     --data-urlencode "prompt=a cat in the gym" \
     --output "./image.png"
     http://localhost:5001
```

It takes around 40s on an M1 MBP to generate the following image, not bad:

![A cat in the gym](image.png)