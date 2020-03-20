# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import pytest


@pytest.mark.gpu
@pytest.mark.integration
def test_ddp_extractive_summarization_cnndm_transformers(scripts, tmp):
    script = scripts["ddp_bertsumext"]
    summary_filename = "bertsumext_prediction.txt"
    import subprocess

    process = subprocess.Popen(
        [
            "python",
            script,
            "--data_dir",
            tmp,
            "--cache_dir",
            tmp,
            "--output_dir",
            tmp,
            "--quick_run",
            "true",
            "--summary_filename",
            summary_filename,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    print(stdout)
    if process.returncode:
        print(stdout)
        print(stderr)
        assert False
    assert os.path.exists(os.path.join(tmp, summary_filename))


@pytest.mark.gpu
@pytest.mark.integration
def test_ddp_abstractive_summarization_cnndm_transformers(scripts, tmp):
    script = scripts["ddp_bertsumabs"]
    summary_filename = "bertsumext_prediction.txt"
    import subprocess

    process = subprocess.Popen(
        [
            "python",
            script,
            "--data_dir",
            tmp,
            "--cache_dir",
            tmp,
            "--output_dir",
            tmp,
            "--quick_run",
            "true",
            "--summary_filename",
            summary_filename,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    print(stdout)
    if process.returncode:
        print(stdout)
        print(stderr)
        assert False
        raise RuntimeError("something bad happened")
    assert os.path.exists(os.path.join(tmp, summary_filename))