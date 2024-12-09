# The Audio Transformers Course

This repo contains the content that's used to create [Hugging Face's Audio Transformers Course](https://huggingface.co/learn/audio-course/). 
The course teaches you about applying Transformers to various tasks in audio and speech processing.It's completely free and open-source!

## 🌎 Languages and translations

| Language                                                                      | Source                                                                             | Authors                                                                                                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bengali](https://huggingface.co/learn/audio-course/bn/chapter0/introduction)                     | [`chapters/bn`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/bn)       |                                                                               |
| [English](https://huggingface.co/learn/audio-course/chapter0/introduction)                        | [`chapters/en`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/en)       |                                                                               |
| [Spanish](https://huggingface.co/learn/audio-course/es/chapter0/introduction)                     | [`chapters/es`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/es)       |                                                                               |
| [French](https://huggingface.co/learn/audio-course/fr/chapter0/introduction)                      | [`chapters/fr`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/fr)       |                                                                               |
| [Korean](https://huggingface.co/learn/audio-course/ko/chapter0/introduction)                      | [`chapters/ko`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/ko)       |                                                                               |
| [Russian](https://huggingface.co/learn/audio-course/ru/chapter0/introduction)                     | [`chapters/ru`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/ru)       | [@blademoon](https://github.com/blademoon), [@Lightmourne](https://github.com/Lightmourne)                                                                              |
| [Turkish](https://huggingface.co/learn/audio-course/tr/chapter0/introduction)                     | [`chapters/tr`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/tr)       |                                                                               |
| [Chinese (simplified)](https://huggingface.co/learn/audio-course/zh-CN/chapter0/introduction)     | [`chapters/zh-CN`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/zh-CN) |                                                                               |
| [Italian](https://huggingface.co/learn/audio-course/it/chapter0/introduction)     | [`chapters/it`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/it) |    [@leofltt](https://github.com/leofltt)                                                                           |
### Translating the course into your language

As part of our mission to democratise machine learning, we'd love to have the course available in many more languages! 
Please follow the steps below if you'd like to help translate the course into your language 🙏.

**🗞️ Open an issue**

To get started, navigate to the [_Issues_](https://github.com/huggingface/audio-transformers-course/issues) page of 
this repo and check if anyone else has opened an issue for your language. If not, open a new issue by selecting 
the _Translation template_ from the _New issue_ button.

Once an issue is created, post a comment to indicate which chapters you'd like to work on and we'll add your name to the list.

**🗣 Join our Discord**

Since it can be difficult to discuss translation details quickly over GitHub issues, we have created dedicated channels 
for each language on our Discord server. Join here 👉: [http://hf.co/join/discord](http://hf.co/join/discord)

**🍴 Fork the repository**

Next, you'll need to [fork this repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo). You can do this 
by clicking on the **Fork** button on the top-right corner of this repo's page.

Once you've forked the repo, you'll want to get the files on your local machine for editing. You can do that by cloning the fork with Git as follows:

```bash
git clone https://github.com/YOUR-USERNAME/audio-transformers-course
```

**📋 Copy-paste the English files with a new language code**

The course files are organised under a main directory:

* [`chapters`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters): all the text and code snippets associated with the course.

You'll only need to copy the files in the [`chapters/en`](https://github.com/huggingface/audio-transformers-course/tree/main/chapters/en) 
directory, so first navigate to your fork of the repo and run the following:

```bash
cd ~/path/to/audio-transformers-course
cp -r chapters/en/CHAPTER-NUMBER chapters/LANG-ID/CHAPTER-NUMBER
```

Here, `CHAPTER-NUMBER` refers to the chapter you'd like to work on and `LANG-ID` should be ISO 639-1 (two lower case letters) 
language code -- see [here](https://www.loc.gov/standards/iso639-2/php/code_list.php) for a handy table.
Alternatively, {two lowercase letters}-{two uppercase letters} format is also supported, e.g. `zh-CN`, here's 
an [example](https://huggingface.co/learn/nlp-course/zh-CN/chapter1/1).

**✍️ Start translating**

Now comes the fun part - translating the text! The first thing we recommend is translating the part of the `_toctree.yml` file that corresponds to your chapter. This file is used to render the table of contents on the website and provide the links to the Colab notebooks. The only fields you should change are the `title`, ones -- for example, here are the parts of `_toctree.yml` that we'd translate for [Chapter 0 of the NLP course](https://huggingface.co/course/chapter0/1?fw=pt):

```yaml
- title: 0. Setup # Translate this!
  sections:
  - local: chapter0/1 # Do not change this!
    title: Introduction # Translate this!
```

> 🚨 Make sure the `_toctree.yml` file only contains the sections that have been translated! Otherwise you won't be able to build the content on the website or locally (see below how).


Once you have translated the `_toctree.yml` file, you can start translating the [MDX](https://mdxjs.com/) files associated with your chapter.

> 🙋 If the `_toctree.yml` file doesn't yet exist for your language, you can simply create one by copy-pasting from the English version and deleting the sections that aren't related to your chapter. Just make sure it exists in the `chapters/LANG-ID/` directory!

**👷‍♂️ Build the course locally**

Once you're happy with your changes, you can preview how they'll look by first installing the [`doc-builder`](https://github.com/huggingface/doc-builder) tool that we use for building all documentation at Hugging Face:

```shell
python -m pip install hf-doc-builder
```

```shell
doc-builder preview audio-transformers-course ../audio-transformers-course/chapters/LANG-ID --not_python_module
```

This will build and render the course on [http://localhost:3000/](http://localhost:3000/). Although the content looks much nicer on the Hugging Face website, this step will still allow you to check that everything is formatted correctly.

**🚀 Submit a pull request**

If the translations look good locally, the final step is to prepare the content for a pull request. Here, the first think to check is that the files are formatted correctly. For that you can run:

```
pip install -r requirements.txt
make style
```

Once that's run, commit any changes, open a pull request, and wait for a review. Congratulations, you've now completed your first translation 🥳!

> 🚨 To build the course on the website, double-check your language code exists in `languages` field of the `build_documentation.yml` and `build_pr_documentation.yml` files in the `.github` folder. If not, just add them in their alphabetical order.

## 📔 Jupyter notebooks

The Jupyter notebooks containing all the code from the course are hosted on the [`huggingface/notebooks`](https://github.com/huggingface/notebooks) repo. If you wish to generate them locally, first install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

Then run the following script:

```bash
python utils/generate_notebooks.py --output_dir nbs
```

This script extracts all the code snippets from the chapters and stores them as notebooks in the `nbs` folder (which is ignored by Git by default).

## ✍️ Contributing a new chapter

> Note: we are not currently accepting community contributions for new chapters. These instructions are for the Hugging Face authors.

Adding a new chapter to the course is quite simple:

1. Create a new directory under `chapters/en/chapterX`, where `chapterX` is the chapter you'd like to add.
2. Add numbered MDX files `sectionX.mdx` for each section. 
3. Update the `_toctree.yml` file to include your chapter sections -- this information will render the table of contents on the website. If your section involves both the PyTorch and TensorFlow APIs of `transformers`, make sure you include links to both Colabs in the `colab` field.

If you get stuck, check out one of the existing chapters -- this will often show you the expected syntax.

Once you are happy with the content, open a pull request and wait for a review. We recommend adding the first chapter draft as a single pull request -- the team will then provide feedback internally to iterate on the content 🤗!

## 🙌 Acknowledgements

The structure of this repo and README are inspired by the wonderful [Advanced NLP with spaCy](https://github.com/ines/spacy-course) course.
