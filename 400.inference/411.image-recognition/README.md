
**Model**

The benchmark uses a pretrained resnet50 from torchvision.

Source: https://download.pytorch.org/models/resnet50-19c8e357.pth

The C++ version of model - `resnet50.pt` - has been generated with the `convert.py` script, with `torch==2.0.0` and `torchvision==0.12.0`, [as recommended by PyTorch documentation](https://github.com/pytorch/tutorials/blob/2.0-RC-TEST/advanced_source/cpp_export.rst).

**Test data**

`fake-resnet` has been generated through the `make_fake_imagenet.sh` script from `mlcommons/inference` project.

Source: https://github.com/mlcommons/inference/blob/d9df70bfb1a1d9898841bb3cb865359b817069f2/v0.5/classification_and_detection/tools/make_fake_imagenet.sh
