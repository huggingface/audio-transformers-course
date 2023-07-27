# Load and explore an audio dataset

In this course we will use the 🤗 Datasets library to work with audio datasets. 🤗 Datasets is an open-source library for
downloading and preparing datasets from all modalities including audio. The library offers easy access to an unparalleled
selection of machine learning datasets publicly available on Hugging Face Hub. Moreover, 🤗 Datasets includes multiple
features tailored to audio datasets that simplify working with such datasets for both researchers and practitioners.

To begin working with audio datasets, make sure you have the 🤗 Datasets library installed:

```bash
pip install datasets[audio]
```

One of the key defining features of 🤗 Datasets is the ability to download and prepare a dataset in just one line of
Python code using the `load_dataset()` function.

Let's load and explore and audio dataset called [MINDS-14](https://huggingface.co/datasets/PolyAI/minds14), which contains
recordings of people asking an e-banking system questions in several languages and dialects.

To load the MINDS-14 dataset, we need to copy the dataset's identifier on the Hub (`PolyAI/minds14`) and pass it
to the `load_dataset` function. We'll also specify that we're only interested in the Australian subset (`en-AU`) of
the data, and limit it to the training split:

```py
from datasets import load_dataset

minds = load_dataset("PolyAI/minds14", name="en-AU", split="train")
minds
```

**Output:**
```out
Dataset(
    {
        features: [
            "path",
            "audio",
            "transcription",
            "english_transcription",
            "intent_class",
            "lang_id",
        ],
        num_rows: 654,
    }
)
```

The dataset contains 654 audio files, each of which is accompanied by a transcription, an English translation, and a label
indicating the intent behind the person's query. The audio column contains the raw audio data. Let's take a closer look
at one of the examples:

```py
example = minds[0]
example
```

**Output:**
```out
{
    "path": "/root/.cache/huggingface/datasets/downloads/extracted/f14948e0e84be638dd7943ac36518a4cf3324e8b7aa331c5ab11541518e9368c/en-AU~PAY_BILL/response_4.wav",
    "audio": {
        "path": "/root/.cache/huggingface/datasets/downloads/extracted/f14948e0e84be638dd7943ac36518a4cf3324e8b7aa331c5ab11541518e9368c/en-AU~PAY_BILL/response_4.wav",
        "array": array(
            [0.0, 0.00024414, -0.00024414, ..., -0.00024414, 0.00024414, 0.0012207],
            dtype=float32,
        ),
        "sampling_rate": 8000,
    },
    "transcription": "I would like to pay my electricity bill using my card can you please assist",
    "english_transcription": "I would like to pay my electricity bill using my card can you please assist",
    "intent_class": 13,
    "lang_id": 2,
}
```

You may notice that the audio column contains several features. Here's what they are:
* `path`: the path to the audio file (`*.wav` in this case).
* `array`: The decoded audio data, represented as a 1-dimensional NumPy array.
* `sampling_rate`. The sampling rate of the audio file (8,000 Hz in this example).

The `intent_class` is a classification category of the audio recording. To convert this number into a meaningful string,
we can use the `int2str()` method:

```py
id2label = minds.features["intent_class"].int2str
id2label(example["intent_class"])
```

**Output:**
```out
"pay_bill"
```

If you look at the transcription feature, you can see that the audio file indeed has recorded a person asking a question
about paying a bill.

If you plan to train an audio classifier on this subset of data, you may not necessarily need all of the features. For example,
the `lang_id` is going to have the same value for all examples, and won't be useful. The `english_transcription` will likely
duplicate the `transcription` in this subset, so we can safely remove them.

You can easily remove irrelevant features using 🤗 Datasets' `remove_columns` method:

```py
columns_to_remove = ["lang_id", "english_transcription"]
minds = minds.remove_columns(columns_to_remove)
minds
```

**Output:**
```out
Dataset({features: ["path", "audio", "transcription", "intent_class"], num_rows: 654})
```

Now that we've loaded and inspected the raw contents of the dataset, let's listen to a few examples! We'll use the `Blocks`
and `Audio` features from `Gradio` to decode a few random samples from the dataset:

```py
import gradio as gr


def generate_audio():
    example = minds.shuffle()[0]
    audio = example["audio"]
    return (
        audio["sampling_rate"],
        audio["array"],
    ), id2label(example["intent_class"])


with gr.Blocks() as demo:
    with gr.Column():
        for _ in range(4):
            audio, label = generate_audio()
            output = gr.Audio(audio, label=label)

demo.launch(debug=True)
```

If you'd like to, you can also visualize some of the examples. Let's plot the waveform for the first example.

```py
import librosa
import matplotlib.pyplot as plt
import librosa.display

array = example["audio"]["array"]
sampling_rate = example["audio"]["sampling_rate"]

plt.figure().set_figwidth(12)
librosa.display.waveshow(array, sr=sampling_rate)
```

<div class="flex justify-center">
    <img src="https://huggingface.co/datasets/huggingface-course/audio-course-images/resolve/main/waveform_unit1.png" alt="Waveform plot">
</div>

Try it out! Download another dialect or language of the MINDS-14 dataset, listen and visualize some examples to get a sense
of the variation in the whole dataset. You can find the full list of available languages [here](https://huggingface.co/datasets/PolyAI/minds14).