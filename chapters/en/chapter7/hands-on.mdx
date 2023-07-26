# Hands-on exercise

In this Unit, we consolidated the material covered in the previous six units of the course to build three integrated
audio applications. As you've experienced, building more involved audio tools is fully within reach by using the 
foundational skills you've acquired in this course.

The hands-on exercise takes one of the applications covered in this Unit, and extends it with a few multilingual 
tweaks 🌍 Your objective is to take the [cascaded speech-to-speech translation Gradio demo](https://huggingface.co/spaces/course-demos/speech-to-speech-translation)
from the first section in this Unit, and update it to translate to any **non-English** language. That is to say, the 
demo should take speech in language X, and translate it to speech in language Y, where the target language Y is not
English. You should start by [duplicating](https://huggingface.co/spaces/course-demos/speech-to-speech-translation?duplicate=true)
the template under your Hugging Face namespace. There's no requirement to use a GPU accelerator device - the free CPU
tier works just fine 🤗 However, you should ensure that the visibility of your demo is set to **public**. This is required
such that your demo is accessible to us and can thus be checked for correctness.

Tips for updating the speech translation function to perform multilingual speech translation are provided in the 
section on [speech-to-speech translation](speech-to-speech). By following these instructions, you should be able
to update the demo to translate from speech in language X to text in language Y, which is half of the task!

To synthesise from text in language Y to speech in language Y, where Y is a multilingual language, you will need 
to use a multilingual TTS checkpoint. For this, you can either use the SpeechT5 TTS checkpoint that you fine-tuned 
in the previous hands-on exercise, or a pre-trained multilingual TTS checkpoint. There are two options for pre-trained 
checkpoints, either the checkpoint [sanchit-gandhi/speecht5_tts_vox_nl](https://huggingface.co/sanchit-gandhi/speecht5_tts_vox_nl),
which is a SpeechT5 checkpoint fine-tuned on the Dutch split of the [VoxPopuli](https://huggingface.co/datasets/facebook/voxpopuli)
dataset, or an MMS TTS checkpoint (see section on [pretrained models for TTS](../chapter6/pre-trained_models)).

<Tip>
    In our experience experimenting with the Dutch language, using an MMS TTS checkpoint results in better performance than a
    fine-tuned SpeechT5 one, but you might find that your fine-tuned TTS checkpoint is preferable in your language.
    If you decide to use an MMS TTS checkpoint, you will need to update the <a href="https://huggingface.co/spaces/course-demos/speech-to-speech-translation/blob/a03175878f522df7445290d5508bfb5c5178f787/requirements.txt#L2">requirements.txt</a>
    file of your demo to install <code>transformers</code> from the PR branch:
    <p><code>git+https://github.com/hollance/transformers.git@6900e8ba6532162a8613d2270ec2286c3f58f57b</code></p>
</Tip>


Your demo should take as input an audio file, and return as output another audio file, matching the signature of the 
[`speech_to_speech_translation`](https://huggingface.co/spaces/course-demos/speech-to-speech-translation/blob/3946ba6705a6632a63de8672ac52a482ab74b3fc/app.py#L35)
function in the template demo. Therefore, we recommend that you leave the main function `speech_to_speech_translation` 
as is, and only update the [`translate`](https://huggingface.co/spaces/course-demos/speech-to-speech-translation/blob/a03175878f522df7445290d5508bfb5c5178f787/app.py#L24)
and [`synthesise`](https://huggingface.co/spaces/course-demos/speech-to-speech-translation/blob/a03175878f522df7445290d5508bfb5c5178f787/app.py#L29)
functions as required.

Once you have built your demo as a Gradio demo on the Hugging Face Hub, you can submit it for assessment. Head to the 
Space [audio-course-u7-assessment](https://huggingface.co/spaces/huggingface-course/audio-course-u7-assessment) and 
provide the repository id of your demo when prompted. This Space will check that your demo has been built correctly by 
sending a sample audio file to your demo and checking that the returned audio file is indeed non-English. If your demo 
works correctly, you'll get a green tick next to your name on the overall [progress space](https://huggingface.co/spaces/MariaK/Check-my-progress-Audio-Course) ✅
