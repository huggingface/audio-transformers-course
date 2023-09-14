# Audio generation with a pipeline

Audio generation encompasses a versatile set of tasks that involve producing an audio output. The tasks 
that we will look into here are speech generation (aka "text-to-speech") and music generation. In text-to-speech, a 
model transforms a piece of text into lifelike spoken language sound, opening the door to applications such as virtual assistants, 
accessibility tools for the visually impaired, and personalized audiobooks. 
On the other hand, music generation can enable creative expression, and finds its use mostly in entertainment and game 
development industries. 

In 🤗 Transformers, you'll find a pipeline that covers both of these tasks. This pipeline is called `"text-to-audio"`, 
but for convenience, it also has a `"text-to-speech"` alias. Here we'll use both, and you are free to pick whichever 
seems more applicable for your task. 

Let's explore how you can use this pipeline to start generating audio narration for texts, and music with just a few lines of code.

This pipeline is new to 🤗 Transformers and comes part of the version 4.32 release. Thus you'll need to upgrade the library to the latest version to get the feature:

```bash
pip install --upgrade transformers
```

## Generating speech

Let's begin by exploring text-to-speech generation. First, just as it was the case with audio classification and automatic 
speech recognition, we'll need to define the pipeline. We'll define a text-to-speech pipeline since it best describes our task, and use the [`suno/bark-small`](https://huggingface.co/suno/bark-small) checkpoint:

```python
from transformers import pipeline

pipe = pipeline("text-to-speech", model="suno/bark-small")
```

The next step is as simple as passing some text through the pipeline. All the preprocessing will be done for us under the hood: 

```python
text = "Ladybugs have had important roles in culture and religion, being associated with luck, love, fertility and prophecy. "
output = pipe(text)
```

In a notebook, we can use the following code snippet to listen to the result: 

```python
from IPython.display import Audio

Audio(output["audio"], rate=output["sampling_rate"])
```

The model that we're using with the pipeline, Bark, is actually multilingual, so we can easily substitute the initial 
text with a text in, say, French, and use the pipeline in the exact same way. It will pick up on the language all by itself:

```python
fr_text = "Contrairement à une idée répandue, le nombre de points sur les élytres d'une coccinelle ne correspond pas à son âge, ni en nombre d'années, ni en nombre de mois. "
output = pipe(fr_text)
Audio(output["audio"], rate=output["sampling_rate"])
```

Not only is this model multilingual, it can also generate audio with non-verbal communications and singing. Here's how 
you can make it sing: 

```python
song = "♪ In the jungle, the mighty jungle, the ladybug was seen. ♪ "
output = pipe(song)
Audio(output["audio"], rate=output["sampling_rate"])
```

We'll dive deeper into Bark specifics in the later unit dedicated to Text-to-speech, and will also show how you can use 
other models for this task. Now, let's generate some music!

## Generating music

Just as before, we'll begin by instantiating a pipeline. For music generation, we'll define a text-to-audio pipeline, and initialise it with the pretrained checkpoint [`facebook/musicgen-small`](https://huggingface.co/facebook/musicgen-small) 

```python
music_pipe = pipeline("text-to-audio", model="facebook/musicgen-small")
```

Let's create a text description of the music we'd like to generate:

```python
text = "90s rock song with electric guitar and heavy drums"
```

We can control the length of the generated output by passing an additional `max_new_tokens` parameter to the model. 

```python
forward_params = {"max_new_tokens": 512}

output = music_pipe(text, forward_params=forward_params)
Audio(output["audio"][0], rate=output["sampling_rate"])
```
