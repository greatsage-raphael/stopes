#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = [
    "stopes",
    "stopes.core",
    "stopes.core.jobs_registry",
    "stopes.core.tests",
    "stopes.modules",
    "stopes.modules.bitext",
    "stopes.modules.bitext.indexing",
    "stopes.modules.bitext.mining",
    "stopes.modules.evaluation",
    "stopes.modules.monolingual",
    "stopes.modules.nmt_bitext_eval_utils",
    "stopes.modules.preprocess",
    "stopes.modules.tests",
    "stopes.pipelines",
    "stopes.pipelines.bitext",
    "stopes.pipelines.filtering",
    "stopes.pipelines.filtering.filters",
    "stopes.pipelines.monolingual",
    "stopes.pipelines.monolingual.utils",
    "stopes.pipelines.prepare_data",
    "stopes.utils",
]

package_data = {
    "": ["*"],
    "stopes.modules": ["translation/*"],
    "stopes.pipelines.bitext": [
        "conf/*",
        "conf/binarize/*",
        "conf/calculate_distances/*",
        "conf/embed_text/*",
        "conf/embed_text/config/*",
        "conf/embed_text/config/encoder/*",
        "conf/embed_text/config/preprocess/*",
        "conf/eval/*",
        "conf/fb_data/*",
        "conf/launcher/*",
        "conf/launcher/cache/*",
        "conf/merge_indexes/*",
        "conf/mine_indexes/*",
        "conf/mine_sentences/*",
        "conf/moses/*",
        "conf/moses_filter/*",
        "conf/populate_index/*",
        "conf/preproc_binarize_mined/*",
        "conf/preset/*",
        "conf/spm/*",
        "conf/train_fairseq/*",
        "conf/train_fairseq/config/*",
        "conf/train_fairseq/config/params/*",
        "conf/train_fairseq/config/params/model/*",
        "conf/train_index/*",
        "conf/training_after_mining_pipeline/*",
    ],
    "stopes.pipelines.filtering": ["conf/*", "scripts/*"],
    "stopes.pipelines.monolingual": ["conf/*", "conf/fb_preset/*"],
}

install_requires = ["hydra-core>=1.2.0", "submitit>=1.4.2", "tqdm", "joblib"]

extras_require = {
    "dev": [
        "pytest>=4.3.0",
        "pytest-asyncio>=0.15.0",
        "pytest-cov>=2.6.1",
        "coverage[toml]>=5.1",
        "black==22.3.0",
        "isort>=5.10.1",
        "mypy>=0.782",
        "types-emoji",
        "pylint>=2.8.0",
        "flit>=3.5.1",
    ],
    "mining": ["fairscale", "faiss-gpu", "sentencepiece", "numpy"],
    "mono": [
        "xxhash",
        "fasttext",
        "sentence_splitter",
        "sentencepiece",
        "indic-nlp-library",
        "emoji",
    ],
}

setup(
    name="stopes",
    version="1.0.0",
    description="Large-Scale Translation Data Mining.",
    author="Facebook AI Research",
    author_email=None,
    url=None,
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">=3.8",
)
