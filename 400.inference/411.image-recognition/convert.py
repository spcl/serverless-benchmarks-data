import torchvision.models as models
import torch

model = models.resnet50(pretrained=False)
model.load_state_dict(torch.load("model/resnet50-19c8e357.pth"))
model.eval()

dummy_input = torch.rand(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, dummy_input)
traced_script_module.save("model/resnet50.pt")
