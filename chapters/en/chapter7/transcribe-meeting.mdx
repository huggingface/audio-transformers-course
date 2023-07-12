# Transcribe a meeting

In this final section, we'll use the Whisper model to generate a transcription for a conversation or meeting between 
two or more speakers. We'll then pair it with a *speaker diarization* model to predict "who spoke when". By matching
the timestamps from the Whisper transcriptions with the timestamps from the speaker diarization model, we can predict an 
end-to-end meeting transcription with fully formatted start / end times for each speaker. This is a basic version of 
the meeting transcription services you might have seen online from the likes of [Otter.ai](https://otter.ai) and co:

<div class="flex justify-center">
     <img src="https://huggingface.co/datasets/huggingface-course/audio-course-images/resolve/main/diarization_transcription.png">
 </div>

## Speaker Diarization

Speaker diarization (or diarisation) is the task of taking an unlabelled audio input and predicting "who spoke when".
In doing so, we can predict start / end timestamps for each speaker turn, corresponding to when each speaker starts 
speaking and when they finish.

🤗 Transformers currently does not have a model for speaker diarization included in the library, but there are checkpoints 
on the Hub that can be used with relative ease. In this example, we'll use the pre-trained speaker diarization model from 
[pyannote.audio](https://github.com/pyannote/pyannote-audio). Let's get started and pip install the package:

```bash
pip install --upgrade pyannote.audio
```

Great! The weights for this model are hosted on the Hugging Face Hub. To access them, we first have to agree to the speaker diarization model's 
terms of use: [pyannote/speaker-diarization](https://huggingface.co/pyannote/speaker-diarization). And subsequently the 
segmentation model's terms of use: [pyannote/segmentation](https://huggingface.co/pyannote/segmentation).

Once complete, we can load the pre-trained speaker diarization pipeline locally on our device:

```python
from pyannote.audio import Pipeline

diarization_pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization@2.1", use_auth_token=True
)
```

Let's try it out on a sample audio file! For this, we'll load a sample of the [LibriSpeech ASR](https://huggingface.co/datasets/librispeech_asr)
dataset that consists of two different speakers that have been concatenated together to give a single audio file:

```python
from datasets import load_dataset

concatenated_librispeech = load_dataset(
    "sanchit-gandhi/concatenated_librispeech", split="train", streaming=True
)
sample = next(iter(concatenated_librispeech))
```

We can listen to the audio to see what it sounds like:

```python
from IPython.display import Audio

Audio(sample["audio"]["array"], rate=sample["audio"]["sampling_rate"])
```

Cool! We can clearly hear two different speakers, with a transition roughly 15s of the way through. Let's pass this audio 
file to the diarization model to get the speaker start / end times. Note that pyannote.audio expects the audio input to be a 
PyTorch tensor of shape `(channels, seq_len)`, so we need to perform this conversion prior to running the model:

```python
import torch

input_tensor = torch.from_numpy(sample["audio"]["array"][None, :]).float()
outputs = diarization_pipeline(
    {"waveform": input_tensor, "sample_rate": sample["audio"]["sampling_rate"]}
)

outputs.for_json()["content"]
```

```text
[{'segment': {'start': 0.4978125, 'end': 14.520937500000002},
  'track': 'B',
  'label': 'SPEAKER_01'},
 {'segment': {'start': 15.364687500000002, 'end': 21.3721875},
  'track': 'A',
  'label': 'SPEAKER_00'}]
```

This looks pretty good! We can see that the first speaker is predicted as speaking up until the 14.5 second mark, and the 
second speaker from 15.4s onwards. Now we need to get our transcription!

## Speech transcription

For the third time in this Unit, we'll use the Whisper model for our speech transcription system. Specifically, we'll load the 
[Whisper Base](https://huggingface.co/openai/whisper-base) checkpoint, since it's small enough to give good 
inference speed with reasonable transcription accuracy. As before, feel free to use any speech recognition checkpoint 
on [the Hub](https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&library=transformers&sort=trending),
including Wav2Vec2, MMS ASR or other Whisper checkpoints:

```python
from transformers import pipeline

asr_pipeline = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-base",
)
```

Let's get the transcription for our sample audio, returning the segment level timestamps as well so that we know the 
start / end times for each segment. You'll remember from Unit 5 that we need to pass the argument
`return_timestamps=True` to activate the timestamp prediction task for Whisper:

```python
asr_pipeline(
    sample["audio"].copy(),
    generate_kwargs={"max_new_tokens": 256},
    return_timestamps=True,
)
```

```text
{
    "text": " The second and importance is as follows. Sovereignty may be defined to be the right of making laws. In France, the king really exercises a portion of the sovereign power, since the laws have no weight. He was in a favored state of mind, owing to the blight his wife's action threatened to cast upon his entire future.",
    "chunks": [
        {"timestamp": (0.0, 3.56), "text": " The second and importance is as follows."},
        {
            "timestamp": (3.56, 7.84),
            "text": " Sovereignty may be defined to be the right of making laws.",
        },
        {
            "timestamp": (7.84, 13.88),
            "text": " In France, the king really exercises a portion of the sovereign power, since the laws have",
        },
        {"timestamp": (13.88, 15.48), "text": " no weight."},
        {
            "timestamp": (15.48, 19.44),
            "text": " He was in a favored state of mind, owing to the blight his wife's action threatened to",
        },
        {"timestamp": (19.44, 21.28), "text": " cast upon his entire future."},
    ],
}
```

Alright! We see that each segment of the transcript has a start and end time, with the speakers changing at the 15.48 second 
mark. We can now pair this transcription with the speaker timestamps that we got from our diarization model to get our 
final transcription.

## Speechbox

To get the final transcription, we'll align the timestamps from the diarization model with those from the Whisper model.
The diarization model predicted the first speaker to end at 14.5 seconds, and the second speaker to start at 15.4s, whereas Whisper predicted segment boundaries at
13.88, 15.48 and 19.44 seconds respectively. Since the timestamps from Whisper don't match perfectly with those from the 
diarization model, we need to find which of these boundaries are closest to 14.5 and 15.4 seconds, and segment the transcription by
speakers accordingly. Specifically, we'll find the closest alignment between diarization and transcription timestamps by 
minimising the absolute distance between both.

Luckily for us, we can use the 🤗 Speechbox package to perform this alignment. First, let's pip install `speechbox` from 
main:

```bash
pip install git+https://github.com/huggingface/speechbox
```

We can now instantiate our combined diarization plus transcription pipeline, by passing the diarization model and 
ASR model to the [`ASRDiarizationPipeline`](https://github.com/huggingface/speechbox/tree/main#asr-with-speaker-diarization) class:

```python
from speechbox import ASRDiarizationPipeline

pipeline = ASRDiarizationPipeline(
    asr_pipeline=asr_pipeline, diarization_pipeline=diarization_pipeline
)
```

<Tip>
    You can also instantiate the <code>ASRDiarizationPipeline</code> directly from pre-trained by specifying the model id
    of an ASR model on the Hub:
    <p><code>pipeline = ASRDiarizationPipeline.from_pretrained("openai/whisper-base")</code></p>
</Tip>

Let's pass the audio file to the composite pipeline and see what we get out:

```python
pipeline(sample["audio"].copy())
```

```text
[{'speaker': 'SPEAKER_01',
  'text': ' The second and importance is as follows. Sovereignty may be defined to be the right of making laws. In France, the king really exercises a portion of the sovereign power, since the laws have no weight.',
  'timestamp': (0.0, 15.48)},
 {'speaker': 'SPEAKER_00',
  'text': " He was in a favored state of mind, owing to the blight his wife's action threatened to cast upon his entire future.",
  'timestamp': (15.48, 21.28)}]
```

Excellent! The first speaker is segmented as speaking from 0 to 15.48 seconds, and the second speaker from 15.48 to 21.28 seconds,
with the corresponding transcriptions for each.

We can format the timestamps a little more nicely by defining two helper functions. The first converts a tuple of
timestamps to a string, rounded to a set number of decimal places. The second combines the speaker id, timestamp and text
information onto one line, and splits each speaker onto their own line for ease of reading:

```python
def tuple_to_string(start_end_tuple, ndigits=1):
    return str((round(start_end_tuple[0], ndigits), round(start_end_tuple[1], ndigits)))


def format_as_transcription(raw_segments):
    return "\n\n".join(
        [
            chunk["speaker"] + " " + tuple_to_string(chunk["timestamp"]) + chunk["text"]
            for chunk in raw_segments
        ]
    )
```

Let's re-run the pipeline, this time formatting the transcription according to the function we've just defined:
```python
outputs = pipeline(sample["audio"].copy())

format_as_transcription(outputs)
```

```text
SPEAKER_01 (0.0, 15.5) The second and importance is as follows. Sovereignty may be defined to be the right of making laws.
In France, the king really exercises a portion of the sovereign power, since the laws have no weight.

SPEAKER_00 (15.5, 21.3) He was in a favored state of mind, owing to the blight his wife's action threatened to cast upon
his entire future.
```

There we go! With that, we've both diarized and transcribe our input audio and returned speaker-segmented transcriptions.
While the minimum distance algoirthm to align the diarized timestamps and transcribed timestamps is simple, it
works well in practice. If you want to explore more advanced methods for combining the timestamps, the
source code for the `ASRDiarizationPipeline` is a good place to start: [speechbox/diarize.py](https://github.com/huggingface/speechbox/blob/96d2d1a180252d92263f862a1cd25a48860f1aed/src/speechbox/diarize.py#L12)
